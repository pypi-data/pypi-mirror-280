import os


def test_get_current_os_name(client_local):
    response = client_local.get_current_os_name_local()
    print(response)
    print(os.name)

    if os.name == 'nt':
        assert 'Windows' in response, 'Current OS name is not Windows'
    elif os.name == 'Linux':
        assert 'Linux' in response, 'Current OS name is not Linux'
    elif os.name == 'posix':
        assert response == 'Darwin', 'Current OS name is not MacOS'
