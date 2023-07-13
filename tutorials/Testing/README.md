# How to test your python code
***

## Testing your code
- **TDD** (Test Driven Development) is a way of code development where the developer first writes the test and after that the function.
- **BDD** (Behaviour-Driven Development) combines the general techniques and principles of TDD with ideas from domain-driven design and object-oriented analysis and design to provide software development and management teams with shared tools and a shared process to collaborate on software development.
***

## Type of testing
- **Acceptance tests** are a quality assurance (QA) process that determines to what degree an application meets end users' approval.
- **Functional tests** check the functionalities of the entire system and ensure different components work together as intended. Theirs purpose is to check an entire application, including its hardware, networking infrastructure, front-end UI, and the back-end database.
- **Integration tests** check if different modules are working fine when combined together as a group.
- **Unit tests** isolate and test individual code units to verify they function as intended. You use unit testing to verify that specific system behaviors produce the intended results. Unit tests point to a specific issue that requires fixing. Since functional testing checks the entire application, it mainly indicates a general issue without pointing out a specific problem.

![image](https://github.com/kyaiooiayk/Awesome-Python-Programming-Notes/assets/89139139/48620a78-ad8f-4da5-b6e4-6982e36110ba)
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
