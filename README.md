# pytest-bug
example pytest bug


We would expect the fixture to yield the tempdir name, not a function

```
C:\Users\kyle\code\pytest-bug>py.test tests
============================= test session starts =============================
platform win32 -- Python 2.7.14, pytest-3.3.2, py-1.5.2, pluggy-0.6.0
rootdir: C:\Users\kyle\code\pytest-bug, inifile:
collected 1 item

tests\test_yield_fixture.py F                                            [100%]

================================== FAILURES ===================================
________________________ test_yield_fixture[tempdir0] _________________________

tempdir = (<function tempdir at 0x037031B0>,)

    @pytest.mark.parametrize('tempdir', [(tempdir,)])
    def test_yield_fixture(tempdir):
>       assert isinstance(tempdir, basestring)
E       assert False
E        +  where False = isinstance((<function tempdir at 0x037031B0>,), basestring)

tests\test_yield_fixture.py:17: AssertionError
========================== 1 failed in 0.05 seconds ===========================
```
