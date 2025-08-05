# passing 10 set of data - it will run 10 times
# data driven format
import pytest

@pytest.mark.parametrize("username,password",[("anu","1234"),("ajay","1555"),("jane","3377")])
def test_sample_data(username,password):
    print(username +"-"+password)

"""
OUTPUT-  command used- pytest Markers/test_parametrize_marker.py -v -rA

(.venv) anumsharma@Anum-MacBook-Pro Pytest % pytest Markers/test_parametrize_marker.py -v
================================================================== test session starts ===================================================================
platform darwin -- Python 3.13.1, pytest-8.4.1, pluggy-1.6.0 -- /Users/anumsharma/code/Pytest/.venv/bin/python
cachedir: .pytest_cache
rootdir: /Users/anumsharma/code/Pytest
configfile: pytest.ini
collected 3 items                                                                                                                                        

Markers/test_parametrize_marker.py::test_sample_data[anu-1234] PASSED                                                                              [ 33%]
Markers/test_parametrize_marker.py::test_sample_data[ajay-1555] PASSED                                                                             [ 66%]
Markers/test_parametrize_marker.py::test_sample_data[jane-3377] PASSED                                                                             [100%]

=================================================================== 3 passed in 0.01s ====================================================================
"""