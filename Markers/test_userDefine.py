import pytest

@pytest.mark.smoke
def test_sample_one():
    print("Inside sample 1")

@pytest.mark.regression
def test_sample_two():
    print("Inside sample 2")

@pytest.mark.regression
def test_sample_three():
    print("Inside sample 3")

"""
run in terminal:

pytest -rA -m smoke
pytest -rA -m regression
pytest -rA -m "smoke or regression"
pytest -rA -m "smoke and not regression"

"""