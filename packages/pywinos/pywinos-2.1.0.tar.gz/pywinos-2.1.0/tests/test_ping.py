import os

import pytest

from pywinos import WinOSClient


@pytest.mark.skipif(os.name != 'nt', reason='Cannot be verified on windows')
def test_ping_remote_host_with_no_ip_in_method():
    tool = WinOSClient(host='8.8.8.8')
    response = tool.ping()
    print(response)
    assert not response.exited, 'Exit code is not 0'


def test_ping_remote_host_with_no_ip_in_class():
    tool = WinOSClient()
    response = tool.ping(host='8.8.8.8')
    assert not response.exited, 'Exit code is not 0'


def test_ping_no_ip():
    tool = WinOSClient(host='')
    response = tool.ping()

    if os.name == 'nt':
        assert response.stdout == 'IP address must be specified.', \
            'IP address must be specified.'
    else:
        assert 'Usage: ping' in response.stderr


@pytest.mark.parametrize('number', [1, 2, 4])
def test_ping_packets_number(number):
    tool = WinOSClient(host='8.8.8.8')
    response = tool.ping(packets_number=number)
    assert number == response.stdout.count('from 8.8.8.8')
