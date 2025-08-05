import pytest

@pytest.mark.skip(reason="function not develop")
def test_sample_newfeature():
    print("New feature for application")

@pytest.mark.regression
def test_sample_newfeature2():
    print("New feature 2 for application")

"""
run in terminal:

anumsharma@Anum-MacBook Pytest % pytest Markers/test_skip_marker.py

output:

platform darwin -- Python 3.13.1, pytest-8.4.1, pluggy-1.6.0
rootdir: /Users/anumsharma/code/Pytest
configfile: pytest.ini
collected 2 items                                                                                                                                        

Markers/test_skip_marker.py s.                                                                                                                     [100%]

============================================================== 1 passed, 1 skipped in 0.01s ==============================================================

"""
