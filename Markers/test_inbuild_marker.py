import pytest

@pytest.mark.smoke
def test_login():
    print("welcome to login page")

@pytest.mark.xfail
def test_sample_addition():
    assert 2+3 == 6

@pytest.mark.xfail
def test_expectedpass():
    print("Expected PASS")

"""
OUTPUT - command line - pytest Markers/test_inbuild_marker.py

(.venv) anumsharma@Anum-MacBook- Pytest % pytest Markers/test_inbuild_marker.py
================================================================== test session starts ===================================================================
platform darwin -- Python 3.13.1, pytest-8.4.1, pluggy-1.6.0
rootdir: /Users/anumsharma/code/Pytest
configfile: pytest.ini
collected 3 items                                                                                                                                        

Markers/test_inbuild_marker.py .xX                                                                                                                 [100%]

======================================================== 1 passed, 1 xfailed, 1 xpassed in 0.04s =========================================================
"""