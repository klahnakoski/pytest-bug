import os
import pytest
import shutil
import tempfile


@pytest.yield_fixture()
def tempdir():
    d = tempfile.mkdtemp()
    yield d
    if os.path.exists(d):
        shutil.rmtree(d, ignore_errors=True)


@pytest.mark.parametrize('tempdir', [(tempdir,)])
def test_yield_fixture(tempdir):
    assert isinstance(tempdir, basestring)
