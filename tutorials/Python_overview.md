# Python-Programming
*Python programming for Data Scientists*
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
- A simple example is the operator `+`. The operator `+` is **overloaded** which means its action depends on the type of the objects on which it acts. Python must check the type of the objects and then call the correct operation. This involves substantial overheads.
```python
# sum btw two string
a = "a"
b = "b"
a+b # requires string concatenation

a = 1
b = 2
a+b # requires to sum the integers

```
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

## Freezing your code
- To *freeze* the code means to create a standalone executable bundle you can distribute without having the end users to have Python installed in their system. Effectively, the distribution contains both the application code and the Python interpreter. As they say, `.py` files are for software engineer and system administrator.
***

## Monkey patch
A monkey patch is a way for a program to extend or modify supporting system software locally (affecting only the running instance of the program).
```python
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
- [Difference between .py and .pyc files?](http://net-informations.com/python/iq/pyc.htm)
- https://realpython.com/python-walrus-operator/
