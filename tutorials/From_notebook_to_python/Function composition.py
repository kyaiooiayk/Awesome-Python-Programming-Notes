#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Introduction" data-toc-modified-id="Introduction-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Introduction</a></span></li><li><span><a href="#What-is-function-composition?" data-toc-modified-id="What-is-function-composition?-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>What is function composition?</a></span></li><li><span><a href="#Examples-#1---naive-implementation" data-toc-modified-id="Examples-#1---naive-implementation-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Examples #1 - naive implementation</a></span></li><li><span><a href="#Example-#2---with-lambda-function" data-toc-modified-id="Example-#2---with-lambda-function-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>Example #2 - <code>with lambda</code> function</a></span></li><li><span><a href="#Example-#3---adding-any-number-of-functions" data-toc-modified-id="Example-#3---adding-any-number-of-functions-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>Example #3 - adding any number of functions</a></span></li><li><span><a href="#Example-#4---with-reduce-function" data-toc-modified-id="Example-#4---with-reduce-function-6"><span class="toc-item-num">6&nbsp;&nbsp;</span>Example #4 - with <code>reduce</code> function</a></span></li><li><span><a href="#References" data-toc-modified-id="References-7"><span class="toc-item-num">7&nbsp;&nbsp;</span>References</a></span></li></ul></div>

# # Introduction
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-warning">
# <font color=black>
# 
# **What?** Function composition
# 
# </font>
# </div>

# # What is function composition?
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
# 
# - Function composition is the way of combining two or more functions in such a way that the output of one function becomes the input of the second function and so on. 
# - For example, let there be two functions `F` and `G` and their composition can be represented as `F(G(x))` where `x` is the argument and output of `G(x)` function will become the input of `F`.
# </font>
# </div>

# # Examples #1 - naive implementation
# <hr style = "border:2px solid black" ></hr>

# In[2]:


def add_two(x):
    return x + 2


def multiply_by_two(x):
    return x * 2


print("Adding 2 to 5 and multiplying the result with 2: ",
      multiply_by_two(add_two(5)))


# # Example #2 - `with lambda` function
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-block alert-info">
# <font color=black>
# 
# - There is a more python (and hence elegant) solution to this which makes use of `lambda` function.
# - `lambda` returns a function object which can be assigned to any variable.
# - `lambda` functions are passed as parameters to functions that expect function object as parameters such as `map`, `reduce`, and `filter` functions. 
# - Lambda functions are single-expression  functions that **are not necessarily** bound to a name (they can be anonymous). 
# - Lambda functions can't use regular Python statements and always include an implicit `return` statement.
# 
# </font>
# </div>

# In[3]:


def composite_function(f, g):
    return lambda x: f(g(x))


# Composite function returns
# a lambda function. Here add_multiply
# will store lambda x : multiply(add(x))
add_multiply = composite_function(multiply_by_two, add_two)

print("Adding 2 to 5 and multiplying the result with 2: ", add_multiply(5))


# # Example #3 - adding any number of functions
# <hr style = "border:2px solid black" ></hr>

# In[5]:


def subtract_one(x):
    return x - 1


add_subtract_multiply = composite_function(
    composite_function(multiply_by_two, subtract_one), add_two)


print("Adding 2 to 5, then subtracting 1 and multiplying the result with 2: ",
      add_subtract_multiply(5))


# # Example #4 - with `reduce` function
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
# 
# - `reduce` is a tool that is typically associated with functional programming, which is a programming paradigm. 
# 
# - In a short sentence, reduce takes an iterable and a binary function (a function that takes two arguments), and then uses that binary function to boil the iterable down to a single value.
# 
# - A concrete example is the function `sum` which is a reduction. 
# 
# - Keep in mind that part of what a reduction does is taking an iterable and reducing it to a single value. 
#     
# </font>
# </div>

# In[8]:


# importing reduce() from functools
from functools import reduce


def composite_function(*func):

    def compose(f, g):
        return lambda x: f(g(x))

    return reduce(compose, func, lambda x: x)


add_subtract_multiply = composite_function(multiply_by_two,
                                           subtract_one,
                                           add_two)

print("Adding 2 to 5, then subtracting 1 and multiplying the result with 2: ",
      add_subtract_multiply(5))


# In[ ]:





# # References
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-warning">
# <font color=black>
# 
# - https://www.geeksforgeeks.org/function-composition-in-python/
#     
# </font>
# </div>

# In[ ]:




