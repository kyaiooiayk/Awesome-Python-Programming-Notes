# How to test your Python code
***

## Testing your code
- **TDD** (Test Driven Development) is a way of code development where the developer first writes the test and after that the function.
- **BDD** (Behaviour-Driven Development) combines the general techniques and principles of TDD with ideas from domain-driven design and object-oriented analysis and design to provide software development and management teams with shared tools and a shared process to collaborate on software development.
***

## Type of testing

For simplicity, let's assume we're working on a simple web application with Flask. The application will have a basic functionality: creating, retrieving, and deleting items from a list.
```MD
myapp/
├── app.py
├── requirements.txt
├── tests/
│   ├── __init__.py
│   ├── test_unit.py
│   ├── test_integration.py
│   ├── test_e2e.py
│   ├── test_acceptance.py
│   ├── test_functional.py
│   ├── test_smoke.py
│   ├── test_performance.py
│   ├── test_security.py
│   ├── test_documentation.py
└── conftest.py

```
Consider the following app.py. This where the main code/logic goes.

```python
from flask import Flask, request, jsonify, Response
from typing import List

app = Flask(__name__)

items: List[str] = []

@app.route('/items', methods=['POST'])
def create_item() -> Response:
    item: str = request.json.get('item', '')
    if item:
        items.append(item)
        return jsonify({'message': 'Item added', 'items': items}), 201
    return jsonify({'message': 'Item is required'}), 400

@app.route('/items', methods=['GET'])
def get_items() -> Response:
    return jsonify({'items': items}), 200

@app.route('/items/<string:item>', methods=['DELETE'])
def delete_item(item: str) -> Response:
    if item in items:
        items.remove(item)
        return jsonify({'message': 'Item deleted', 'items': items}), 200
    return jsonify({'message': 'Item not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
```
`conftest.py` is a special configuration file used by pytest to define fixtures and hooks that can be shared across multiple test modules. It's automatically discovered by pytest and allows you to create reusable setup and teardown code, which can be used across different test files without the need for importing them explicitly.
```python
import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

@pytest.fixture(autouse=True)
def clear_items():
    from app import items
    items.clear()

```

**Unit Tests**
- **Purpose**: Verify the functionality of individual components or functions in isolation.
- **Example**: Test if an item can be added to a list.
```python
# tests/test_unit.py
def test_create_item(client):
    response = client.post('/items', json={'item': 'item1'})
    assert response.status_code == 201
    assert 'item1' in response.json['items']

def test_get_items(client):
    response = client.post('/items', json={'item': 'item1'})
    response = client.get('/items')
    assert response.status_code == 200
    assert 'item1' in response.json['items']

def test_delete_item(client):
    response = client.post('/items', json={'item': 'item1'})
    response = client.delete('/items/item1')
    assert response.status_code == 200
    assert 'item1' not in response.json['items']

def test_create_item_without_item(client):
    response = client.post('/items', json={})
    assert response.status_code == 400

```

**Integration Tests**
- **Purpose**: Ensure that different components of the system work together correctly.
- **Example**: Test the interaction between the item creation and retrieval endpoints.

**End-to-End (E2E) Tests**
- **Purpose**: Validate the complete flow of the application from the user's perspective.
- **Example**: Test adding an item, retrieving it, and then deleting it via HTTP requests.

**Acceptance Tests**
- **Purpose**: Confirm the application meets business requirements and user expectations.
- **Example**: Test the lifecycle of an item (creation, retrieval, deletion) as expected by stakeholders.

**Functional Tests**
- **Purpose**: Check specific functionalities of the application in a realistic environment.
- **Example**: Test item creation and deletion functionalities together.

**Smoke Tests**
- **Purpose**: Perform a quick check to ensure the basic functionalities of the application work.
- **Example**: Test if the main endpoints are up and responding correctly.

**Performance Tests**
- **Purpose**: Measure the responsiveness and stability of the application under load.
- **Example**: Ensure the items retrieval endpoint responds within a specified time.

**Security Tests**
- **Purpose**: Identify vulnerabilities and ensure the application is secure.
- **Example**: Test for SQL injection vulnerabilities in the item creation endpoint.

**Usability Tests**
- **Purpose**: Assess the application's user-friendliness and overall user experience.
- **Example**: Collect feedback from users interacting with the application.

**Compatibility Tests**
- **Purpose**: Ensure the application works across different environments, devices, and browsers.
- **Example**: Verify the homepage loads correctly on different web browsers.

**Documentation Tests**
- **Purpose**: Ensure that the documentation is accurate, complete, and useful.
- **Example**: Check the existence and content of the README file for installation and usage instructions.
***

## Python testing framework
- [Unittest](https://docs.python.org/3/library/unittest.html) is a built-in Python framework for unit testing. It was inspired by a unit testing framework called JUnit from the Java programming language. Since it comes out of the box with the Python language, there are no extra modules to install, and most developers use it to begin learning about testing.
- [Pytest](https://docs.pytest.org/en/7.3.x/) is possibly the most widely used Python testing framework around - this means it has a large community to support you whenever you get stuck. It’s an open-source framework that enables developers to write simple, compact test suites while supporting unit testing, functional testing, and API testing.
doctest
- [doctest](https://docs.python.org/3/library/doctest.html) merges two core components of software engineering: documentation and testing. This functionality ensures that all software programs are thoroughly documented and tested to ensure they run as they should. doctest comes with Python’s standard library and is pretty straightforward to learn.
- [Nose2](https://docs.nose2.io/en/latest/), the successor to the nose regiment,  is essentially unittest with plugins. People often refer to nose2 as “extended unit tests” or “unit tests with a plugin” due to its close ties to the Python built-in unit testing framework. Since it’s practically an extension of the unittest framework, nose2 is incredibly easy to adopt for those familiar with unittest.
- [Testify](https://github.com/Yelp/Testify), a Python framework for unit, integration, and system testing, is popularly known as the framework that was designed to replace unittest and nose. The framework is packed with extensive plugins and has quite a smooth learning curve if you’re already familiar with unittest.
- [Hypothesis](https://hypothesis.readthedocs.io/en/latest/) enables developers to create unit tests that are simpler to write and are powerful when run. Since the framework is built to support data science projects, it helps to find edge cases that aren’t so apparent while you’re creating your tests by generating examples of inputs that align with specific properties you define.
***


## What is the Arrange, Act and Assert Pattern?
- The Arrange, Act and Assert Pattern is a way of structuring unit tests so that they are easy to read and understand. This pattern is also known as the Given, When, Then pattern.
    - **Arrange**: Set up the conditions for your test. This might involve creating objects, setting up variables or anything else that’s required for your test.
    - **Act**: This is where you actually execute the code that you are testing.
    - **Assert**: Verify that the code you’re testing behaves as expected. This might involve checking the value of a variable, or verifying that a certain method was called.
```python
# test_calculator.py

import pytest
from calculator import add

def test_add():
    # Given: two numbers, a and b
    a = 2
    b = 3

    # When: we add the two numbers
    result = add(a, b)

    # Then: the result should be the sum of a and b
    expected_result = 5
    assert result == expected_result

```
***

## Available tutorials
- [Test-driven Development (TDD)](https://github.com/kyaiooiayk/Python-Programming/tree/main/tutorials/Testing/Test-driven%20Development%20(TDD))
- [Unittesting](https://github.com/kyaiooiayk/Python-Programming/tree/main/tutorials/Testing/Unittesting)
- [The Differences Between Unit Testing, Integration Testing and Functional Testing](https://www.softwaretestinghelp.com/the-difference-between-unit-integration-and-functional-testing/)
- [Doctest](https://github.com/kyaiooiayk/Python-Programming/tree/main/tutorials/Testing/Doctest)
- [Parametrised testing](https://github.com/kyaiooiayk/Python-Programming/tree/main/tutorials/Testing/parametrised_testing)
- [How to Use Pytest for Unit Testing](https://www.datacamp.com/tutorial/pytest-tutorial-a-hands-on-guide-to-unit-testing)
- [Pytest](https://github.com/kyaiooiayk/Python-Programming/tree/main/tutorials/Testing/pytest)
***
