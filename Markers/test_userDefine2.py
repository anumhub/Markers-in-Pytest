import pytest

@pytest.mark.smoke
def test_sample_five():
    print("Inside sample 5")


"""
To overcome warning in user define marker :
PytestUnknownMarkWarning: Unknown pytest.mark.regression - is this a typo?
You can register custom marks to avoid this warning -
for details, see https://docs.pytest.org/en/stable/how-to/mark.html

solution is :
create a custom marker in pytest.ini  under folder pytest
"""