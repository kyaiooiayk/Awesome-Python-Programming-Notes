# Pytest
***

## Installation
- `pip install pytest`
- `pytest --version`
***

## Usage
- Pytest will execute all the python files that have the name test_ prepended or _test appended to the name of the script.
- Simply type `pytest` in the directory where the tests are located.

## `@pytest.fixture`
- Fixtures can be used for both setting up and tearing down resources, as well as for grouping shared pieces of code. They provide a way to encapsulate common setup and teardown logic, making tests cleaner and more maintainable. Additionally, fixtures can help in reducing code duplication by allowing shared code to be defined once and reused across multiple tests.
```python
# test_no_fixiture.py

import pytest

class Database:
    def __init__(self):
        self.connected = False

    def connect(self):
        # Simulate connecting to a database
        self.connected = True

    def disconnect(self):
        # Simulate disconnecting from a database
        self.connected = False

def test_database_connection():
    # Set up the database connection
    db = Database()
    db.connect()

    # Ensure that the database is connected
    assert db.connected == True

    # Tear down the database connection
    db.disconnect()

def test_database_disconnection():
    # Set up the database connection
    db = Database()
    db.connect()

    # Ensure that the database is connected
    assert db.connected == True

    # Disconnect from the database
    db.disconnect()

    # Ensure that the database is disconnected
    assert db.connected == False

```

```python
# test_with_fixiture.py

import pytest

class Database:
    def __init__(self):
        self.connected = False

    def connect(self):
        # Simulate connecting to a database
        self.connected = True

    def disconnect(self):
        # Simulate disconnecting from a database
        self.connected = False

@pytest.fixture
def database():
    # Set up the database connection
    db = Database()
    db.connect()
    return db  # Provide the fixture object to the test
    # Tear down the database connection
    #db.disconnect()

def test_database_connection(database):
    # Ensure that the database is connected
    assert database.connected == True

def test_database_disconnection(database):
    # Disconnect from the database
    database.disconnect()

    # Ensure that the database is disconnected
    assert database.connected == False

```
***

## `@pytest.parametrize`
- Consider the scenario where we have 4 different but very similar tests. There is quite a lot of boiler plate going on.
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

## `@pytest.mark`
- Markers allow you to group tests and selectively run them as `pytest -m slow`.
```python
@pytest.mark.slow
def test_slow_function():
    import time
    time.sleep(5)
    assert True
```
***

## `@pytest.fixture(scope="")`
- function: The default scope. The fixture is setup/teardown for each test function.
- class: The fixture is setup/teardown once per test class.
- module: The fixture is setup/teardown once per module.
- session: The fixture is setup/teardown once per session (typically the entire test run).
***

## References
- [How to Use Pytest for Unit Testing](https://www.datacamp.com/tutorial/pytest-tutorial-a-hands-on-guide-to-unit-testing)
- [How to use fixtures](https://docs.pytest.org/en/7.1.x/how-to/fixtures.html)
***
