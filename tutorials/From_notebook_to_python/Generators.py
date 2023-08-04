#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Introduction" data-toc-modified-id="Introduction-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Introduction</a></span></li><li><span><a href="#Generators" data-toc-modified-id="Generators-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Generators</a></span></li><li><span><a href="#Generator-Functions:-Using-yield" data-toc-modified-id="Generator-Functions:-Using-yield-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Generator Functions: Using yield</a></span></li><li><span><a href="#Only-the-first-element-is-evaluated-but-..." data-toc-modified-id="Only-the-first-element-is-evaluated-but-...-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>Only the first element is evaluated but ...</a></span></li><li><span><a href="#Be-aware-of-the-consuming-generator" data-toc-modified-id="Be-aware-of-the-consuming-generator-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>Be aware of the consuming generator</a></span></li><li><span><a href="#List-comprehension-vs.-generators" data-toc-modified-id="List-comprehension-vs.-generators-6"><span class="toc-item-num">6&nbsp;&nbsp;</span>List comprehension vs. generators</a></span></li><li><span><a href="#References" data-toc-modified-id="References-7"><span class="toc-item-num">7&nbsp;&nbsp;</span>References</a></span></li></ul></div>

# # Introduction
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-block alert-warning">
# <font color=black>
# 
# **What?** Generators
# 
# </font>
# </div>

# # Generators
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-info">
# <font color=black>
# 
# - List comprehensions and generator expressions are not the same thing.
# - List comprehensions use **square brackets**, while generator expressions use **parentheses**.
# - A list is a collection of values, while a generator is a recipe for producing values
# - When you create a list, you are actually building a collection of values, and there is some memory cost associated with that. When you create a generator, you are not building a collection of values, but a recipe for producing those values.
# - The difference is that a generator expression does not actually compute the values until they are needed. This not only leads to **memory efficiency**, but to computational efficiency as well! This also means that while the size of a list is limited by available memory, the size of a generator expression is unlimited!
# 
# </font>
# </div>

# In[1]:


# This is a list comprehension
[n ** 2 for n in range(12)]


# In[4]:


# This is a generator
(n ** 2 for n in range(12))


# In[5]:


# To print its content we have to turn it into a list
G = (n ** 2 for n in range(12))
print(list(G))


# In[8]:


# Both expose the same iterator interface, as we can see here:
L = [n ** 2 for n in range(12)]
for val in L:
    print(val, end=' ')

print("")
G = (n ** 2 for n in range(12))
for val in G:
    print(val, end=' ')


# <div class="alert alert-info">
# <font color=black>
# 
# - A list can be iterated multiple times; a generator expression is single-use 
# - One place there are very useful is when working with collections of data files on disk; it means that you can quite easily analyze them in batches, letting the generator keep track of which ones you have yet to see.
# 
# </font>
# </div>

# In[9]:


L = [n ** 2 for n in range(12)]
for val in L:
    print(val, end=' ')
print()

for val in L:
    print(val, end=' ')


# In[12]:


# A generator expression, on the other hand, is used-up after one iteration:
G = (n ** 2 for n in range(12))
list(G)


# In[13]:


list(G)


# In[12]:


# This can be very useful because it means iteration can be stopped and started:
G = (n**2 for n in range(12))
for n in G:
    print(n, end=' ')
    if n > 30: break

print("\ndoing something in between")

for n in G:
    print(n, end=' ')


# # Generator Functions: Using yield
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-info">
# <font color=black>
# 
# - A **generator function** is a function that, rather than using return to return a value once, uses yield to yield a (potentially infinite) sequence of values. 
# - Just as in generator expressions, the state of the generator is preserved between partial iterations, but if we want a fresh copy of the generator we can simply call the function again.
# 
# </font>
# </div>

# In[13]:


L1 = [n ** 2 for n in range(12)]

L2 = []
for n in range(12):
    L2.append(n ** 2)

print(L1)
print(L2)


# In[14]:


# Similarly, here we have two ways of constructing equivalent generators:    
G1 = (n ** 2 for n in range(12))
print(*G1)

def gen():
    for n in range(12):
        yield n ** 2

G2 = gen()

print(*G2)


# <div class="alert alert-info">
# <font color=black>
# 
# - A Python generator is an object that acts as an iterator: it’s an object you can use with the `for ... in` operator. 
# - Generators are built using the `yield` operator. 
# 
# </font>
# </div>

# In[2]:


def generator():
    i = 0
    while True:
        i += 1
        yield i


# In[3]:


for item in generator():
    print(item)
    if item > 4:
        break


# # Only the first element is evaluated but ...
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-info">
# <font color=black>
#     
# - The main reason why we love to use generators in certain cases (i.e., when we are dealing with large numbers of computations) is that it only computes the next value when it is needed, which is also known as "lazy" evaluation.
# - However, the first clause of an generator is already checked upon it's creation.
# - Certainly, this is a nice feature, since it notifies us about syntax erros immediately. 
# - **However**, this is not the case if we have multiple cases in our generator.
# 
# </font>
# </div>

# In[1]:


gen_fails = (i for i in 1/0)


# In[2]:


# Here there is an exta for so it would not be evaluate at creation
gen_succeeds = (i for i in range(5) for j in 1/0)


# In[3]:


# But obviously fails when we iterate
for i in gen_succeeds:
    print(i)


# # Be aware of the consuming generator
# <hr style="border:2px solid black"> </hr>

# In[4]:


gen = (i for i in range(5))
# Every time you call in you are using a __next__ call
print('2 in gen,', 2 in gen)
print('3 in gen,', 3 in gen)
print('1 in gen,', 1 in gen) 


# In[5]:


gen = (i for i in range(5))
# although it defeats the purpouse of the generators1
a_list = list(gen)
print('2 in l,', 2 in a_list)
print('3 in l,', 3 in a_list)
print('1 in l,', 1 in a_list) 


# # List comprehension vs. generators
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-info">
# <font color=black>
# 
# - List comprehensions are fast, but generators are faster! 
# - So what's the reason to prefer one over the other?
#     - use lists if you want to use the plethora of list methods  
#     - use generators when you are dealing with huge collections to avoid memory issues
# 
# </font>
# </div>

# In[5]:


def plainlist(n=100000):
    my_list = []
    for i in range(n):
        if i % 5 == 0:
            my_list.append(i)
    return my_list


def listcompr(n=100000):
    my_list = [i for i in range(n) if i % 5 == 0]
    return my_list


def generator(n=100000):
    my_gen = (i for i in range(n) if i % 5 == 0)
    return my_gen


def generator_yield(n=100000):
    for i in range(n):
        if i % 5 == 0:
            yield i


# In[6]:


get_ipython().run_line_magic('timeit', 'plainlist()')
get_ipython().run_line_magic('timeit', 'listcompr()')
get_ipython().run_line_magic('timeit', 'generator()')
get_ipython().run_line_magic('timeit', 'generator_yield()')


# <div class="alert alert-info">
# <font color=black>
# 
# - To be fair to the list, let us exhaust the generators!
# - In this case  there is no much difference.
#     
# </font>
# </div>

# In[7]:


def test_plainlist(plain_list):
    for i in plain_list():
        pass


def test_listcompr(listcompr):
    for i in listcompr():
        pass


def test_generator(generator):
    for i in generator():
        pass


def test_generator_yield(generator_yield):
    for i in generator_yield():
        pass


# In[8]:


print('plain_list:     ', end='')
get_ipython().run_line_magic('timeit', 'test_plainlist(plainlist)')
print('\nlistcompr:     ', end='')
get_ipython().run_line_magic('timeit', 'test_listcompr(listcompr)')
print('\ngenerator:     ', end='')
get_ipython().run_line_magic('timeit', 'test_generator(generator)')
print('\ngenerator_yield:     ', end='')
get_ipython().run_line_magic('timeit', 'test_generator_yield(generator_yield)')


# # References
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-block alert-warning">
# <font color=black>
# 
# - [Whirlwind Tour of Python](http://www.oreilly.com/programming/free/a-whirlwind-tour-of-python.csp)
# - https://nbviewer.org/github/rasbt/python_reference/blob/master/tutorials/not_so_obvious_python_stuff.ipynb?create=1
#     
# </font>
# </div>
