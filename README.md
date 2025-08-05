# Markers-in-Pytest

This repository shows how to use different Pytest markers with simple examples:
- `@pytest.mark.skip`
- `@pytest.mark.parametrize`
- Custom markers - make a pytest.ini file AND  mention all the user define markers to avoid warning in output
- Inbuild Markers (like `@pytest.mark.xfail`)
- User Define Markers (like `@pytest.mark.smoke`)

Running Examples:
- Run all tests ( make sure that user should be in root directory of his/her project):
pytest -v
- Run only smoke tests:
pytest -rA -m smoke
- Run only regression tests:
pytest -rA -m regression
- Run only smoke and regression tests:
pytest -rA -m "smoke or regression"
- Run only smoke tests but not regtession:
pytest -rA -m "smoke and not regression"
- Run only parametrize tests:
Terminal- anumsharma@Anum-MacBook Pytest % pytest Markers/test_parametrize_marker.py -v -rA
pytest is the project name 
Markers is folder name
test_parametrize_marker.py is filename
-Run only inbuild tests:
Terminal- pytest Markers/test_inbuild_marker.py
- Run only skip tests:
Terminal- pytest Markers/test_skip_marker.py

