# Pytest
***

## Installation
- `pip install pytest`
- `pytest --version`
***

## Usage
- Pytest will execute all the python files that have the name test_ prepended or _test appended to the name of the script.
- Simply type `pytest` in the directory where the tests are located.
- You can run all test in paralle with `pytest-xdist`. Instal it with `pip install pytest-xdist` and run it as `pytest -n 4`.
- If you are using mocking make sure you have it installed: `pip install pytest-mock`.
- To have a nice report, install `pip install pytest-html` and then run `pytest --html=report.html`
***

## `conftest.py`
- This file helps maintain cleaner and more maintainable test code by centralizing common setup, configuration, and customization logic.
***

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
- Here's an example that demonstrates the number of setups and teardowns executed using different fixture scopes (function, class, module, and session). We'll use a counter to track the number of times the setup and teardown functions are called.
```python
# test_scopes.py
import pytest

setup_counter = {
    'function': 0,
    'class': 0,
    'module': 0,
    'session': 0
}

teardown_counter = {
    'function': 0,
    'class': 0,
    'module': 0,
    'session': 0
}

class Database:
    def __init__(self):
        self.connected = False

    def connect(self):
        self.connected = True

    def disconnect(self):
        self.connected = False

# Fixture with function scope
@pytest.fixture(scope="function")
def db_function():
    setup_counter['function'] += 1
    db = Database()
    db.connect()
    yield db
    db.disconnect()
    teardown_counter['function'] += 1

# Fixture with class scope
@pytest.fixture(scope="class")
def db_class():
    setup_counter['class'] += 1
    db = Database()
    db.connect()
    yield db
    db.disconnect()
    teardown_counter['class'] += 1

# Fixture with module scope
@pytest.fixture(scope="module")
def db_module():
    setup_counter['module'] += 1
    db = Database()
    db.connect()
    yield db
    db.disconnect()
    teardown_counter['module'] += 1

# Fixture with session scope
@pytest.fixture(scope="session")
def db_session():
    setup_counter['session'] += 1
    db = Database()
    db.connect()
    yield db
    db.disconnect()
    teardown_counter['session'] += 1

# Tests using function scope
def test_function_scope_1(db_function):
    assert db_function.connected

def test_function_scope_2(db_function):
    assert db_function.connected

# Tests using class scope
class TestClassScope:
    def test_class_scope_1(self, db_class):
        assert db_class.connected

    def test_class_scope_2(self, db_class):
        assert db_class.connected

# Tests using module scope
def test_module_scope_1(db_module):
    assert db_module.connected

def test_module_scope_2(db_module):
    assert db_module.connected

# Tests using session scope
def test_session_scope_1(db_session):
    assert db_session.connected

def test_session_scope_2(db_session):
    assert db_session.connected

# Print setup and teardown counters
def test_print_counters():
    print("\nSetup Counters:", setup_counter)
    print("Teardown Counters:", teardown_counter)
```
- Which should give you this output:
```bash
Setup Counters: {'function': 2, 'class': 1, 'module': 1, 'session': 1}
Teardown Counters: {'function': 2, 'class': 1, 'module': 1, 'session': 1}

```
***

## Mocking
- `MagicMock` is not directly used in this specific example, but pytest-mock uses the mock library under the hood.
```python
# test_mocking.py
from unittest.mock import MagicMock
import pytest

class Database:
    def connect(self):
        # Simulate a real database connection
        return "Connected"

def test_mocking(mocker):
    db = Database()
    mocker.patch.object(db, 'connect', return_value=True)
    
    # The connect method is now mocked and will return True
    assert db.connect() == True

```
***

## `@pytest.mark.skip` 
```python
@pytest.mark.skip(reason="Skipping this test for now")
def test_to_skip():
    assert False
```
***

## `@pytest.mark`
```python
@pytest.mark.xfail(reason="This test is expected to fail")
def test_expected_to_fail():
    assert False
```
***

## `conftest.py`

***

## References
- [How to Use Pytest for Unit Testing](https://www.datacamp.com/tutorial/pytest-tutorial-a-hands-on-guide-to-unit-testing)
- [How to use fixtures](https://docs.pytest.org/en/7.1.x/how-to/fixtures.html)
***
