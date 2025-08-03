# Markers-in-Pytest

This repository shows how to use different Pytest markers with simple examples:
- `@pytest.mark.skip`
- `@pytest.mark.skipif`
- `@pytest.mark.parametrize`
- Custom markers (like `@pytest.mark.smoke`)
- Grouping tests with markers

Running Examples:
- Run all tests:
pytest -v
- Run only smoke tests:
pytest -m smoke

