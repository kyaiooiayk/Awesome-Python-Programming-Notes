#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Introduction" data-toc-modified-id="Introduction-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Introduction</a></span></li><li><span><a href="#History" data-toc-modified-id="History-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>History</a></span></li><li><span><a href="#Decorators" data-toc-modified-id="Decorators-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Decorators</a></span></li><li><span><a href="#References" data-toc-modified-id="References-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>References</a></span></li></ul></div>

# # Introduction
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-warning">
# <font color=black>
# 
# **What?** First class functions
# 
# </font>
# </div>

# # History
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
# 
# - Everything is a class in Python. Guido van Rossum has designed the language according to the principle "first-class everything". He wrote: "One of my goals for Python was to make it so that all objects were "first class." By this, I meant that I wanted all objects that could be named in the language (e.g., integers, strings, functions, classes, modules, methods, and so on) to have equal status. That is, they can be assigned to variables, placed in lists, stored in dictionaries, passed as arguments, and so forth.
# - In other words, "everything" is treated the same way, everything is a class: functions and methods are values just like lists, integers or floats. Each of these are instances of their corresponding classes.
#     
# </font>
# </div>

# # Decorators
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-info">
# <font color=black>
# 
# - In python, functions are `First class functions` allow us to treat functions like any other object, so for example: we can pass functions as arguments to another function, return functions and we can assign functions to variables. 
# - `Closures` allows us to take advantage of `First class functions` that returns an inner function that remembers and has access to variables local to the scope in which they were created.
# 
# </font>
# </div>

# In[1]:


# we can assign functions to variables
def greet(name):
    return 'Hello ' + name


greet_someone = greet
print(greet_someone('John'))


# we can define functions inside other functions
def greet(name):
    def get_message():
        return 'Hello '

    result = get_message() + name
    return result


print(greet('John'))


# functions can be passed as parameters to other functions
def greet(name):
    return 'Hello ' + name


def call_func(func):
    other_name = 'John'
    return func(other_name)


print(call_func(greet))


# functions can return other functions
def compose_greet_func():
    def get_message():
        return 'Hello John'

    return get_message


greet = compose_greet_func()
print(greet())


# scoping, access the inner functions.
# note that python only allows read access to the outer scope and not assignment
def compose_greet_func(name):
    def get_message():
        return 'Hello ' + name

    return get_message


greet = compose_greet_func('John')
print(greet())


# # References
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-block alert-warning">
# <font color=black>
# 
# - [Blog: Guide to python function decorators](http://thecodeship.com/patterns/guide-to-python-function-decorators/)
# - [Youtube: Decorators - Dynamically Alter The Functionality Of Your Functions](https://www.youtube.com/watch?v=FsAPt_9Bf3U)
# - http://nbviewer.jupyter.org/github/ethen8181/machine-learning/blob/master/python/decorators/decorators.ipynb
# - [Youtube: Programming Terms: First-Class Functions](https://www.youtube.com/watch?v=kr0mpwqttM0&feature=cards&src_vid=swU3c34d2NQ&annotation_id=98878b78-dceb-4942-8d49-bcbed34e5263).
# - https://python-course.eu/oop/object-oriented-programming.php
#     
# </font>
# </div>

# In[ ]:




