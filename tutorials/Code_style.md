# Python code style guidelines
***

## What is PEP?
PEP stands for Python Enhancement Proposals, and the two most known are the PEP8 and the PEP20.
***

## This is not Pythonic!
This usually means that some line of the code do not follow the guidelines and fail to express the intent in what is considered the most redable way.
***

## Anti-patterns
- Anti-patterns are certain patterns in software development that are considered bad programming practices.
- As opposed to design patterns which are common approaches to common problems that have been formalized and are generally considered a good development practice, anti-patterns are the opposite and are undesirable.
- Anti-patterns make code difficult to read, hard to maintain, slow, over-engineered, unstable, prone to errors and with potential security issues.

***

## How to automatically check your code for PEP conformity?
- This is the job of what are called linters: programs that check for conformity. Here are two of them.
- Install pep8: `pip3 install pep8` and run it like this `pep8 my_script.py`
- Install autpep8 `pip3 install autopep8` and run it like this `autopep8 --in-place my_script.py`
***

## Explicit is better than implicit
- This an example of bad coding:
```
def make_dict(*args):
  x, y = args
  return dict(**locsls())
```
- This is an example of good coding:
```
def make_dict(x, y):  
  return {'x':x, 'y':y}
```
- In the good code snippet, x and y are explicitly reveived for the caller, and an explicit dictionary is returned.
***

## Sparse is better than dense
- The general rule is to make one statement per line.
- Some compound statement, such as list comprehensions are well appreciated.
- An example of dense code is:
```
# First example
print("hello");print("hi")
# Second example
if x == 1: print("one")
```
- This can be rewritten as:
```
# First example
print("hello")
print("hi")
# Second example
if x == 1: 
  print("one")
```
***

## General rule to handle errors
- The general rule in python to handle error is to yse `try` and `except`.
- Errors should never be pass silently, unless explicitly silenced. What it means is that if we use the `except` clause without any specified will catch everythin, including `KeyboardInterrupt` and ingnore it! Further, this can also hide bugs, which can hit you back somewhere else in the code.
- An example of error being passed silently:
```
while True:
    try:
        # you can assume somethig that may fail is beinf executed here!
        print("Doing something")
    except:
      # Essentially, you are passing the error silently!
      pass
```
- How should be writing it:
```
while True:
    try:
        # you can assume somethig that may fail is beinf executed here!
        print("Doing something")
    except:
        print("An exception has occured! Raising!")
        raise
```
***

## Fuction arguments should be intuitive to use
- You have 4 ways to pass arguments to the function:
  - Positional arguments
  - Keyword arguments
  - Arbitraary arguments
  - Arbitrary keyword arguments
- And the order is generally accepted to be like this:
```
def my_function(positional, keyword=value, *arg, **kwargs)):
  pass
```
***

## How to import a module
- There three ways to import a module.
  - This is a very bad example because one may be asking whether `sqrt` is part of `modu` or a bulit-in or defined above?:
  ```
  from modu import *
  x = sqrt(4)
  ```
  - This is somehow better. but one may still be asking wheter `sqrt` has been modified or redefined or is it the originally pulled from `modu`?
  ```
  from modue import sqrt
  x = sqrt(4)
  ```
  - This is the best option where it is immediately obviusl that `sqrt` is an attribute of `modu`'s namespace.
  ```
  import modu
  x = modu.sqrt(4)
  ```
***

## Spaghetti & Ravioli code
 - **Spaghetti code**: is a term used to describe a long list of `if` and for `loop` with a lot of copy-pasted codes.
 -  **Ravioli code**: is a term used to describe a collection of disjointed pieces of code withouth a proper structure.
***

## Dynamic typing and reassigning variable names
- **Dynamically typed** language if the types are not known until the code is run, meaning that there will be some additional boilerplate to keep track of what variables are integers, strings, lists, and so on. Thus, use short functions or methods to reduce the risk of using the same name for two unrelated actions. This an example of bad practice:
```
a = 1
a = "answer is {}".format(a)
```
- This is an example of good coding practice:
```
def get_answer(a):
     return  "answer is {}".format(a)"
a = get_asnwer(1)
```
***

## Docstring vs. block comments
- Consider the following code snipper, here is what we can say about it:
  - It can be applied to both methods and classes:
  - The leading comment block on top of the function is a programmer's note
  - Teh doc string describes the operation of the function and it will be shown to the user when the `help(square_root)` is used.
```
# This function needs to be reviewed for speed.
def square_root(x):
  """Return the square root of a x"""
```
***

## Linters & Formatters
- `black` is an auto-formatters. It can be installed as `pip install black` and use like this `black <source_code.py>`; alternatively: `python -m black <source_code.py>`. Black will reformat your file automatically.
- `pycodestyle` is similar to black but the big difference between black and pycodestyle is that black does reformat your code, whereas pycodestyle just complains. It can be installed as `pip install pycodestyle` and use like this `pycodestyle <source_code.py>`; alternatively: `python -m pycodestyle <source_code.py>`
- `flake8` is more than an auto-formatters and is technically speaking a linters. Linters are tools that analyse your code and help you find things like: stylistic issues, programming errors, some types of bugs etc. It can be installed as `pip install flake8` and use like this `flake8 <source_code.py>`; alternatively: `python -m flake8 <source_code.py>`
***

## Naming conventions
- **PascalCase** is used for classes. What this means is that your classes will look like:
```
class Shape: 
    # ...
class Circle(Shape): 
    # ...
```

- **snake_case** is used for variables, functions, methods, arguments:
```
def cool_function(cool_argument, optional_info): 
    # ...
```

- **CAPS_LOCK_WITH_UNDERSCORES** is used to represent global constants. Python doesn’t have support for variables that are truly constant, so we use this convention to help. Generally, you will find these “constants” in the beginning of a file:
```
IMG_BIN = "images"
LOG_FILE = "logs/app.log"
```
***


## References
- [The Hitchhiker's Guide to Python: Best Practices for Development ](https://www.amazon.com/Hitchhikers-Guide-Python-Practices-Development/dp/1491933178/ref=as_li_ss_il?ie=UTF8&linkCode=li2&tag=bookforkind-20&linkId=804806ebdacaf3b56567347f3afbdbca)
- The Data Science Handbook, First Edition. Field Cady. © 2017 John Wiley & Sons, Inc. Published 2017 by John Wiley & Sons, Inc. 
- [18 common python antipatterns](https://towardsdatascience.com/18-common-python-anti-patterns-i-wish-i-had-known-before-44d983805f0f)
***
