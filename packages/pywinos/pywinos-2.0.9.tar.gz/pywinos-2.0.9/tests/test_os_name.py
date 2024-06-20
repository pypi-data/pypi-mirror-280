import os

import pytest


@pytest.mark.skipif(os.name != 'nt', reason='Cannot be verified on windows')
def test_os_name(client_local):
    assert 'Windows' in client_local.get_os_name_local(), 'response is not Windows'
