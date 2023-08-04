#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Introduction" data-toc-modified-id="Introduction-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Introduction</a></span></li><li><span><a href="#Imports" data-toc-modified-id="Imports-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Imports</a></span></li><li><span><a href="#What-is-a-decorator?" data-toc-modified-id="What-is-a-decorator?-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>What is a decorator?</a></span></li><li><span><a href="#Creating-a-decorator" data-toc-modified-id="Creating-a-decorator-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>Creating a decorator</a></span><ul class="toc-item"><li><span><a href="#ourDecorators()-vs.-ourDecorators" data-toc-modified-id="ourDecorators()-vs.-ourDecorators-4.1"><span class="toc-item-num">4.1&nbsp;&nbsp;</span><code>ourDecorators()</code> vs. <code>ourDecorators</code></a></span></li><li><span><a href="#Why-using-wrap?" data-toc-modified-id="Why-using-wrap?-4.2"><span class="toc-item-num">4.2&nbsp;&nbsp;</span>Why using <code>wrap</code>?</a></span></li></ul></li><li><span><a href="#How-to-unwrap-a-function-from-a-decorator" data-toc-modified-id="How-to-unwrap-a-function-from-a-decorator-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>How to unwrap a function from a decorator</a></span></li><li><span><a href="#What-would-it-be-if-there-was-not-decorator?" data-toc-modified-id="What-would-it-be-if-there-was-not-decorator?-6"><span class="toc-item-num">6&nbsp;&nbsp;</span>What would it be if there was not decorator?</a></span></li><li><span><a href="#How-to-unwrap" data-toc-modified-id="How-to-unwrap-7"><span class="toc-item-num">7&nbsp;&nbsp;</span>How to unwrap</a></span></li><li><span><a href="#Chaining-Decorators-in-Python" data-toc-modified-id="Chaining-Decorators-in-Python-8"><span class="toc-item-num">8&nbsp;&nbsp;</span>Chaining Decorators in Python</a></span></li><li><span><a href="#How-to-handle-function-decorator-inside-a-class" data-toc-modified-id="How-to-handle-function-decorator-inside-a-class-9"><span class="toc-item-num">9&nbsp;&nbsp;</span>How to handle function decorator inside a class</a></span></li><li><span><a href="#How-to-add-parameters-to-a-decorator" data-toc-modified-id="How-to-add-parameters-to-a-decorator-10"><span class="toc-item-num">10&nbsp;&nbsp;</span>How to add parameters to a decorator</a></span><ul class="toc-item"><li><span><a href="#Example-#1" data-toc-modified-id="Example-#1-10.1"><span class="toc-item-num">10.1&nbsp;&nbsp;</span>Example #1</a></span></li><li><span><a href="#Example-#2" data-toc-modified-id="Example-#2-10.2"><span class="toc-item-num">10.2&nbsp;&nbsp;</span>Example #2</a></span></li></ul></li><li><span><a href="#How-to-make-the-decorator-callable" data-toc-modified-id="How-to-make-the-decorator-callable-11"><span class="toc-item-num">11&nbsp;&nbsp;</span>How to make the decorator callable</a></span><ul class="toc-item"><li><span><a href="#With-args-and-kargs" data-toc-modified-id="With-args-and-kargs-11.1"><span class="toc-item-num">11.1&nbsp;&nbsp;</span>With args and kargs</a></span></li><li><span><a href="#With-kargs-only" data-toc-modified-id="With-kargs-only-11.2"><span class="toc-item-num">11.2&nbsp;&nbsp;</span>With kargs only</a></span></li></ul></li><li><span><a href="#Practical-Use-Cases" data-toc-modified-id="Practical-Use-Cases-12"><span class="toc-item-num">12&nbsp;&nbsp;</span>Practical Use Cases</a></span></li><li><span><a href="#Advance-logging" data-toc-modified-id="Advance-logging-13"><span class="toc-item-num">13&nbsp;&nbsp;</span>Advance logging</a></span></li><li><span><a href="#References" data-toc-modified-id="References-14"><span class="toc-item-num">14&nbsp;&nbsp;</span>References</a></span></li></ul></div>

# # Introduction
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-warning">
# <font color=black>
# 
# **What?** Function decorators
# 
# </font>
# </div>

# # Imports
# <hr style="border:2px solid black"> </hr>

# In[2]:


import functools
from functools import wraps


# # What is a decorator?
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-info">
# <font color=black>
# 
# - A decorator takes in a function, adds some functionality and **RETURNS** it.
# - A **decorator** is basically a function that takes another function as an argument, adds some kind of functionality and then returns another function. So why would we want to do something like this? Well, it's because this allows us to easily add or alter the functionality to our existing function method or class without having to directly use its subclasses. In short, **decorators** are simply wrappers to existing functions.
# 
# </font>
# </div>

# # Creating a decorator
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-info">
# <font color=black>
# 
# - Our decorator does nothing more than adding an extra print functions.
# - If you're wondering why there is a ` @functools.wraps ` here while other examples do not have it, it is because it is **good practice**. 
# - This automatically adds a `__wrapped__` attribute that let you retrieve the original, undecorated function
# 
# </font>
# </div>

# In[51]:


def ourDecorator(func: callable):
    @functools.wraps(func)
    def functionWrapper(x):
        print("Decorating the function")
        func(x)        
    return functionWrapper


# In[52]:


@ourDecorator
def foo(x):
    print("Hi, foo has been called with: " + str(x))


# In[53]:


# Let us call foo
foo("Hi")


# In[54]:


# This can be also re-written as (keep in mind that @function is just a syntaz sugar)
ourDecorator(foo("Hi"));


# ## `ourDecorators()` vs. `ourDecorators`

# In[55]:


@ourDecorator()
def foo(x):
    print("Hi, foo has been called with: " + str(x))


# <div class="alert alert-info">
# <font color=black>
# 
# - `@decorator def func` gets replaced by `func = decorator(func)`.
# - `@decorator() def func` gets replaced by `func = decorator()(func)`. So in the latter case, decorator() is run, and it needs to return a function which accepts a function as as an argument, and returns a function.
# 
# </font>
# </div>

# ## Why using `wrap`?

# <div class="alert alert-info">
# <font color=black>
# 
# - You should always use wraps, when implementing decorators.
# - It will fix the function metadata (for example: copy the __name__, the docstring, etc). 
# - An example is provided below to showcase what will happen if you dont'.
# 
# </font>
# </div>

# In[14]:


def ourDecorator(func: callable):
    """With wraps"""
    @functools.wraps(func)
    def functionWrapper(x):
        print("Decorating the function")
        func(x)        
    return functionWrapper

@ourDecorator
def foo(x):
    print("Hi, foo has been called with: " + str(x))
    
foo("Hi")


# In[15]:


# The original funciton name can be access via
foo.__name__


# In[16]:


#  Reference to the original, undecorated function.
foo.__wrapped__


# In[17]:


def ourDecorator(func: callable):
    """With no wraps"""
    def functionWrapper(x):
        print("Decorating the function")
        func(x)        
    return functionWrapper

@ourDecorator
def foo(x):
    print("Hi, foo has been called with: " + str(x))
    
foo("Hi")


# In[18]:


# The original funciton name cann't be access via
foo.__name__


# In[19]:


# Reference to the original, undecorated function will not be available
foo.__wrapped__


# # How to unwrap a function from a decorator
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-info">
# <font color=black>
# 
# - How do we go back to the undecorated function?
# - One solution would be to use @include_original 
# - https://stackoverflow.com/questions/1166118/how-to-strip-decorators-from-a-function-in-python
# 
# </font>
# </div>

# In[6]:


# This is equivalent to 
ourDecorator(foo("Hi"))


# In[7]:


foo.__wrapped__("Hi")


# In[8]:


"""
However, instead of manually accessing the __wrapped__ attribute, it's better to use inspect.unwrap:
IT IS NOT WORKING!
"""


# In[9]:


import inspect
inspect.unwrap(foo)


# In[10]:


inspect.unwrap(foo("Hi"))


# # What would it be if there was not decorator?
# <hr style="border:2px solid black"> </hr>

# In[11]:


def make_pretty(func):
    def inner():
        print("I got decorated")
        func()
    return inner


def ordinary():
    print("I am ordinary")


# In[12]:


# Let us call the ordinary function
ordinary()


# In[13]:


# let's decorate this ordinary function. essentially all it added was a print statement
pretty = make_pretty(ordinary)
pretty()


# In[14]:


# Generally, we decorate a function and reassign it as
ordinary = make_pretty(ordinary)


# In[15]:


ordinary()


# <div class="alert alert-info">
# <font color=black>
# 
# - This is a common construct and for this reason, Python has a syntax to simplify this.
# - We can use the `@` symbol along with the name of the decorator function and place it above the definition of the function to be decorated. Essentially this is a syntactuc sugar 
# 
# </font>
# </div>

# In[16]:


@make_pretty
def ordinary():
    print("I am ordinary")


# In[17]:


ordinary()


# In[18]:


# This is equivalent to
def ordinary():
    print("I am ordinary")
ordinary = make_pretty(ordinary)
ordinary()


# # How to unwrap
# <hr style="border:2px solid black"> </hr>

# In[19]:


def divide(a, b):
    return a/b


# In[20]:


divide(4,2)


# In[21]:


# This call will spit out an error. We'll show how to create a decorator to check for this
divide(4,0)


# In[ ]:


def smart_divide(func):
    def inner(a, b):
        print("I am going to divide", a, "and", b)
        if b == 0:
            print("Whoops! cannot divide")
            return

        return func(a, b)
    return inner


# In[ ]:


@smart_divide
def divide(a, b):
    print(a/b)


# In[ ]:


divide(4,0)


# In[ ]:


# we saw it is good practice to add @functools.wraps()


# In[ ]:


def smart_divide(func):
    @functools.wraps(func)
    def inner(a, b):
        print("I am going to divide", a, "and", b)
        if b == 0:
            print("Whoops! cannot divide")
            return

        return func(a, b)
    return inner


# In[ ]:


@smart_divide
def divide(a, b):
    print(a/b)


# In[ ]:


# Again, if I want to use the old undecoreated function I can do
divide.__wrapped__(4,0)


# In[ ]:


divide(4,0)


# # Chaining Decorators in Python
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-info">
# <font color=black>
# 
# - Multiple decorators can be chained in Python.
# - This is to say, a function can be decorated multiple times with different (or same) decorators. 
# - We simply place the decorators above the desired function.
# 
# </font>
# </div>

# In[ ]:


def star(func):
    def inner(*args, **kwargs):
        print("*" * 30)
        func(*args, **kwargs)
        print("*" * 30)
    return inner


def percent(func):
    def inner(*args, **kwargs):
        print("%" * 30)
        func(*args, **kwargs)
        print("%" * 30)
    return inner


# In[ ]:


@star
@percent
def printer(msg):
    print(msg)


printer("Hello")


# In[ ]:


# For comlpeteness the above syntax is equivalent to 
def printer(msg):
    print(msg)
printer = star(percent(printer))


# # How to handle function decorator inside a class
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-info">
# <font color=black>
# 
# - When decorating a method inside a class we need to hanfle `self` explicitly.
# 
# </font>
# </div>

# In[ ]:


class A():
        
    def __init__(self, data):
        self.data = data

    def myPrintDecorator(func):
        """My print decorator        
        
        Print the name of the method when it is called.
        """
        
        def printCallNameMethod(self, *args, **kwargs):        
            print("Using method", func.__name__)
            instance = func(self, *args, **kwargs)            
            return instance 
        
        return printCallNameMethod
    
    @myPrintDecorator
    def double(self):
        return self.data*2


# In[ ]:


instance = A([1,1])
a = instance.double()
print(a)


# # How to add parameters to a decorator
# <hr style="border:2px solid black"> </hr>

# ## Example #1

# In[25]:


def get_time(t_start: float, t_end: float, unit: str):
    """Get elapsed time given the unit.
    """
    if unit.lower() == "sec":
        return np.around(t_end - t_start, 3)

    elif unit.lower() == "min":
        return np.around((t_end - t_start) / 60, 3)

    elif unit.lower() == "hr":
        return np.around((t_end - t_start) / 3600, 3)
    else:
        raise TypeError(f"Unit of time {unit} not known!")


# In[37]:


import time


def time_it(
    func_: None = None,
    unit: str = "sec",
):

    def _decorator(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            t1 = time.time()
            output = func(self, *args, **kwargs)
            t2 = time.time()

            print(
                f"Executed in: {str(get_time(t1, t2, unit))} {unit}")

            return output

        return wrapper

    if callable(func_):
        return _decorator(func_)
    elif func_ is None:
        return _decorator
    else:
        raise RuntimeWarning("Positional arguments are not supported!")


# In[38]:


@time_it(unit="sec")
def sum_two_numbers(a,b):
    time.sleep(2)
    return a+b


# In[39]:


sum_two_numbers(1,2)


# In[40]:


@time_it(unit="min")
def sum_two_numbers(a,b):
    time.sleep(2)
    return a+b


# In[41]:


sum_two_numbers(1,2)


# In[42]:


# Alternative syntax
time_it(unit="sec")(sum_two_numbers(1,2));


# ## Example #2

# In[46]:


def repeat(n: int = 1):
    def decorator(func: callable):
        def inner(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return inner
    return decorator

@repeat(n=3)
def hello(name: str):
    print(f'Hello {name}!')

hello('world')


# # How to make the decorator callable
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-info">
# <font color=black>
# 
# 
# 
# - This is a template for a function decorator that does not require `()` if no parameters are to be given and supports both positional and keyword parameters (but requires cheching on `locals()` to find out if the first parameter is the function to be decorated or not):
# 
# </font>
# </div>

# ## With args and kargs

# In[ ]:


import functools


# In[ ]:


def multiplying(factor_or_func=None):
    def _decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if 'factor_or_func' not in locals() \
                    or callable(factor_or_func) \
                    or factor_or_func is None:
                factor = 1
            else:
                factor = factor_or_func
            return factor * func(*args, **kwargs)
        return wrapper
    return _decorator(factor_or_func) if callable(factor_or_func) else _decorator


# In[ ]:


@multiplying
def summing(x): return sum(x)
summing([3,2])


# In[ ]:


@multiplying()
def summing(x): return sum(x)
summing([3,2])


# In[ ]:


@multiplying(2)
def summing(x): return sum(x)
summing([3,2])


# ## With kargs only

# In[ ]:


def multiplying(func_=None, factor=1):
    def _decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            return factor * func(*args, **kwargs)
        return wrapper

    if callable(func_):
        return _decorator(func_)
    elif func_ is None:
        return _decorator
    else:
        raise RuntimeWarning("Positional arguments are not supported.")


# In[ ]:


@multiplying
def summing(x): return sum(x)
summing([3,2])


# In[ ]:


@multiplying()
def summing(x): return sum(x)
summing([3,2])


# In[ ]:


@multiplying(factor=2)
def summing(x): return sum(x)
summing([3,2])


# # Practical Use Cases
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-info">
# <font color=black>
# 
# - While writing a large code there two things we want to do as basics.
#     - How fast it runs and generally we time it
#     - What is doing and generally we use some print statements
# 
# - Now consider the situation where you have to do it over and over. A nice way to save you space and time is to create two decorator that do just this for you.
# 
# </font>
# </div>

# In[ ]:


import time
import logging
import functools

def timer(func):
    """time the running time of the passed in function"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = func(*args, **kwargs)
        t2 = time.time() - t1
        print('{} ran in: {} sec'.format(func.__name__, t2))
        return result
    
    return wrapper


# In[ ]:


@timer
def display_info(name, age):
    time.sleep(1)  # manually add a second to the timing
    print('display info ran with arguments ({}, {})'.format(name, age))

display_info('John', 25)


# In[ ]:


def logger(func):
    """
    create logging for the function,
    re-define the format to add specific logging time
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        logging.basicConfig(
            filename = './logging_example',
            format = '%(asctime)s -- %(levelname)s:%(name)s: %(message)s',
            datefmt = '%Y/%m/%d-%H:%M:%S',
            level = logging.INFO)
        
        # custom the logging information
        logging.info('Ran with args: {} and kwargs: {}'.format(args, kwargs))
        return func(*args, **kwargs)

    return wrapper


# In[ ]:


# http://stackoverflow.com/questions/18786912/get-output-from-the-logging-module-in-ipython-notebook
# ipython notebook already call basicConfig somewhere, thus reload the logging
import logging
from importlib import reload
reload(logging)

@logger
def display_info(name, age):
    print('display info ran with arguments ({}, {})'.format(name, age))
    
display_info('John', 25)


# In[ ]:


@logger
@timer
def display_info(name, age):
    time.sleep(1) # manually add a second to the timing
    print('display info ran with arguments ({}, {})'.format(name, age))
    
display_info('Tom', 22)


# In[ ]:


dir(logging)


# In[ ]:


import logging

logging.basicConfig(filename='./example.log', encoding='utf-8', level=logging.DEBUG)
logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')
logging.error('And non-ASCII stuff, too, like Øresund and Malmö')


# # Advance logging
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-info">
# <font color=black>
# 
# - Please refer to this folder `Decorators_Advanced_Example` for a more advanced used of the decorators. 
# - In particular, one of th example shows how to keep track of two diffrent handlers: one that is written on a `.log` file where you print all the info and another one that keep track of the message printed on the console.
# 
# </font>
# </div>

# In[ ]:


# List only directories
get_ipython().system('ls -d */')


# In[ ]:


get_ipython().system('ls')


# # References
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-warning">
# <font color=black>
# 
# - https://www.programiz.com/python-programming/decorator
# - [How to handle function decorator inside a class](https://stackoverflow.com/questions/38524332/declaring-decorator-inside-a-class)
# - [Blog: Guide to python function decorators](http://thecodeship.com/patterns/guide-to-python-function-decorators/)
# - [Youtube: Decorators - Dynamically Alter The Functionality Of Your Functions](https://www.youtube.com/watch?v=FsAPt_9Bf3U)
# - http://nbviewer.jupyter.org/github/ethen8181/machine-learning/blob/master/python/decorators/decorators.ipynb
# - https://medium.com/swlh/add-log-decorators-to-your-python-project-84094f832181
# - https://machinelearningmastery.com/a-gentle-introduction-to-decorators-in-python/
# - [Decorators with parameters?](https://stackoverflow.com/questions/5929107/decorators-with-parameters)
# - [python decorator patterns](https://bytepawn.com/python-decorator-patterns.html)
#     
# </font>
# </div>

# In[ ]:




