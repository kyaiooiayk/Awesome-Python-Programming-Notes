# Pytest
***

## Installation
- `pip install pytest`
- `pytest --version`
***

## Usage
- Pytest will execute all the python files that have the name test_ prepended or _test appended to the name of the script.
- Simply type `pytest` in the directory where the tests are located.

### Pytest fixiture
```python
import pytest


class Fruit:
    def __init__(self, name):
        self.name = name
        self.cubed = False

    def cube(self):
        self.cubed = True


class FruitSalad:
    def __init__(self, *fruit_bowl):
        self.fruit = fruit_bowl
        self._cube_fruit()

    def _cube_fruit(self):
        for fruit in self.fruit:
            fruit.cube()


# Arrange
@pytest.fixture
def fruit_bowl():
    return [Fruit("apple"), Fruit("banana")]


def test_fruit_salad(fruit_bowl):
    # Act
    fruit_salad = FruitSalad(*fruit_bowl)

    # Assert
    assert all(fruit.cubed for fruit in fruit_salad.fruit)
```
- In this example, test_fruit_salad “requests” fruit_bowl (i.e. def test_fruit_salad(fruit_bowl):), and when pytest sees this, it will execute the fruit_bowl fixture function and pass the object it returns into test_fruit_salad as the fruit_bowl argument.
***

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
- [How to use fixtures](https://docs.pytest.org/en/7.1.x/how-to/fixtures.html)
***
