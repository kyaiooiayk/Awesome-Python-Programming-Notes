# Python-Programming
*Python programming for Data Scientists*
***

## Difference between modules, packages, libraries and frameworks?
- *Module*: As soon as you use the `import` statement, you also use module. Modules in python have they own datatype: if you `import sys` and the `print(type(sys))` you'll get somethig like this `<class 'module'>`. Examples are:
  -  `random` module to generate pseudo-random number generators for various distributions.
  - `html` module to parse HTML pages.

- *Packages*: When developing a large application, you may end up with many different modules that are difficult to manage. In such a case, you’ll benefit from grouping and organizing your modules. That’s when packages come into play.
Python packages are basically a directory of a collection of modules. Packages allow the hierarchical structure of the module namespace. Just like we organize our files on a hard drive into folders and sub-folders, we can organize our modules into packages and subpackages.
To be considered a package (or subpackage), a directory must contain a file named __init__.py. This file usually includes the initialization code for the corresponding package. Examples are:
  - `NumPy` is the fundamental Python package for scientific computing.
  - `pandas` is a Python package for fast and efficient processing of tabular data, time series, matrix data, etc.
  - `pytest` provides a variety of modules to test new code, including small unit tests or complex functional tests.

- *Libraries*: A library is an umbrella term referring to a reusable chunk of code. Usually, a Python library contains a collection of related modules and packages. Actually, this term is often used interchangeably with “Python package” because packages can also contain modules and other packages (subpackages). However, it is often assumed that while a package is a collection of modules, a library is a collection of packages.
Oftentimes, developers create Python libraries to share reusable code with the community. To eliminate the need for writing code from scratch, they create a set of useful functions related to the same area. Examples are:
  - `Matplotlib` library is a standard library for generating data visualizations in Python. It supports building basic two-dimensional graphs as well as more complex animated and interactive visualizations.
  - `PyTorch` is an open-source deep-learning library built by Facebook’s AI Research lab to implement advanced neural networks and cutting-edge research ideas in industry and academia.
  
- *Frameworks*: Similar to libraries, Python frameworks are a collection of modules and packages that help programmers to fast track the development process. However, frameworks are usually more complex than libraries. Also, while libraries contain packages that perform specific operations, frameworks contain the basic flow and architecture of the application. If you compare application development to house construction, Python frameworks provide all the essential building blocks like the foundation, walls, windows, and roof. Then, the developers build their application around this foundation by adding functionalities comparable to a house’s alarm system, furniture, appliances, etc. Examples are:
  - `Django` is a Python framework for building web applications with less coding. With all the necessary features included by default, developers can focus on their applications rather than dealing with routine processes.
  - `Flask` is a web development framework that is known for its lightweight and modular design. It has many out-of-the-box features and is easily adaptable to specific requirements.

***

## How the import modules works
- Whenever we type somethinf like this `import modu` python does the following:
  -  First python searches for a file called `modu.py` in the same directory as the caller.
  -  If the line above is not successful, then python search for `modu.py` in python's search path.
  -  If the line above is not successful then python reases an `ImportError` exception.
  -  If any of the above is found, then python execute `modu.py`.
- How do I know which python's search path my system is using? You can check this by `import sys` and then `sys.path`. All the executed imports. functions and class are then made available to the caller through the module's namespace.
***

## Namespace Tools
- Module's vairables, functions, and classes are available via the model's namespace. A namespace is a scope containing the names of the things we have imported. We can check what is the namespace with this python's methods:
  - `dir(your_object)` - show you the attributes available in the object
  - `globals()` - a dictionary of the attributes and their values in the global namespace
  - `locals()` - a dictionary of the attributes and their values in the local namespace
***

## Is python an object-oriented programming language?
- It is sometimes decribes as such, but if compared to other languages this can be misleading. Here is why.
  - Python treats everything (functions, classes, strings, types, etc ...) as an object. The term to dscribe this is first-class object. In this understanding, python is an object-oriented language.
  - The confusion come when comparing it against languages such as Java, C++ and C#. Unlike them, python does not impose object-oriented programming. This means that is perfectly possible in python to use litterarly zero classes, no class inheritance or any other mechanism specific to a fully fledged object-oriented language. Essentially, the feature are available but not compulsory!
***

## Static versus Dynamic Typing
- **Statically typed** language if the computer figures out, at the time the code is compiled, what the type is of all the variables. 
- **Dynamically typed** language if the types are not known until the code is run, meaning that there will be some additional boilerplate to keep track of what variables are integers, strings, lists, and so on. 
- Python is a great example of a dynamically typed language. The interpreter is written in C, and under the hood, every variable is implemented as a C structure called a PyObject. One function of the PyObject structure is to keep track of what the type is of each variable. There is a lot of overhead in this approach. Most simply, you have to store more stuff in RAM: not just your actual data, but the type metadata. The other problem is that, before your code can perform some operation (such as “+”) on a variable, it must first check what data type that variable is and hence what the operation means in this context. Dynamic typing has many benefits in terms of flexibility, but **you pay a large performance cost**. In a statically typed language such as C, on the other hand, the compiler can just translate every operation into the appropriate byte‐level manipulations, without storing any explicit reference to the data types or any method lookups. 
***

## Functional programming 
- Functional programming is a programming paradigm in which the primary method of computation is evaluation of functions. A more in-depth article can be found [here](https://realpython.com/python-functional-programming/). 
- In functional programming, a program consists entirely of evaluation of pure functions. A pure function is a function whose output value follows solely from its input values, without any observable side effects. 
- The `map`, `filter` and `reduce` functions (which lives in Python's `functools` module) are fundamental components of the functional programming. 
- This style, which, while not a dominant programming style in the Python world, has its outspoken proponents.
- A programming style in which functions are treated and manipulated as objects, i.e. functions can be assigned to variables, they can be passed as arguments, and they can be stored in containers along with other data. We can write parallel code that works by running lots of functions in parallel on large amounts of data.
- When you build your applications completely out of pure functions. A pure function has its return value determined exclusively by it's arguments.
***

## Mutable and immutable types
- First of all, why do we need this distinction? If used properly, and if you remember about it, making the diffence between mutable and immutable clarifies the intent of your code. 
- **Mutable types** allows inplace modifications of the object's content. Examples are lists and dictionaries which both have mutating methods such as `list.append()` or `dict.pop()`.
- **Immutable types** provide no methods to allow inplace inplace modifications. Examples are tuple, integer and string. Because of this, mutable types cannot be used as dictionaty keys because if the value changes, it will not hash back to the same value!
***

## Testing your code
- **TDD** (Test Driven Development) is a way of code development where the developer first writes the test and after that the function.
- **BDD** (Behaviour-Driven Development)
***

## Project documentation
- A project should generally containt this 5 files.
  - A `README` file = detailes the purpouse of the project
    - An INSTALL section [inside the README file] = detailes how to install the package or everything which is needed to run the code
    - A TODO section = [inside the README file] = detailes the planned development
    - A CHANGELOG section [inside the README file] = details a short overview of the changes
  - A license file = conditions under which the software is made available to the public
***

## How to release your own python package
- There at least 4 ways you can do it. Please refere to this [reference](https://github.com/idrl-lab/idrlnet) to see how they did it.
- For all the following 4 options the general rule is still valid: to avoid version conflicts, please use some tools to create a virtual environment first.
  - **Option No#1**: simple installation from PyPI: `pip install -U your_package_name`
  - **Option No#2**: Docker, pull latest docker image from Dockerhub: `docker pull our_package_name:latest` and then `docker run -it our_package_name:latest bash`
  - **Option No#3**: using anaconda or miniconda: first `conda create -n your_ve_name python=3.8 -y` then `conda activate your_ve_name` and finally: `pip install your_package_name`
  - **Option No#4**: from source
***

## pip install vs. conda install
- `pip` is an open source project and is maintained by PyPa (Python Packaging Authority)
- `conda` is the commericial equivalent of `pip` maintained by Continuum analytics.
- Very briefly, consider conda an option suited for non coders. This is the easiest way to reach the wide academic, commerical, and Windoes-using audience.
***

## Freezing your code
- To *freeze* the code means to create a standalone executable bundle you can distribute without having the end users to have Python installed in their system. Effectively, the distribution contains both the application code and the Python interpreter. As they say, `.py` files are for software engineer and system administrator.
***

## Monkey patch
A monkey patch is a way for a program to extend or modify supporting system software locally (affecting only the running instance of the program). 
```
>>> import math
>>> math.pi
3.141592653589793
>>> math.pi = 3.2   # monkey-patch the value of Pi in the math module
>>> math.pi
3.2
================================ RESTART ================================
>>> import math
>>> math.pi
3.141592653589793
```
***

## Difference between .py and .pyc files?

- Python compiles the .py files and saves it as .pyc files , so it can reference them in subsequent invocations. The .pyc contain the compiled bytecode of Python source files. The .pyc contain the compiled bytecode of Python source files, which is what the Python interpreter compiles the source to. This code is then executed by Python's virtual machine . There's no harm in deleting them (.pyc), but they will save compilation time if you're doing lots of processing.

- Python is an interpreted language , as opposed to a compiled one, though the distinction can be blurry because of the presence of the bytecode compiler. Compiling usually means converting to machine code which is what runs the fastest. But interpreters take human readable text and execute it. They may do this with an intermediate stage .

- For example, When you run myprog.py source file, the python interpreter first looks to see if any 'myprog.pyc' (which is the byte-code compiled version of 'myprog.py') exists, and if it is more recent than 'myprog.py'. If so, the interpreter runs it. If it does not exist, or 'myprog.py' is more recent than it (meaning you have changed the source file), the interpreter first compiles 'myprog.py' to 'myprog.pyc'.

- There is one **exception** to the above example. If you put `#! /usr/bin/env python` on the first line of `myprog.py`, make it executable , and then run 'myprog.py' by itself.
***


## Statement & expression

- A **statement** in Python is a unit of code. For example number = 1 + 2 is an assignment statement that doesn’t evaluate to a value.
- An **expression** is a special statement that can be evaluated to some value. For example, 1 + 2 is an expression that evaluates to the value 3.
***


## References
- [The Hitchhiker's Guide to Python: Best Practices for Development ](https://www.amazon.com/Hitchhikers-Guide-Python-Practices-Development/dp/1491933178/ref=as_li_ss_il?ie=UTF8&linkCode=li2&tag=bookforkind-20&linkId=804806ebdacaf3b56567347f3afbdbca)
- The Data Science Handbook, First Edition. Field Cady. © 2017 John Wiley & Sons, Inc. Published 2017 by John Wiley & Sons, Inc. 
- [Differences btw modules, packages and libraries](https://learnpython.com/blog/python-modules-packages-libraries-frameworks/)
- [Difference between .py and .pyc files?](http://net-informations.com/python/iq/pyc.htm)
- https://realpython.com/python-walrus-operator/