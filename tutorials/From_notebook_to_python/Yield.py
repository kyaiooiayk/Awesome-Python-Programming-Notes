#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Introduction" data-toc-modified-id="Introduction-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Introduction</a></span></li><li><span><a href="#What-is-Yield?" data-toc-modified-id="What-is-Yield?-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>What is Yield?</a></span></li><li><span><a href="#Case-with-no-yield" data-toc-modified-id="Case-with-no-yield-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Case with no yield</a></span></li><li><span><a href="#Case-with-yield" data-toc-modified-id="Case-with-yield-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>Case with yield</a></span></li><li><span><a href="#Another-example" data-toc-modified-id="Another-example-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>Another example</a></span></li><li><span><a href="#Approaches-to-overcome-generator-exhaustion" data-toc-modified-id="Approaches-to-overcome-generator-exhaustion-6"><span class="toc-item-num">6&nbsp;&nbsp;</span>Approaches to overcome generator exhaustion</a></span></li><li><span><a href="#Generator-are-memory-efficient" data-toc-modified-id="Generator-are-memory-efficient-7"><span class="toc-item-num">7&nbsp;&nbsp;</span>Generator are memory efficient</a></span></li><li><span><a href="#References" data-toc-modified-id="References-8"><span class="toc-item-num">8&nbsp;&nbsp;</span>References</a></span></li></ul></div>

# # Introduction

# <div class="alert alert-warning">
# <font color=black>
# 
# **What?** Yield
# 
# </font>
# </div>

# # What is Yield?

# <div class="alert alert-info">
# <font color=black>
# 
# - The `yield` keyword can turn any function into a generator object. 
# - Yields work like a standard `return` keyword.
# - When done so, the function instead of returning the output, it returns a generator that can be **iterated upon**. 
# 
# </font>
# </div>

# # Case with no yield

# In[1]:


def testgen_baseline(index):
    weekdays = ['sun','mon','tue','wed','thu','fri','sat']
    return weekdays[index]


# In[2]:


day = testgen_baseline(0)
print(day)
print(type(day))


# In[3]:


day = testgen_baseline(1)
print(day)
# Still print the same value as expected!
print(day)


# # Case with yield

# In[4]:


def testgen_with_yield(index):
    weekdays = ['sun','mon','tue','wed','thu','fri','sat']
    yield weekdays[index]
    yield weekdays[index+1]


# In[5]:


day = testgen_with_yield(0)
print(day)
print(type(day))


# <div class="alert alert-info">
# <font color=black>
# 
# - You can then iterate through the generator to extract items. 
# - Iterating is done using a `for loop` or simply using the `next()` function.
# 
# </font>
# </div>

# In[6]:


print(next(day), next(day))


# In[7]:


day = testgen_with_yield(0)
for i in day:
    print("=", i)


# In[8]:


day = testgen_with_yield(0)
for i in day:
    print("=", i, next(day))


# <div class="alert alert-info">
# <font color=black>
# 
# - **How do we explain the error below?**
# - Each time you iterate, Python runs the code **until** it encounters a yield statement inside the function. 
# - Then, it sends the yielded value and pauses the function in that state without exiting. 
# - When the function is invoked the next time, the **state** at which it was last paused is remembered and execution is continued from that point onwards. It means, any local variable you may have created inside the function before yield was called will be available the next time you invoke the function.
# - This continues until the generator is exhausted.
# 
# </font>
# </div>

# In[9]:


day = testgen_with_yield(0)
next(day)
for i in day:
    print("=", i)
    print(next(day))


# # Another example

# <div class="alert alert-info">
# <font color=black>
# 
# - Since the yield enables the function to remember its 'state', this function can be used to generate values in a logic defined by you. So, it function becomes a **generator**. 
# 
# </font>
# </div>

# In[10]:


def simple_generator():
    """
    We have defined a logic which goes like this:
    
    call me once and I will return 1
    cam me twice and I will return 2
    call me three times and I will return 3
    """
    x = 1
    yield x
    yield x + 1
    yield x + 2


# In[11]:


# Only generator. no code runs. no value gets returned
generator_object = simple_generator()
generator_object


# In[12]:


# Now you can iterate through the generator object. But it works only once.
for i in generator_object:
    print(i)


# In[13]:


# This will not print anything as the generator has exhasuted all the options and has to be re-initialised
for i in generator_object:
    print(i)


# # Approaches to overcome generator exhaustion

# <div class="alert alert-info">
# <font color=black>
# 
# -  To overcome generator exhaustion, you can:    
#     - **Approach 1**: Iterate by calling the function that created the generator in the first place
#     - **Approach 2** (best): Convert it to a class that implements a `__iter__()` method. This creates an iterator every time, so you don't have to worry about the generator getting exhausted.
# 
# </font>
# </div>

# **Approach No1**

# In[14]:


generator_object = simple_generator()
for i in generator_object:
    print(i)
generator_object = simple_generator()
for i in generator_object:
    print(i)    


# **Approach No2**

# In[15]:


class Iterable(object):
    """
    Creates an iterator object every time, 
    so you don't have to keep recreating the generator.
    """
    def __iter__(self):
        x = 1
        yield x
        yield x + 1
        yield x + 2


# In[16]:


# Instantiate the class once only!
iterable = Iterable()


# In[17]:


for i in iterable:  # iterator created here
    print(i)
for i in iterable:  # iterator created here
    print(i)    


# # Generator are memory efficient

# <div class="alert alert-info">
# <font color=black>
# 
# - Let's we want to iterate through al  list. If you do so, the content of the list occupies tangible memory as soon as you materialise it (you run the code and everythign get sent into the RAM). The larger the list gets, it occupies more memory resource. Generators are memory efficient because the values are not materialized **until called**. 
# 
# - But if there is a certain logic behind producing the items that you want, you **don't have** to store in a list. But rather, simply write a generator that will produce the items whenever you want them.
# 
# 
# - Let's say, you want to iterate through squares of numbers from 1 to 10. There are two ways:
#     - Create the list 
#     - Create a generator 
# 
# </font>
# </div>

# **Option No1 - create a list**

# In[18]:


import sys
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Size of a list", sys.getsizeof(my_list))
for i in my_list:
    print(i**2)


# **Option No2 - create a generator**

# In[19]:


def squares(x=0):
    
    while x < 10:        
        x = x + 1
        yield x*x
        print("size of x", sys.getsizeof(x))

for i in squares():
    print(i)


# # References

# <div class="alert alert-warning">
# <font color=black>
# 
# - https://codingcompiler.com/python-coding-interview-questions-answers/
# - https://www.machinelearningplus.com/python/what-does-yield-keyword-do/
# 
# </font>
# </div>
