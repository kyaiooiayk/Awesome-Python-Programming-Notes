# Pytest
***

## Installation
- `pip install pytest`
- `pytest --version`
***

## Usage
- Pytest will execute all the python files that have the name test_ prepended or _test appended to the name of the script.
- Simply type `pytest` in the directory where the tests are located.

### Pytest parametrize
- Consider the scenario where we have 4 different but very similar test. There is quite a lot of boiler plate going on.
```python
def test_eval_addition():
    assert eval("2 + 2") == 4

def test_eval_subtraction():
    assert eval("2 - 2") == 0

def test_eval_multiplication():
    assert eval("2 * 2") == 4

def test_eval_division():
    assert eval("2 / 2") == 1.0
```
- Pytest offers a solution here called `pytest.mark.parametrize()`
```python
import pytest

@pytest.mark.parametrize("test_input, expected_output", [("2+2", 4), ("2-2", 0), ("2*2", 4), ("2/2", 1.0)])
def test_eval(test_input, expected_output):
    assert eval(test_input) == expected_output
```
***

## References
- [How to Use Pytest for Unit Testing](https://www.datacamp.com/tutorial/pytest-tutorial-a-hands-on-guide-to-unit-testing)
***
