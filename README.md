# Python-Programming
*Python programming for Data Scientists*

## Difference between modules and packages?
- As soon as you use the `import` statement, you also use module. Modules in python have they own datatype: if you `import sys` and the `print(type(sys))` you'll get somethig like this `<class 'module'>`.

## How the import modules works
- Whenever we type somethinf like this `import modu` python does the following:
  -  First python searches for a file called `modu.py` in the same directory as the caller.
  -  If the line above is not successful, then python search for `modu.py` in python's search path.
  -  If the line above is not successful then python reases an `ImportError` exception.
  -  If any of the above is found, then python execute `modu.py`.
- How do I know which python's search path my system is using? You can check this by `import sys` and then `sys.path`. All the executed imports. functions and class are then made available to the caller through the module's namespace.

## Namespace Tools
- Module's vairables, functions, and classes are available via the model's namespace. A namespace is a scope containing the names of the things we have imported. We can check what is the namespace with this python's methods:
  - `dir(your_object)` - show you the attributes available in the object
  - `globals()` - a dictionary of the attributes and their values in the global namespace
  - `locals()` - a dictionary of the attributes and their values in the local namespace

## Is python an object-oriented programming language?
- It is sometimes decribes as such, but if compared to other languages this can be misleading. Here is why.
  - Python treats everything (functions, classes, strings, types, etc ...) as an object. The term to dscribe this is first-class object. In this understanding, python is an object-oriented language.
  - The confusion come when comparing it against languages such as Java, C++ and C#. Unlike them, python does not impose object-oriented programming. This means that is perfectly possible in python to use litterarly zero classes, no class inheritance or any other mechanism specific to a fully fledged object-oriented language. Essentially, the feature are available but not compulsory!

## Static versus Dynamic Typing
- **Statically typed** language if the computer figures out, at the time the code is compiled, what the type is of all the variables. 
- **Dynamically typed** language if the types are not known until the code is run, meaning that there will be some additional boilerplate to keep track of what variables are integers, strings, lists, and so on. 
- Python is a great example of a dynamically typed language. The interpreter is written in C, and under the hood, every variable is implemented as a C structure called a PyObject. One function of the PyObject structure is to keep track of what the type is of each variable. There is a lot of overhead in this approach. Most simply, you have to store more stuff in RAM: not just your actual data, but the type metadata. The other problem is that, before your code can perform some operation (such as “+”) on a variable, it must first check what data type that variable is and hence what the operation means in this context. Dynamic typing has many benefits in terms of flexibility, but **you pay a large performance cost**. In a statically typed language such as C, on the other hand, the compiler can just translate every operation into the appropriate byte‐level manipulations, without storing any explicit reference to the data types or any method lookups. 

## Functional programming 
Functional programming is a programming paradigm in which the primary method of computation is evaluation of functions. It typically plays a fairly small role in Python code. A more in-depth article can be found [here](https://realpython.com/python-functional-programming/). In functional programming, a program consists entirely of evaluation of pure functions. A pure function is a function whose output value follows solely from its input values, without any observable side effects. 

## Mutable and immutable types
- First of all, why do we need this distinction? If used properly, and if you remember about it, making the diffence between mutable and immutable clarifies the intent of your code. 
- **Mutable types** allows inplace modifications of the object's content. Examples are lists and dictionaries which both have mutating methods such as `list.append()` or `dict.pop()`.
- **Immutable types** provide no methods to allow inplace inplace modifications. Examples are tuple, integer and string. Because of this, mutable types cannot be used as dictionaty keys because if the value changes, it will not hash back to the same value!

## Testing your code
- **TDD** (Test Driven Development) is a way of code development where the developer first writes the test and after that the function.
- **BDD** (Behaviour-Driven Development)

## Project documentation
- A project should generally containt this 5 files.
  - A `README` file = detailes the purpouse of the project
    - An INSTALL section [inside the README file] = detailes how to install the package or everything which is needed to run the code
    - A TODO section = [inside the README file] = detailes the planned development
    - A CHANGELOG section [inside the README file] = details a short overview of the changes
  - A license file = conditions under which the software is made available to the public

## How to release your own python package
- There at least 4 ways you can do it. Please refere to this [reference](https://github.com/idrl-lab/idrlnet) to see how they did it.
- For all the following 4 options the general rule is still valid: to avoid version conflicts, please use some tools to create a virtual environment first.
  - **Option No#1**: simple installation from PyPI: `pip install -U your_package_name`
  - **Option No#2**: Docker, pull latest docker image from Dockerhub: `docker pull our_package_name:latest` and then `docker run -it our_package_name:latest bash`
  - **Option No#3**: using anaconda or miniconda: first `conda create -n your_ve_name python=3.8 -y` then `conda activate your_ve_name` and finally: `pip install your_package_name`
  - **Option No#4**: from source

## pip install vs. conda install
- `pip` is an open source project and is maintained by PyPa (Python Packaging Authority)
- `conda` is the commericial equivalent of `pip` maintained by Continuum analytics.
- Very briefly, consider conda an option suited for non coders. This is the easiest way to reach the wide academic, commerical, and Windoes-using audience.

## Freezing your code
- To *freeze* the code means to create a standalone executable bundle you can distribute without having the end users to have Python installed in their system. Effectively, the distribution contains both the application code and the Python interpreter. As they say, `.py` files are for software engineer and system administrator.

## References
- [The Hitchhiker's Guide to Python: Best Practices for Development ](https://www.amazon.com/Hitchhikers-Guide-Python-Practices-Development/dp/1491933178/ref=as_li_ss_il?ie=UTF8&linkCode=li2&tag=bookforkind-20&linkId=804806ebdacaf3b56567347f3afbdbca)
- The Data Science Handbook, First Edition. Field Cady. © 2017 John Wiley & Sons, Inc. Published 2017 by John Wiley & Sons, Inc. 
