import os

import pytest

from pywinos import WinOSClient


@pytest.mark.parametrize('command', ['whoami', 'hostname', 'arp -a'])
def test_run_cmd_local(command):
    tool = WinOSClient(host='')
    response = tool.run_cmd_local(cmd=command)
    assert response.ok, 'Response is not OK'


def test_run_cmd_invalid_command():
    tool = WinOSClient(host='')
    response = tool.run_cmd_local('whoamia')
    assert not response.ok, 'Response is OK. Must be False'
    assert not response.stdout, 'STDOUT is not empty. Must be empty'

    if os.name == 'nt':
        assert 'is not recognized as an internal' in response.stderr, \
            'Response is OK. Must be False'
    else:
        assert 'whoamia: not found' in response.stderr


def test_list_all_methods(client_local):
    response = client_local.list_all_methods()
    assert isinstance(response, list)
    assert 'run_cmd' in response
    assert 'run_ps' in response


def test_run_local(client_local):
    response = client_local._run_local('hostname')
    assert not response.exited, 'Exit code not equal 0'
