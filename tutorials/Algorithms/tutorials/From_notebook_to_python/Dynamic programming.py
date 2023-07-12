#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Introduction" data-toc-modified-id="Introduction-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Introduction</a></span></li><li><span><a href="#What-is-dynamic-programming?" data-toc-modified-id="What-is-dynamic-programming?-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>What is dynamic programming?</a></span></li><li><span><a href="#Fibonacci-series" data-toc-modified-id="Fibonacci-series-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Fibonacci series</a></span></li><li><span><a href="#Fibonacci-solved-with-recursion" data-toc-modified-id="Fibonacci-solved-with-recursion-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>Fibonacci solved with recursion</a></span></li><li><span><a href="#Fibonacci-solved-with-dynamic-programming" data-toc-modified-id="Fibonacci-solved-with-dynamic-programming-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>Fibonacci solved with dynamic programming</a></span></li><li><span><a href="#References" data-toc-modified-id="References-6"><span class="toc-item-num">6&nbsp;&nbsp;</span>References</a></span></li></ul></div>

# # Introduction
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-warning">
# <font color=black>
#
# **What?** Dynamic programming
#
# </font>
# </div>

# # What is dynamic programming?
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-block alert-info">
# <font color=black>
#
# - Dynamic Programming is a powerful technique that allows one to solve many different types of problems in time `O(n^2)` or `O(n^3)` for which a naive approach would take **exponential time**.
# - Dynamic Programming is mainly an optimisation strategy over plain recursion. Wherever we see a recursive solution that has repeated calls for same inputs, we can optimise it using dynamic programming.
# - The idea is to simply store the results of subproblems, so that we do not have to re-compute them when needed later.
# - This simple optimisation reduces time complexity from exponential to polynomial.
#
# </font>
# </div>

# # Fibonacci series
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-block alert-info">
# <font color=black>
#
# - The Fibonacci numbers are the numbers in the following integer sequence: `0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ……`
# - The sequence Fn of Fibonacci numbers is defined by the recurrence relation: `Fn = Fn-1 + Fn-2` with seed values
# `F0 = 0` and `F1 = 1`.
#
# </font>
# </div>

# # Fibonacci solved with recursion
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-block alert-info">
# <font color=black>
#
# - Recursion has exponential time complexity as every function calls two other functions.
#
# </font>
# </div>

# In[1]:


def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


# In[2]:


n = 20
print(fibonacci(n))


# # Fibonacci solved with dynamic programming
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-block alert-info">
# <font color=black>
#
# - We can avoid the repeated work done in method 1 by storing the Fibonacci numbers calculated so far.
# - In dynamic programming, if we optimise the call by storing solutions of subproblems, time complexity reduces to linear.
#
# </font>
# </div>

# In[3]:


def fibonacci(n):
    # Taking 1st two fibonacci numbers as 0 and 1
    f = [0, 1]

    for i in range(2, n + 1):
        f.append(f[i - 1] + f[i - 2])
    return f[n]


# In[4]:


print(fibonacci(20))


# # References
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-warning">
# <font color=black>
#
# - https://www.geeksforgeeks.org/dynamic-programming/?ref=ghm
#
# </font>
# </div>

# In[ ]:
