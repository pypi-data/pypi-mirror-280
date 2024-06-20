import os

import pytest


@pytest.mark.skipif(os.name == 'nt', reason='Cannot be verified on windows')
def test_exists_true(client_local):
    assert client_local.exists_local('/root')


def test_exists_false(client_local):
    assert not client_local.exists_local('/root1')
