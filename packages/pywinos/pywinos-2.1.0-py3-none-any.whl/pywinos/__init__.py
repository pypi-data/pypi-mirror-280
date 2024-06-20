__author__ = 'Andrey Komissarov'
__email__ = 'a.komisssarov@gmail.com'
__date__ = '12.2019'

import json
import socket
import subprocess
from json import JSONDecodeError

import plogger
import winrm
import xmltodict
from requests.exceptions import ConnectionError
from winrm import Protocol
from winrm.exceptions import (InvalidCredentialsError,
                              WinRMError,
                              WinRMTransportError,
                              WinRMOperationTimeoutError)

from pywinos.exceptions import ServiceLookupError, RemoteCommandExecutionError, LocalCommandExecutionError


class WinResponse:
    """Response parser"""

    def __init__(self, response, cmd: str = None):
        self.response = response
        self.command = cmd

    def __str__(self):
        dict_ = self.dict
        return json.dumps(dict_, default=self._convert_data, indent=4)

    @property
    def stdout(self):
        try:
            stdout = self._decoder(self.response.std_out)
        except AttributeError:
            stdout = self._decoder(self.response.stdout)

        out = stdout
        try:
            out = json.loads(stdout)
            self._clean_stdout(out)
        except (TypeError, JSONDecodeError):
            ...

        return out

    @property
    def stderr(self) -> str:
        try:
            stderr = self._decoder(self.response.std_err)
        except AttributeError:
            stderr = self._decoder(self.response.stderr)

        err = None if '#< CLIXML\r\n<Objs Version="1.1.0.1"' in stderr else stderr
        return err

    @property
    def exited(self) -> int:
        """Get exit code"""

        try:
            exited = self.response.status_code
        except AttributeError:
            exited = self.response.returncode
        return exited

    @property
    def ok(self) -> bool:
        try:
            return self.response.status_code == 0
        except AttributeError:
            return self.response.returncode == 0

    @property
    def raw(self) -> winrm.Response:
        """Returns raw WinRM response."""

        return self.response

    # ---------- Auxiliary methods ---------
    @property
    def to_debug_log(self):
        msg = (f'\traw: {self.response}\n'
               f'\tok: {self.ok}\n'
               f'\tstdout: {self.stdout}\n'
               f'\tstderr: {self.stderr}')

        return msg

    @property
    def dict(self):
        """Get raw response from WinRM and return result dict"""

        result = {
            'exit_code': self.exited,
            'ok': self.ok,
            'stdout': self.stdout,
            'stderr': self.stderr,
            'cmd': self.command,
            'raw': self.response,
        }

        return result

    @staticmethod
    def _decoder(response):
        return response.decode('cp1252').strip()

    @staticmethod
    def _convert_data(obj):
        """Convert data in order to get brief raw response data"""

        if isinstance(obj, winrm.Response):
            response = f'<Exit={obj.status_code}, out={obj.std_out}, err={obj.std_err[:30]}...>'
            return response

    @staticmethod
    def _clean_stdout(out: dict) -> dict:
        """Clean stdout from useless and service data.

        Args:
            out:
        """

        # Remove redundant info
        key_remove = ('PSDrive', 'PSProvider', 'Directory', 'CimClass', 'CimInstanceProperties', 'CimSystemProperties',
                      'Modules', 'StartInfo', 'Threads')
        match out:
            case list():
                [i.pop(k, None) for i in out for k in key_remove]
            case dict():  # Only 1 object exists
                [out.pop(k, None) for k in key_remove]

        return out


class WinOSClient:
    """The cross-platform tool to work with remote and local Windows OS.

    Returns response object with exit code, sent command, stdout/stderr, json.
    Check response methods.
    """

    _URL = 'https://pypi.org/project/pywinrm/'

    def __init__(self,
                 host: str = '',
                 username: str = None,
                 password: str = None,
                 log_enabled: bool = True,
                 log_level: str | int = 'INFO'):
        self.host = host
        self.username = username
        self.password = password
        self.logger = plogger.logger('WinOSClient', enabled=log_enabled, level=log_level)

    def __str__(self):
        str_msg = (f'==========================\n'
                   f'Remote IP: {self.host}\n'
                   f'Username: {self.username}\n'
                   f'Password: {self.password}\n'
                   f'Host available: {self.is_host_available()}\n'
                   f'==========================')
        return str_msg

    def list_all_methods(self):
        """Returns all available public methods"""

        return [method for method in dir(self) if not method.startswith('_')]

    def is_host_available(self, port: int = 5985, timeout: int = 5) -> bool:
        """Check remote host is available using specified port.

        Port 5985 used by default
        """

        is_local = not self.host or self.host == 'localhost' or self.host == '127.0.0.1'
        if is_local:
            return True

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(timeout)
            response = sock.connect_ex((self.host, port))
            result = False if response else True
            self.logger.info(f'{self.host} is available: {result}')
            return result

    # ---------- Service section ----------
    def __create_session(self):
        """Create WinRM session connection to a remote server"""

        try:
            credentials = self.username, self.password
            self.logger.debug(f'Create the Session to the {self.host} using credentials {credentials}')
            session = winrm.Session(self.host, auth=credentials)
            self.logger.debug('The Session has been created')
        except TypeError as err:
            self.logger.exception(f'Verify credentials ({self.username=}, {self.password=})')
            raise err

        return session

    def __set_protocol(self, endpoint: str, transport: str = 'ntlm'):
        """Create Protocol using low-level API

        :param endpoint: http://<IP>:5985/wsman, https://<IP>:5986/wsman
        :param transport: ntlm, credssp
        :return: Session configured with a protocol
        """

        self.logger.debug('Create Protocol using low-level API')
        session = self.__create_session()
        protocol_cfg = {
            'endpoint': endpoint,
            'transport': transport,
            'username': self.username,
            'password': self.password,
            'server_cert_validation': 'ignore',
            'message_encryption': 'always',
            'operation_timeout_sec': 20
        }
        protocol = Protocol(**protocol_cfg)  # Create Protocol instance
        session.protocol = protocol  # Point protocol to the Session
        self.logger.debug(f'Protocol was set to the Session with the config:\n{json.dumps(protocol_cfg, indent=4)}')
        return session

    def __client(self, use_cred_ssp: bool = False, insecure: bool = False):
        """The client to send PowerShell or command-line commands

        :param use_cred_ssp: Specify if CredSSP is used
        :param insecure: Insecure! http://{IP}:5985/wsman will be used!
        :return: Client
        """

        self.logger.debug(f'Creating client to send PowerShell or command-line commands. Use CredSSP: {use_cred_ssp}')

        endpoint = f'https://{self.host}:5986' if use_cred_ssp and not insecure else f'http://{self.host}:5985'
        endpoint += '/wsman'
        transport = 'credssp' if use_cred_ssp else 'ntlm'
        client = self.__set_protocol(endpoint=endpoint, transport=transport)

        msg_log = (f'The client has been created:\n\t'
                   f'Endpoint: {endpoint}\n\t'
                   f'Verify cert: {insecure}\n\t'
                   f'Transport: {transport}\n\t')
        self.logger.debug(msg_log)
        return client

    @staticmethod
    def __get_transport_name(ps: bool = True) -> str:
        """Get transport name

        :param ps:
        :return: "PS" or "CMD"
        """

        return 'PS' if ps else 'CMD'

    def exec_command(self, cmd: str,
                     ps: bool = False,
                     use_cred_ssp: bool = False,
                     insecure: bool = False,
                     ignore_errors: bool = False,
                     *args) -> WinResponse:
        """Execute PS or command-line command.

        :param cmd: Command to execute
        :param ps: Specify if PowerShell is used. Otherwise, command-line will be used
        :param use_cred_ssp: Use CredSSP
        :param insecure: Insecure! http://{IP}:5985/wsman will be used!
        :param ignore_errors: Ignore errors
        :return:
        """

        client = self.__client(use_cred_ssp=use_cred_ssp, insecure=insecure)

        try:
            if ps:
                self.logger.info(f'{self.host:<14} | PS  | {cmd}')
                response = client.run_ps(cmd)  # status_code, std_err, std_out
            else:
                self.logger.info(f'{self.host:<14} | CMD | {cmd}')
                response = client.run_cmd(cmd, [arg for arg in args])

        # Catch exceptions
        except InvalidCredentialsError as err:
            self.logger.error(f'{self.host:<14}| Invalid credentials: {self.username}@{self.password}. {err}.')
            raise InvalidCredentialsError
        except ConnectionError as err:
            self.logger.error(f'{self.host:<14}| Connection error:\n{err}.')
            raise ConnectionError
        except (WinRMError,
                WinRMOperationTimeoutError,
                WinRMTransportError) as err:
            self.logger.error(f'{self.host:<14}| WinRM error:\n{err}.')
            raise err
        except Exception as err:
            self.logger.error(f'{self.host:<14}| Something went wrong:\n{err}.')
            raise err

        parsed = WinResponse(response=response, cmd=cmd)

        # Log response
        transport_sent = self.__get_transport_name(ps)

        # Log ERROR
        msg_err = f'{self.host:<14} | {transport_sent:<3} | Something went wrong! {parsed.exited}:\n\t{parsed.stderr}'
        if exited := parsed.exited:  # Exit code != 0

            if ignore_errors:
                self.logger.warning(f'Exit code: {exited}, but suppress error enabled. Processing...')
            else:
                self.logger.error(msg_err)
                raise RemoteCommandExecutionError(parsed.stderr)

        # Log WARNING
        if parsed.stderr:  # warning detected
            self.logger.warning(msg_err)
        else:
            # Log INFO and DEBUG
            out = json.dumps(parsed.stdout, indent=4)
            msg_to_log = f'{parsed.exited}:\n\t{out}'
            self.logger.info(f'{self.host:<14} | {transport_sent:<3} | {msg_to_log}')

        self.logger.debug(f'{self.host:<14} | {transport_sent:<3} |\n{parsed.to_debug_log}')

        return parsed

    def _run_local(self, cmd: str, timeout: int = 60):
        """Main function to send commands using subprocess LOCALLY.

        Used command-line (cmd.exe, powershell or bash)

        Add mandatory param "CMD" or "PS" to use appropriate transport

        :param cmd: string, command
        :param timeout: timeout for command
        :return: Decoded response
        """

        self.logger.info(cmd)

        response = subprocess.run(cmd, capture_output=True, timeout=timeout)
        parsed = WinResponse(response, cmd=cmd)

        # Log ERROR
        msg_err = f'Something went wrong!{parsed.exited}:\n\t{parsed.stderr}'
        if parsed.exited:  # Exit code != 0 or stderr contains text
            self.logger.error(msg_err)
            raise RemoteCommandExecutionError(parsed.stderr)

        # Log WARNING
        if parsed.stderr:  # warning detected
            self.logger.warning(msg_err)

        # Log INFO and DEBUG
        msg_to_log = f'{parsed.exited}:\n\t{parsed.stdout}' if parsed.stdout else f'{parsed.exited}:'
        self.logger.info(msg_to_log)
        self.logger.debug(f'\n{parsed.to_debug_log}')

        return parsed

    # ----------------- Main low-level methods ----------------
    def run_cmd(self,
                cmd: str,
                use_cred_ssp: bool = False,
                insecure: bool = False,
                ignore_errors: bool = False,
                *args) -> WinResponse:
        """Allows executing cmd command on a remote server.

        :param cmd: Command to execute using cmd.exe
        :param use_cred_ssp:
        :param insecure: Insecure! http://{IP}:5985/wsman will be used!
        :param ignore_errors: Ignore errors
        :param args: additional command arguments
        :return: WinResponse class
        """

        cmd = {
            'cmd': cmd,
            'ps': False,
            'use_cred_ssp': use_cred_ssp,
            'insecure': insecure,
            'ignore_errors': ignore_errors,
        }

        result = self.exec_command(*args, **cmd)
        return result

    def run_ps(self,
               cmd: str,
               use_cred_ssp: bool = False,
               insecure: bool = False,
               ignore_errors: bool = False, ) -> WinResponse:
        """Allows executing PowerShell command or script using a remote shell.

        :param cmd: Command to execute using PoserShell
        :param use_cred_ssp:
        :param insecure: Insecure! http://{IP}:5985/wsman will be used!
        :param ignore_errors: Ignore errors
        :return: WinResponse class
        """

        cmd = {
            'cmd': cmd,
            'ps': True,
            'use_cred_ssp': use_cred_ssp,
            'insecure': insecure,
            'ignore_errors': ignore_errors,
        }
        result = self.exec_command(**cmd)
        return result

    def run_cmd_local(self, cmd: str, timeout: int = 60):
        """Allows executing cmd command on a local server.

        :param cmd: command to execute
        :param timeout: timeout, sec
        :return: Object with exit code, stdout and stderr
        """

        return self._run_local(cmd, timeout)

    def run_ps_local(self, cmd: str = None, script: str = None, timeout: int = 60, **params):
        """Allows executing PowerShell command on a remote server.

        :param cmd: command to execute
        :param script:
        :param timeout: timeout, sec
        :param params:
        :return: Object with exit code, stdout and stderr
        """

        cmd = f'powershell -command "{cmd}"'
        if script:
            params_ = ' '.join([f'-{key} {value}' for key, value in params.items()])
            cmd = f'powershell -file {script} {params_}'

        return self._run_local(cmd, timeout)

    # ----------------- High-level methods ----------------
    def remove_item(self, path: str, ignore_errors: bool = False) -> bool:
        r"""Remove file or directory recursively on remote server

        - Remove-Item -Path "{path}" -Recurse -Force
        - Remove-Item -Path "X:1\*" -Recurse -Force

        Args:
            path: Full file\directory\registry path (HKLM:\\SOFTWARE\\StarWind Software)
            ignore_errors: Suppress errors
        """

        cmd = f'Remove-Item -Path "{path}" -Recurse -Force'
        if ignore_errors:
            cmd += ' -ErrorAction SilentlyContinue'

        result = self.run_ps(cmd)
        return result.ok

    def get_os_info(self) -> dict:
        """Get OS info"""

        cmd = 'Get-CimInstance Win32_OperatingSystem | ConvertTo-Json -Depth 1'
        return self.run_ps(cmd).stdout

    def get_os_name(self) -> str:
        """Get OS name only"""

        return self.get_os_info().get('Caption')

    def exists(self, path: str) -> bool:
        """Check file/directory exists from remote server

        - Test-Path -Path "{path}"

        Args:
            path: Full path. Can be network path. Share must be attached!
        """

        cmd = f'Test-Path -Path "{path}"'
        result = self.run_ps(cmd)
        return True if result.stdout == 'True' else False

    def get_content(self, path: str) -> str | dict:
        """Get remote file content

        - Get-Content "{path}"

        Args:
            path: File path

        Returns:
            File content
        """

        cmd = f'Get-Content "{path}"'
        result = self.run_ps(cmd)
        return result.stdout

    def select_string(self, *path: str, pattern: str, case_sensitive: bool = True) -> dict:
        r"""Find text in file contents.

        - Select-String -Path "{path}" -Pattern "{pattern}"

        Usage:
            - select_string(r"X:\Diskspd\readme.txt", pattern="Diskspd Tool")
            - select_string(r"X:\Diskspd\readme.txt", r"X:\Diskspd\readme.txt.txt", pattern="Diskspd Tool")

        Args:
            path: File path
            pattern: Pattern to look for. Example: "Data corruption occurred"
            case_sensitive: True by default

        Returns:
            Files info with pattern matching found
        """

        path_ = f'"{path[0]}"' if len(path) == 1 else f'@{path}'
        cmd = f'Select-String -Path {path_} -Pattern "{pattern}"'
        if case_sensitive:
            cmd += ' -CaseSensitive'
        cmd += ' | ConvertTo-Json'

        result = self.run_ps(cmd)
        result = self._convert_result(result, key='Filename')

        return result

    def get_dir_size(self, path: str) -> int:
        r"""Get directory size in bytes

        Ags:
            path: Directory full path. Example, C:\test | D:

        Returns:
            Directory size in bytes
        """

        cmd = f'(Get-ChildItem "{path}" -Recurse | Measure Length -Sum).Sum'
        try:
            result = int(self.run_ps(cmd).stdout)
        except ValueError:
            return 0

        return result

    def get_item(self, path: str) -> dict:
        """Get remote Windows file info (versions, size, etc...)

        - Get-Item -Path "{path}"

        Args:
            path: Full path to the file
        """

        cmd = fr'Get-Item "{path}" | ConvertTo-Json -Depth 1'

        try:
            response = self.run_ps(cmd)
        except RemoteCommandExecutionError:
            self.logger.error(f'File ({path}) not found.')
            raise FileNotFoundError(path)

        result = self._convert_result(response)
        return result

    def get_child_item(self, path: str, mask: str = '') -> dict:
        r"""Get the items and child items in one or more specified locations.

        - Get-ChildItem -path "{path}" | Sort LastWriteTime -Descending

        Args:
            path: Root directory to search. List dir if specified this param only. X:\, X:\Build
            mask: List dir by mask by filter. "*.txt"
        """

        cmd = f'Get-ChildItem "{path}" -Filter "{mask}" | Sort LastWriteTime -Descending | ConvertTo-Json -Depth 1'
        response = self.run_ps(cmd)
        result = self._convert_result(response)

        return result

    def get_item_property(self, path: str) -> dict:
        """Get remote Windows file property

        - Get-ItemProperty -Path "{path}"

        Args:
            path: Full path to the file
        """

        cmd = fr'Get-ItemProperty "{path}" | ConvertTo-Json -Depth 1'
        try:
            response = self.run_ps(cmd)
        except RemoteCommandExecutionError:
            self.logger.error(f'File ({path}) not found.')
            raise FileNotFoundError(path)

        result = self._convert_result(response, key='PSChildName')
        return result

    def get_hash(self, path: str, algorithm: str = 'MD5') -> str:
        """Get file hash on remote server.

        - (Get-FileHash -Path {path} -Algorithm {algorithm}).Hash

        Args:
            path: Full file path
            algorithm: Algorithm type. MD5, SHA1(256, 384, 512), RIPEMD160

        Returns:
            File's hash. D36C604229BBD19FC59F64ACB342493F
        """

        cmd = f'(Get-FileHash -Path "{path}" -Algorithm {algorithm}).Hash'
        try:
            result = self.run_ps(cmd)
        except RemoteCommandExecutionError:
            self.logger.error(f'File ({path}) not found.')
            raise FileNotFoundError(path)

        return result.stdout

    def get_xml(self, file_name: str, xml_attrs: bool = False) -> dict:
        """Parse specified xml file's content

        Args:
            file_name: XML file path
            xml_attrs: Get XML attributes
        """

        self.logger.info(f'{self.host:<14} | Getting "{file_name}" as dictionary')

        try:
            xml = self.get_content(file_name)
            xml_data = xmltodict.parse(xml, xml_attribs=xml_attrs)
        except TypeError as err:
            self.logger.error(f'{self.host:<14} | File ({file_name}) not found.')
            raise err
        else:
            result = json.loads(json.dumps(xml_data))
            self.logger.info(f'{self.host:<14} | {result}')
            return result

    def copy_item(self, src: str, dst: str) -> bool:
        r"""Copy file on remote server.

        - Copy-Item -Path "{source}" -Destination "{dst_full}" -Recurse -Force

        https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.management/copy-item?view=powershell-7.2

        Usage:
            Copy to dir:
                - .copy_item(r'D:\\Install\build_log_20220501_050045.txt', r'x:\\1')

            Copy and rename
                - .copy_item(r'D:\\Install\\build_log_20220501_050045.txt', r'x:\\1\\renamed.txt')

            Copy all files
                - .copy_item(r'D:\\Install\\*', r'x:\\1')

        Args:
            src: Source path to copy. d:\zen.txt, d:\dir\*
            dst: Destination root directory. e:, e:\dir1
        """

        cmd = f'Copy-Item -Path "{src}" -Destination "{dst}" -Recurse -Force'
        result = self.run_ps(cmd)
        return result.ok

    def move_item(self, src: str, dst: str) -> bool:
        r"""Move file on remote server.

        - Move-Item -Path "{source}" -Destination "{dst_full}" -Force

        https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.management/move-item?view=powershell-7.2

        Args:
            src: Source path to copy. d:\zen.txt, d:\dir
            dst: Destination root directory. e:\zen.txt, e:\dir1
        """

        cmd = f'Move-Item -Path "{src}" -Destination "{dst}" -Force'
        result = self.run_ps(cmd)
        return result.ok

    def create_directory(self, path: str) -> bool:
        """Create directory on remote server. Directories will be created recursively.

        - New-Item -Path "{path}" -ItemType Directory -Force | Out-Null

        >>> self.create_directory(r'e:\1\2\3')

        Args:
            path:
        :return:
        """

        cmd = fr'New-Item -Path "{path}" -ItemType Directory -Force | Out-Null'
        result = self.run_ps(cmd)
        return result.ok

    def unzip(self, path: str, target_directory: str) -> bool:
        r"""Extract .zip archive to destination folder on remote server.

        - Expand-Archive -Path "{path}" -DestinationPath "{target_directory}"

        Creates destination folder if it does not exist

        Args:
            path: C:\Archives\Draft[v1].Zip
            target_directory: C:\Reference
        """

        cmd = f'Expand-Archive -Path "{path}" -DestinationPath "{target_directory}"'
        result = self.run_ps(cmd)
        return result.ok

    # ---------- Service / process management ----------
    def get_service(self, name: str) -> dict:
        """Get Windows service detailed info

        - Get-Service -Name "{name}"

        Args:
            name: Service name
        """

        cmd = f'Get-Service -Name "{name}" | ConvertTo-Json -Depth 1'
        try:
            result = self.run_ps(cmd)
        except RemoteCommandExecutionError as err:
            if f"Cannot find any service with service name '{name}'" in err.error:
                self.logger.error(f'Service ({name}) not found!')
                raise ServiceLookupError(name)
            raise err
        return result.stdout

    def is_service_running(self, name: str) -> bool:
        """Verify local Windows service is running

        - Get-Service -Name "{name}"

        Status:
            - Stopped 1
            - StartPending 2
            - StopPending 3
            - Running 4
            - PausePending 6
            - ContinuePending 5
            - Paused 7

        Args:
            name: Service name
        """

        result = self.get_service(name)
        status = result.get('Status')
        return status == 4

    def start_service(self, name: str) -> bool:
        """Start service

        - Start-Service -Name {name}

        Args:
            name: Service name
        """

        cmd = f'Start-Service -Name "{name}"'
        result = self.run_ps(cmd)
        return result.ok

    def restart_service(self, name: str) -> bool:
        """Restart service

        - Restart-Service -Name {name}

        Args:
            name: Service name
        """

        cmd = f'Restart-Service -Name "{name}"'
        result = self.run_ps(cmd)
        return result.ok

    def stop_service(self, name: str, force: bool = False) -> bool:
        """Stop service

        - Stop-Service -Name {name}

        Args:
            name: Service name
            force: False
        """

        cmd = f'Stop-Service -Name {name}'
        if force:
            cmd += ' -Force'

        result = self.run_ps(cmd)
        return result.ok

    def wait_service_start(self, name: str, timeout: int = 30, interval: int = 3) -> bool:
        """Wait for service start specific time

        - Get-Service -Name {name}

        Args:
            name: Service name
            timeout: Timeout in sec
            interval: How often check service status
        """

        cmd = f"""
        if (!(Get-Service -Name {name} -ErrorAction SilentlyContinue)){{
            throw "Service [{name}] not found!"
        }}

        $timeout = {timeout}
        $timer = 0
        While ((Get-Service -Name {name}).Status -ne "Running"){{
            Start-Sleep {interval}
            $timer += {interval}
            if ($timer -gt $timeout){{
                throw "The service [{name}] was not started within {timeout} seconds."
            }}
        }}
        """

        result = self.run_ps(cmd)
        return result.ok

    def get_process(self, name: str, ignore_error: bool = False) -> dict:
        """Get Windows process detailed info

        - Get-Process -Name {name}

        Args:
            name: Process name without extension. svchost, alg
            ignore_error: Suppress error if occurs
        """

        cmd = f'Get-Process -Name {name} -ErrorAction SilentlyContinue | ConvertTo-Json -Depth 1'
        if not ignore_error:
            cmd = cmd.replace(' -ErrorAction SilentlyContinue', '')

        result = self.run_ps(cmd)
        result = self._convert_result(result, key='Id')

        return result

    def start_process(self, path: str, timeout: int = 2) -> bool:
        """Start process

        - Start-Process -FilePath "{path};Start-Sleep 2"

        Args:
            path: Executable path
            timeout: Wait for process starts completely
        """

        cmd = f'Start-Process -FilePath "{path}"'
        if timeout:
            cmd += f';Start-Sleep {timeout}'
        result = self.run_ps(cmd)
        return result.ok

    def kill_process(self, name: str) -> bool:
        """Kill Windows service

        - taskkill -im {name} /f

        Args:
            name: Process name
        """

        result = self.run_cmd(f'taskkill -im {name} /f')
        return result.ok

    def stop_process(self, name: str, ignore_error: bool = False) -> bool:
        """Stop Windows service

        - Stop-Process -Name {name} -Force -ErrorAction SilentlyContinue

        Args:
            name: Process name
            ignore_error: Suppress error if occurs
        """

        cmd = f'Stop-Process -Name {name} -Force'
        if ignore_error:
            cmd += ' -ErrorAction SilentlyContinue'
        result = self.run_ps(cmd)
        return result.ok

    def is_process_running(self, name: str) -> bool:
        """Verify process is running

        - Get-Process -Name {name}

        Args:
            name: Process name without extension. svchost, alg
        """

        result = self.get_process(name, ignore_error=True)
        return True if result else False

    # ------------------ Networking ----------------------
    def get_net_adapter(self, name: str = None) -> dict:
        """Get network adapter info

        - Get-NetAdapter | ConvertTo-Json

        Args:
            name: Network adapter name. Ethernet0, SYNC, DATA
        """

        cmd = 'Get-NetAdapter | ConvertTo-Json -Depth 1'
        response = self.run_ps(cmd)
        result = self._convert_result(response)

        return result if name is None else result.get(name)

    def disable_net_adapter(self, name: str) -> bool:
        """Disable network adapter in Windows by its name

        - Disable-NetAdapter -Name "{name}" -Confirm:$false

        Log info is adapter already disabled and return

        Args:
            name: DATA, SYNC
        """

        cmd = f'Disable-NetAdapter -Name "{name}" -Confirm:$false'
        result = self.run_ps(cmd)
        return result.ok

    def enable_net_adapter(self, name: str) -> bool:
        """Enable network adapter in Windows by its name

        - Enable-NetAdapter

        Log info is adapter already disabled and return

        Args:
            name: DATA, SYNC
        """

        cmd = f'Enable-NetAdapter -Name "{name}" -Confirm:$false'
        result = self.run_ps(cmd)
        return result.ok

    # ------------------- DISK --------------------
    def set_disk_state(self, disk_number: int, enabled: bool) -> bool:
        """Set underline disk state.

        - Set-Disk -Number {disk_number} -IsOffline $

        Args:
            enabled: True | False
            disk_number: 1 | 2 | 3

        Returns:
            Bool after successful execution.
        """

        cmd = f'Set-Disk -Number {disk_number} -IsOffline ${not enabled}'
        result = self.run_ps(cmd)
        return result.ok

    def get_disk(self, disk_number: int = None) -> dict:
        """Get Disks info.

        - Get-Disk

        Key in dict - disk number, int. Additional key - 'entities_quantity', int.

        - if disk_number is None, return all disks info
        - if disk_number is not None, return specific disk info

        :param disk_number: Disk disk_number. 1, 2, 3...
        """

        disks = self.run_ps('Get-Disk | ConvertTo-Json -Depth 1').stdout

        result = {
            int(disk['DiskNumber']): {
                'DiskNumber': disk['DiskNumber'],
                'NumberOfPartitions': disk['NumberOfPartitions'],
                'PartitionStyle': disk['PartitionStyle'],
                'ProvisioningType': disk['ProvisioningType'],
                'OperationalStatus': disk['OperationalStatus'],
                'HealthStatus': disk['HealthStatus'],
                'BusType': disk['BusType'],
                'SerialNumber': disk['SerialNumber'],
                'AllocatedSize': disk['AllocatedSize'],
                'BootFromDisk': disk['BootFromDisk'],
                'IsBoot': disk['IsBoot'],
                'IsClustered': disk['IsClustered'],
                'IsOffline': disk['IsOffline'],
                'IsReadOnly': disk['IsReadOnly'],
                'Location': disk['Location'],
                'LogicalSectorSize': disk['LogicalSectorSize'],
                'PhysicalSectorSize': disk['PhysicalSectorSize'],
                'Manufacturer': disk['Manufacturer'],
                'Model': disk['Model'],
                'Size': disk['Size'],

            } for disk in disks}

        # noinspection PyTypeChecker
        result['entities_quantity'] = len(result)
        return result.get(disk_number) if disk_number else result

    def get_volume(self, letter: str = None) -> dict:
        """Get virtual volumes info.

        - Get-Volume

        Key in dict - volume letter (disk name).
        "entities_quantity" - auxiliary key is added. Number of entities in volume.
        Empty values replaced by None.

        - If letter is specified, only one volume info will be returned.
        - If letter is not specified, all volumes info will be returned.
        - If volume without letter found, it will be named <SystemN>, where N - number of volume.

        Args:
            letter: Volume letter. C, D, E...

        Returns:
            {
                'W': {'DriveLetter': 'W', 'FileSystemLabel': None, 'Size': 0, 'SizeRemaining': 0, 'SizeUsed': 0...}
        """

        vol_name = letter.removesuffix('\\').removesuffix(':') if letter else letter
        volumes = self.run_ps('Get-Volume | ConvertTo-Json -Depth 1').stdout

        volumes_dict = {}
        for n, vol in enumerate(volumes):
            volume_letter = vol['DriveLetter']
            key = volume_letter if volume_letter is not None else f'System{n}'

            volumes_dict[key] = {
                'DriveLetter': vol['DriveLetter'],
                'FileSystemLabel': vol['FileSystemLabel'] if vol['FileSystemLabel'] else None,
                'Size': vol['Size'],
                'SizeRemaining': vol['SizeRemaining'],
                'SizeUsed': vol['Size'] - vol['SizeRemaining'],
                'HealthStatus': vol['HealthStatus'],
                'DriveType': vol['DriveType'],
                'FileSystem': vol['FileSystem'] if vol['FileSystem'] else None,
                'DedupMode': vol['DedupMode'],
                'AllocationUnitSize': vol['AllocationUnitSize'],
                'OperationalStatus': vol['OperationalStatus'],
                'UniqueId': vol['UniqueId'],
            }

        volumes_dict['entities_quantity'] = len(volumes)

        return volumes_dict.get(vol_name) if vol_name else volumes_dict

    # ------------------- Auxiliary methods -------------------------
    @staticmethod
    def _convert_result(response: WinResponse, key: str = 'Name') -> dict:
        """Convert list/dict response into named dict.

        Args:
            response: Raw Response from WinRM
            key: Key name to be root
        """

        stdout = response.stdout

        match stdout:
            case list():
                entity = {i[key]: i for i in stdout}
                entity['entities'] = [*entity]
                entity['entities_quantity'] = len(entity['entities'])
            case dict():  # Only 1 object exists
                entity = stdout
                entity['entities'] = [entity.get(key)]
                entity['entities_quantity'] = 1
            case _:
                entity = {'entities': [], 'entities_quantity': 0}

        return entity
