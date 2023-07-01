#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Introduction" data-toc-modified-id="Introduction-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Introduction</a></span></li><li><span><a href="#Imports" data-toc-modified-id="Imports-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Imports</a></span></li><li><span><a href="#itertools" data-toc-modified-id="itertools-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>itertools</a></span></li><li><span><a href="#Example-#1" data-toc-modified-id="Example-#1-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>Example #1</a></span></li><li><span><a href="#Example-#2" data-toc-modified-id="Example-#2-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>Example #2</a></span></li><li><span><a href="#Example-#3" data-toc-modified-id="Example-#3-6"><span class="toc-item-num">6&nbsp;&nbsp;</span>Example #3</a></span></li><li><span><a href="#References" data-toc-modified-id="References-7"><span class="toc-item-num">7&nbsp;&nbsp;</span>References</a></span></li></ul></div>

# # Introduction
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-warning">
# <font color=black>
# 
# **What?** itertools
# 
# </font>
# </div>

# # Imports
# <hr style = "border:2px solid black" ></hr>

# In[1]:


from itertools import product, chain, combinations


# # itertools
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
# 
# - `itertools ` is a module implements a number of iterator building blocks inspired by constructs from APL, Haskell, and SML. Each has been recast in a form suitable for Python.
# 
# - The module standardizes a core set of fast, memory efficient tools that are useful by themselves or in combination. Together, they form an “iterator algebra” making it possible to construct specialized tools succinctly and efficiently in pure Python.
# 
# </font>
# </div>

# # Example #1
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
# 
# - Implement the IceCreamMachine's scoops method so that it returns all combinations of one ingredient and one topping. 
# 
# - If there are no ingredients or toppings, the method should return an empty list.
# For example: `IceCreamMachine(["vanilla", "chocolate"], ["chocolate sauce"]).scoops()` should return `[['vanilla', 'chocolate sauce'], ['chocolate', 'chocolate sauce']]`
# 
# 
# </font>
# </div>

# In[2]:


class IceCreamMachine:

    def __init__(self, ingredients, toppings):
        self.ingredients = ingredients
        self.toppings = toppings

    def scoops(self):
        return [list(p) for p in product(self.ingredients, self.toppings)]


# In[3]:


machine = IceCreamMachine(["vanilla", "chocolate"], ["chocolate sauce"])
# should print[['vanilla', 'chocolate sauce'], ['chocolate', 'chocolate sauce']]
print(machine.scoops())


# # Example #2
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
# 
# - Implement the unique_names method. When passed two arrays of names, it will return an array containing the names that appear in either or both arrays.
# - The returned array should have no duplicates.
# - For example, `calling unique_names(['Ava', 'Emma', 'Olivia'], ['Olivia', 'Sophia', 'Emma'])` should return an array containing Ava, Emma, Olivia, and Sophia in any order.
# 
# </font>
# </div>

# In[4]:


def unique_names(names1, names2):
    return list(set(chain(names1, names2)))

names1 = ["Ava", "Emma", "Olivia"]
names2 = ["Olivia", "Sophia", "Emma"]
print(unique_names(names1, names2))  # should print Ava, Emma, Olivia, Sophia


# # Example #3
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
# 
# - To be completed in **30 min**
# 
# - Write a function that, when passed a list and a target sum, returns, efficiently with respect to time used, two distinct zero-based indices of any two of the numbers, whose sum is equal to the target sum. 
# 
# - If there are no two numbers, the function should return None.
# 
# - For example, find_two_sum([3, 1, 5, 7, 5, 9], 10) should return a single tuple containing any of the following pairs of indices:
# 
# ```
# * 0 and 3 (or 3 and 0) as 3 + 7 = 10
# * 1 and 5 (or 5 and 1) as 1 + 9 = 10
# * 2 and 4 (or 4 and 2) as 5 + 5 = 10
# ```
# 
# </font>
# </div>

# In[2]:


def find_two_sum(numbers, target_sum):
    # :param numbers: (list of ints) The list of numbers.
    # :param target_sum: (int) The required target sum.
    # :returns: (a tuple of 2 ints) The indices of the two elements whose sum is equal to target_sum
    
    
    #print(list(combinations(numbers,2)))
    for duo in list(combinations(numbers,2)):
        if sum(duo) == target_sum:
            #print(duo, duo[0], duo[1], numbers.index(duo[0]), numbers.index(duo[1]))
            # the task said any, so I will return the first one I find!
            return (numbers.index(duo[0]), numbers.index(duo[1]))


print(find_two_sum([3, 1, 5, 7, 5, 9], 10))


# # References
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-warning">
# <font color=black>
# 
# - [TestDome home page](https://www.testdome.com/tests/python-online-test/45)
# - [elegant solution](https://github.com/jozo/testdome-python-solutions/blob/master/02_ice_cream_machine.py)
# - [`itertools`](https://docs.python.org/3/library/itertools.html)
# 
# </font>
# </div>

# In[ ]:




