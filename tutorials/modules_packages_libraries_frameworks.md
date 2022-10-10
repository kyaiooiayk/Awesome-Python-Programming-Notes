# Difference between modules, packages, libraries and frameworks?
***

## Module
- *Module*: As soon as you use the `import` statement, you also use module. Modules in python have they own datatype: if you `import sys` and the `print(type(sys))` you'll get somethig like this `<class 'module'>`. Examples are:
  - `random` module to generate pseudo-random number generators for various distributions.
  - `html` module to parse HTML pages.
***

## Package
- *Packages*: When developing a large application, you may end up with many different modules that are difficult to manage. In such a case, you’ll benefit from grouping and organizing your modules. That’s when packages come into play.
Python packages are basically a directory of a collection of modules. Packages allow the hierarchical structure of the module namespace. Just like we organize our files on a hard drive into folders and sub-folders, we can organize our modules into packages and subpackages.
To be considered a package (or subpackage), a directory must contain a file named __init__.py. This file usually includes the initialization code for the corresponding package. Examples are:
  - `NumPy` is the fundamental Python package for scientific computing.
  - `pandas` is a Python package for fast and efficient processing of tabular data, time series, matrix data, etc.
  - `pytest` provides a variety of modules to test new code, including small unit tests or complex functional tests.
***


## Libraries
- *Libraries*: A library is an umbrella term referring to a reusable chunk of code. Usually, a Python library contains a collection of related modules and packages. Actually, this term is often used interchangeably with “Python package” because packages can also contain modules and other packages (subpackages). However, it is often assumed that while a package is a collection of modules, a library is a collection of packages.
Oftentimes, developers create Python libraries to share reusable code with the community. To eliminate the need for writing code from scratch, they create a set of useful functions related to the same area. Examples are:
  - `Matplotlib` library is a standard library for generating data visualizations in Python. It supports building basic two-dimensional graphs as well as more complex animated and interactive visualizations.
  - `PyTorch` is an open-source deep-learning library built by Facebook’s AI Research lab to implement advanced neural networks and cutting-edge research ideas in industry and academia.
***

## Frameworks
- *Frameworks*: Similar to libraries, Python frameworks are a collection of modules and packages that help programmers to fast track the development process. However, frameworks are usually more complex than libraries. Also, while libraries contain packages that perform specific operations, frameworks contain the basic flow and architecture of the application. If you compare application development to house construction, Python frameworks provide all the essential building blocks like the foundation, walls, windows, and roof. Then, the developers build their application around this foundation by adding functionalities comparable to a house’s alarm system, furniture, appliances, etc. Examples are:
  - `Django` is a Python framework for building web applications with less coding. With all the necessary features included by default, developers can focus on their applications rather than dealing with routine processes.
  - `Flask` is a web development framework that is known for its lightweight and modular design. It has many out-of-the-box features and is easily adaptable to specific requirements.
***

## References
- [Differences btw modules, packages and libraries](https://learnpython.com/blog/python-modules-packages-libraries-frameworks/)
- [Packages](https://python-course.eu/python-tutorial/packages.php)
- [Modules and modular programming](https://python-course.eu/python-tutorial/modules-and-modular-programming.php)