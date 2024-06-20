import os

import pytest


@pytest.mark.skipif(os.name == 'nt', reason='Cannot be verified on windows')
def test_search_windows(client_local):
    result = client_local.get_dirs_files('/etc')
    # result = client_local.search('c:\\windows', filter_='fes')
    # result = client_local.search('c:\\windows', starts='Pro')
    # result = client_local.search('c:\\windows', ends='exe')
    assert result, 'Files not found'
