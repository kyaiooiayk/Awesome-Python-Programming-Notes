#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Introduction" data-toc-modified-id="Introduction-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Introduction</a></span></li><li><span><a href="#The-link-with-functional-programming" data-toc-modified-id="The-link-with-functional-programming-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>The link with functional programming</a></span></li><li><span><a href="#What-is-a-lambda-function?" data-toc-modified-id="What-is-a-lambda-function?-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>What is a <code>lambda</code> function?</a></span></li><li><span><a href="#map-function" data-toc-modified-id="map-function-4"><span class="toc-item-num">4&nbsp;&nbsp;</span><code>map</code> function</a></span><ul class="toc-item"><li><span><a href="#Map-vs.-list-comprehension" data-toc-modified-id="Map-vs.-list-comprehension-4.1"><span class="toc-item-num">4.1&nbsp;&nbsp;</span><code>Map</code> vs. list comprehension</a></span></li></ul></li><li><span><a href="#filter-function" data-toc-modified-id="filter-function-5"><span class="toc-item-num">5&nbsp;&nbsp;</span><code>filter</code> function</a></span><ul class="toc-item"><li><span><a href="#filter-vs.-list-comprehension" data-toc-modified-id="filter-vs.-list-comprehension-5.1"><span class="toc-item-num">5.1&nbsp;&nbsp;</span><code>filter</code> vs. list comprehension</a></span></li></ul></li><li><span><a href="#reduce" data-toc-modified-id="reduce-6"><span class="toc-item-num">6&nbsp;&nbsp;</span><code>reduce</code></a></span><ul class="toc-item"><li><span><a href="#reduce-vs.-list-comprehension" data-toc-modified-id="reduce-vs.-list-comprehension-6.1"><span class="toc-item-num">6.1&nbsp;&nbsp;</span><code>reduce</code> vs. list comprehension</a></span></li></ul></li><li><span><a href="#References" data-toc-modified-id="References-7"><span class="toc-item-num">7&nbsp;&nbsp;</span>References</a></span></li></ul></div>

# # Introduction
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-block alert-warning">
# <font color=black>
# 
# **What?** Lambda, map and filter functions
# 
# </font>
# </div>

# # The link with functional programming
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
# 
# - `map`, `filter` and `reduce` are all example of functional programming in python.
# - **Definition #1** style of programming in which functions are treated and manipulated as objects, i.e. functions can be assigned to variables, they can be passed as arguments, and they can be stored in containers along with other data. We can write parallel code that works by running lots of functions in parallel on large amounts of data.
# - **Definition #2** when you build your applications completely out of pure functions. Pure Function: Its return value is determined exclusively by it's arguments.
# 
# - **Why would you want to use them?** It’s much simpler, it improves maintainability, we can define extremely complex functions easily, it provides modularity and is shorter. It makes parallelisation much easier. 
#     
# </font>
# </div>

# # What is a `lambda` function?
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-block alert-info">
# <font color=black>
# 
# - `lambda` returns a function object which can be assigned to any variable.
# - `lambda` functions are passed as parameters to functions that expect function object as parameters such as `map`, `reduce`, and `filter` functions. So, you will often see `lambda` used in combination with those functions.
# - Lambda functions are single-expression  functions that **are not necessarily** bound to a name (they can be anonymous). 
# - Lambda functions can't use regular Python statements and always include an implicit `return` statement.
# 
# </font>
# </div>

# In[1]:


# Can we achieve something like this in a different way?
def add(x, y):
    return x + y


# In[2]:


lambda x, y: x + y


# In[3]:


add = lambda x, y: x + y
add(1, 2)


# In[4]:


# The same type is being printed here as well
add


# <div class="alert alert-block alert-info">
# <font color=black>
# 
# - **So why would you ever want to use such a thing?** Primarily, it comes down to the fact that *everything is an object* in Python, even functions themselves!
# - That means that functions can be passed as arguments to functions.
# - As an example of this, suppose we have some data stored in a list of dictionaries:
#     
# 
# </font>
# </div>    

# In[5]:


data = [{'first':'Guido', 'last':'Van Rossum', 'YOB':1956},
        {'first':'Grace', 'last':'Hopper',     'YOB':1906},
        {'first':'Alan',  'last':'Turing',     'YOB':1912}]


# In[6]:


data[0]["first"]


# Now suppose we want to sort this data.
# Python has a ``sorted`` function that does this:

# In[7]:


sorted([2,4,3,5,1,6])


# <div class="alert alert-block alert-info">
# <font color=black>
# 
# - But dictionaries are not orderable: we need a way to tell the function *how* to sort our data.
# - We can do this by specifying the ``key`` function, a function which given an item returns the sorting key for that item: 
# 
# </font>
# </div>

# In[8]:


# sort alphabetically by first name
sorted(data, key = lambda item: item['first'])


# In[9]:


# sort by year of birth
sorted(data, key = lambda item: item['YOB'])


# # `map` function
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-block alert-info">
# <font color=black>
# 
# - `map()` is a built-in function that allows you to process and transform all the items in an iterable without using an explicit for loop.
# - This technique is called **mapping**, hence the name.
# - `map()` is useful when you need to apply a transformation function to each item in an iterable and transform them **into a new iterable**.
# - `map()` is one of the tools that support a functional programming style in Python.
# - The structure is the following: `map(function_object, iterable1, iterable2, ....)`
# 
# </font>
# </div>

# In[10]:


def multiplyByTwo(x):
    return x*2


# In[11]:


# Return another iterable
map(multiplyByTwo, [1,2,3,4])


# In[12]:


# Check if it really returns an iterable
hasattr(map(multiplyByTwo, [1,2,3,4]), '__iter__')


# In[13]:


list(map(multiplyByTwo, [1,2,3,4]))


# In[14]:


list(map(multiplyByTwo, [[1,2,3,4], [5,6,7,8]]))


# In[15]:


# We can made the whole thing much shorter
list(map(lambda x:x*2, [1,2,3,4]))


# In[16]:


a = [1, 2]
b = [2, 3]
list(map(multiplyByTwo, [a, b]))


# ## `Map` vs. list comprehension

# <div class="alert alert-block alert-info">
# <font color=black>
# 
# - It seems to be a matter of preferences, and under certain conditions this is the case.
# - Here, we'd like to go a little deeper into the comparison.
# Specifically, we will look at three scenarios: 
#     - list comprehensions
#     - `map()` with a predefined input function
#     - `map()` with an ad-hoc lambda function.
# </font>
# </div>

# In[2]:


# Definie an input list
lst = list(range(1000000))


# In[4]:


# list comprehension
get_ipython().run_line_magic('timeit', '-r 10 -n 10 [i / 0.939276 for i in lst]')


# In[5]:


# predefined conversion function
def eur_to_usd(x):
    return x / 0.939276


# In[7]:


# map with predefined input function
get_ipython().run_line_magic('timeit', '-r 10 -n 10 list(map(eur_to_usd, lst))')


# In[8]:


# map with lambda function
get_ipython().run_line_magic('timeit', '-r 10 -n 10 list(map(lambda x: x / 0.939276, lst))')


# <div class="alert alert-block alert-info">
# <font color=black>
# 
# - **Simplicity and readability**: the list comprehension appears to be winning the race here. The programmer’s intention is immediately apparent and there’s no need to include any extra keywords or define additional functions. However, it’s worth noting that for more complex operations, separate transformation functions may need to be defined, which would take away some of the brownie points that list comprehensions generally receive for their readability.
# 
# - **Performance**: list comprehensions are fastest, followed by `map()` with a predefined input function, and lastly `map()` with a `lambda` function. A `lambda` function gets called for each item in the input list, resulting in a computational overhead due to the creation and destruction of `lambda` function objects. Predefined functions, by contrast, are optimised and stored in memory, which leads to more efficient execution.
# 
# </font>
# </div>

# # `filter` function
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-block alert-info">
# <font color=black>
# 
# - The `filter()` function expects two arguments: function_object and an iterable. 
# - function_object returns a boolean value and is called for each element of the iterable. 
# - `filter()` returns only those elements for which the function_object returns `True`.
# - Like the `map()` function, the `filter()` function also returns a list of elements.
# - Unlike `map()`, the `filter()` function can only have **one** iterable as input.
# 
# </font>
# </div>

# In[17]:


list_a = [1, 2, 3, 4, 5]


# In[18]:


# This is a quick way to know if it is iterable
iter(list_a)


# In[19]:


filterObject = filter(lambda x: x%2 == 0.0, list_a)
# This returns an object
print(filterObject)


# In[20]:


# To get the list use list
filterObject = list(filterObject)
print(filterObject)


# In[21]:


# This is what happens if I do not use filter
filterObject = lambda x: x%2 == 0.0, list_a
even_num = list(filterObject)
print(even_num)


# ## `filter` vs. list comprehension

# <div class="alert alert-block alert-info">
# <font color=black>
# 
# - It seems to be a matter of preferences, and under certain conditions this is the case.
# - Here, we'd like to go a little deeper into the comparison.
# Specifically, we will look at three scenarios: 
#     - list comprehensions
#     - `filter()` with a predefined input function
#     - `filter()` with an ad-hoc lambda function.
# </font>
# </div>

# In[11]:


# Create an input list
lst = list(range(1000000))


# In[12]:


# List comprehension
get_ipython().run_line_magic('timeit', '-r 10 -n 10 [i for i in lst if i % 2 == 0]')


# In[13]:


# Predefined filter function
def fil(x):
    if x % 2 == 0:
        return True
    else:
        return False


# In[14]:


# Filter with predefined filter function
get_ipython().run_line_magic('timeit', '-r 10 -n 10 list(filter(fil, lst))')


# In[16]:


# Filter with lambda function
get_ipython().run_line_magic('timeit', '-r 10 -n 10 list(filter(lambda x: x % 2 == 0, lst))')


# <div class="alert alert-block alert-info">
# <font color=black>
# 
# - **Readability** seems to be draw! List comprehensions are pretty easy to read and don’t require any predefined or ad-hoc functions or extra keywords. However, it has been argued that the use of the function filter() immediately gives away the programmer’s intent of, well, filtering something, perhaps more so than the list comprehension does. This is of course a highly subjective matter and will depend on the individual’s preferences and tastes.
# - **Performance**: list comprehensions are fastest, followed by filter() with a predefined filter function, and filter() with an ad-hoc lambda function comes in last. The reasons for this are the same mentioned for `map`.
#     
# </font>
# </div>

# # `reduce`
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-block alert-info">
# <font color=black>
# 
# - `reduce()` function doesn’t return a new sequence like `map()` and `filter()`. Instead, it returns a single value. The syntax is similar to the other two functions: `reduce(function, iterable)`
# - `reduce()` applies the function to the elements of the sequence, from left to right, starting with the first two elements in the sequence.
# - We combine the result of applying the function to the sequence’s first two elements with the third element and pass them to another call of the same function.
# - This process repeats until we reach the end of the iterable and the iterable reduces to a single value. 
# 
# </font>
# </div>

# In[12]:


from functools import reduce

nums = [1, 3, 4, 1]
# (((1*3)*4)*)1
reduce(lambda x, y: x*y, nums)


# # References
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-block alert-warning">
# <font color=black>
# 
# - [Whirlwind Tour of Python](http://www.oreilly.com/programming/free/a-whirlwind-tour-of-python.csp)
# - https://medium.com/better-programming/lambda-map-and-filter-in-python-4935f248593 
# - [Python's `map()`: Processing Iterables Without a Loop](https://realpython.com/python-map-function/)
# - [`map` vs. `reduce`](https://www.udacity.com/blog/2020/12/our-guide-to-map-filter-and-reduce-functions-in-python.html)
# - [Comparing List Comprehensions vs. Built-In Functions in Python: Which Is Better?](https://towardsdatascience.com/comparing-list-comprehensions-vs-built-in-functions-in-python-which-is-better-1e2c9646fafe)
#     
# </font>
# </div>

# In[ ]:




