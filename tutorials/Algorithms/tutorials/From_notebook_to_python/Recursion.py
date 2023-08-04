#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Introduction" data-toc-modified-id="Introduction-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Introduction</a></span></li><li><span><a href="#What-is-a-recursion?" data-toc-modified-id="What-is-a-recursion?-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>What is a recursion?</a></span></li><li><span><a href="#Depth-first-versus-breadth-first" data-toc-modified-id="Depth-first-versus-breadth-first-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Depth-first versus breadth-first</a></span></li><li><span><a href="#Watch-out-for-RecursionError" data-toc-modified-id="Watch-out-for-RecursionError-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>Watch out for <code>RecursionError</code></a></span></li><li><span><a href="#Problem-#1" data-toc-modified-id="Problem-#1-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>Problem #1</a></span></li><li><span><a href="#Problem-#2" data-toc-modified-id="Problem-#2-6"><span class="toc-item-num">6&nbsp;&nbsp;</span>Problem #2</a></span></li><li><span><a href="#Problem-#3" data-toc-modified-id="Problem-#3-7"><span class="toc-item-num">7&nbsp;&nbsp;</span>Problem #3</a></span></li><li><span><a href="#Conclusions" data-toc-modified-id="Conclusions-8"><span class="toc-item-num">8&nbsp;&nbsp;</span>Conclusions</a></span></li><li><span><a href="#References" data-toc-modified-id="References-9"><span class="toc-item-num">9&nbsp;&nbsp;</span>References</a></span></li></ul></div>

# # Introduction
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-warning">
# <font color=black>
# 
# **What?** Recursion
# 
# </font>
# </div>

# # What is a recursion?
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-info">
# <font color=black>
# 
# - Recursion is the process of defining something in terms of itself.
# - Being more specific, recursion must have three elements:
#     - It must have a **base case** which is the condition to stop the recursion.
#     - It must have a **recursive case** which is the part where the function call itself recursively.
#     - It must change it's state and move towards the base case
#     
# </font>
# </div>
# 

# ![image.png](attachment:image.png)

# In[ ]:


def factorial(x):
    if x == 1:  # This is the base case
        return 1

    else:  # This is the recursive case
        return(x * factorial(x-1))


print(factorial(4))


# # Depth-first versus breadth-first
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-info">
# <font color=black>
# 
# - Keep in mind that recursive solutions are **inherently depth-first** in nature, whereas your problem might warrant a breadth-first solution.
# - Depth-First Search (DFS) means that when you are traversing some structure, you prioritise exploring in depth, and only then you look around, whereas in Breadth-First Search (BFS) you first explore the level you are at, and only then go a level deeper.
# - [Breadth-first search](https://en.wikipedia.org/wiki/Breadth-first_search)
# 
# </font>
# </div>

# # Watch out for `RecursionError`
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
# 
# - The recursion depth limit is something that makes your code raise a RecursionError if you make too many
# recursive calls. 
# - In many cases, this limit helps, because it helps you find recursive functions for which you did not define the base case properly.
# There are, however, cases in which the default recursive calls isn’t enough to finish your computations. A
# - By default Python does not allow us to make sufficient recursive calls. 
# - You can always set your own recursion depth with `sys.setrecursionlimit()`.
# - **Careful!** You are likely not to be interested in having Python run out of memory because you set a very large amount of recursive calls.
# 
# </font>
# </div>

# In[18]:


def f(i):
    i+=1
    print(i)
    return f(i)


# In[19]:


f(0)


# In[21]:


import sys
sys.setrecursionlimit(4000)
f(0)


# # Problem #1
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-info">
# <font color=black>
# 
# - First problem: convert an integer to a string in any Base. 
# 
# </font>
# </div>

# In[4]:


def to_str(n, base):
    convert_str = '0123456789ABCDEF'
    if n < base:
        """
        look up the string representation if it's smaller 
        than the base
        """
        return convert_str[n]
    else:
        """
        convert_str comes after to to_str method so that it will
        delayed the addition until the recursive call finishes
        """
        return to_str(n // base, base) + convert_str[n % base]


# In[5]:


print(to_str(769, 10))


# In[6]:


print(to_str(1, 2))


# In[7]:


print(to_str(2, 2))


# # Problem #2
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-info">
# <font color=black>
# 
# - **Fibonacci sequence**.
# - A Fibonacci sequence is the integer sequence of `0, 1, 1, 2, 3, 5, 8...`
# - The first two terms are `0` and `1`. 
# - All other terms are obtained by adding the preceding two terms.
# - This means to say the nth term is the sum of `(n-1)th` and `(n-2)th` terms.
# 
# </font>
# </div>

# In[30]:


def rec_fib(num):
    if num < 2:
        print("start")
        return num
    else:
        """
        3 = 2+1
        """
        print(num-1, num-2)
        return (rec_fib(num-1)+rec_fib(num-2))


for i in range(5):
    print("\nsending", i)
    print("ouput", rec_fib(i))


# # Problem #3
# <hr style="border:2px solid black"> </hr>

# ![image.png](attachment:image.png)

# In[1]:


def factorial(x):
    """This is a recursive function
    to find the factorial of an integer"""

    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))


# In[2]:


num = 3
print("The factorial of", num, "is", factorial(num))


# # Conclusions
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-danger">
# <font color=black>
# 
# - **Advantages of Recursion**
#     - Recursive functions make the code look clean and elegant.
#     - A complex task can be broken down into simpler sub-problems using recursion.
#     - Sequence generation is easier with recursion than using some nested iteration.
# 
# - **Disadvantages of Recursion**
#     - Sometimes the logic behind recursion is hard to follow through.
#     - Recursive calls are expensive (inefficient) as they take up a lot of memory and time.
#     - Recursive functions are hard to debug.
# 
# </font>
# </div>

# # References
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-warning">
# <font color=black>
# 
# - https://github.com/ethen8181/machine-learning/blob/master/python/algorithms/recursion.ipynb
# - http://interactivepython.org/runestone/static/pythonds/Recursion/toctree.html
# - https://stackoverflow.com/questions/494594/how-to-write-the-fibonacci-sequence
# - https://mathspp.com/blog/pydonts 
# - https://www.programiz.com/python-programming/recursion
#     
# </font>
# </div>
