#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Introduction" data-toc-modified-id="Introduction-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Introduction</a></span></li><li><span><a href="#What-constitute-an-efficient-algorithm?" data-toc-modified-id="What-constitute-an-efficient-algorithm?-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>What constitute an efficient algorithm?</a></span></li><li><span><a href="#Space-complexity" data-toc-modified-id="Space-complexity-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Space complexity</a></span></li><li><span><a href="#Time-complexity" data-toc-modified-id="Time-complexity-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>Time complexity</a></span></li><li><span><a href="#Asymptotic-analysis" data-toc-modified-id="Asymptotic-analysis-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>Asymptotic analysis</a></span></li><li><span><a href="#Best,-Worst,-and-Average-Cases" data-toc-modified-id="Best,-Worst,-and-Average-Cases-6"><span class="toc-item-num">6&nbsp;&nbsp;</span>Best, Worst, and Average Cases</a></span></li><li><span><a href="#Asymptotic-notation" data-toc-modified-id="Asymptotic-notation-7"><span class="toc-item-num">7&nbsp;&nbsp;</span>Asymptotic notation</a></span><ul class="toc-item"><li><span><a href="#Ω-(Big-Omega)-Notation-definition" data-toc-modified-id="Ω-(Big-Omega)-Notation-definition-7.1"><span class="toc-item-num">7.1&nbsp;&nbsp;</span>Ω (Big-Omega) Notation definition</a></span></li><li><span><a href="#O-(Big-O)-Notation-definition" data-toc-modified-id="O-(Big-O)-Notation-definition-7.2"><span class="toc-item-num">7.2&nbsp;&nbsp;</span>O (Big-O) Notation definition</a></span></li><li><span><a href="#Θ-(Big-Theta)-Notation-definition" data-toc-modified-id="Θ-(Big-Theta)-Notation-definition-7.3"><span class="toc-item-num">7.3&nbsp;&nbsp;</span>Θ (Big-Theta) Notation definition</a></span></li></ul></li><li><span><a href="#References" data-toc-modified-id="References-8"><span class="toc-item-num">8&nbsp;&nbsp;</span>References</a></span></li></ul></div>

# # Introduction
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-warning">
# <font color=black>
#
# **What?** Time and space complexity
#
# </font>
# </div>

# # What constitute an efficient algorithm?
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-info">
# <font color=black>
#
# - Algorithm’s efficiency measures both the time and space (memory) it takes when executed.
# - The **best algorithm** = least amount of time + least amount of space.
# - **Rreality** is that algorithms have a **tradeoff** between saving space or time.
# - Admiting there is ia tradeoff means that:
#     - The best algorithm **depends** on our requirements.
#     - If need both least time and memory we can settle for the average.
#
# </font>
# </div>

# # Space complexity
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-info">
# <font color=black>
#
# - Space complexity of an algorithm is the amount of space it uses for execution in relation to the size of the input. The keyword here is **in relation to the iput size**.
#
# - Assume that adding a single integer to the list takes `c` amout of space and other initial operations, including creating a new list, takes `d` amount space. Then the space taken can be computed as: `c*n+d` where `n` is our input size.
# - The values of the **constants** `c` and `d` are outside of the control of the algorithm and depend on factors such as programming language, hardware specifications, etc.<br>
#     - `when n       -> c*n + d`<br>
#     - `when n = 10  -> c*10 + d`<br>
#     - `when n = 100 -> c*100 + d`<br>
#
# </font>
# </div>

# In[2]:


n = int(input())

nums = []
for i in range(1, n + 1):
    nums.append(i * i)
print(nums)


# # Time complexity
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-info">
# <font color=black>
#
# - Time complexity is the number of elementary operations an algorithm performs in relation to the input size. Here, we count the number of operations, instead of time itself, based on the assumption that each operation takes a fixed amount of time to complete.
# - The algorithm performs `n` number of operations (n iterations of the loop) to complete its execution.
# - As we did earlier the equation for the time complexity is still: `c*n + d` thus the time complexity of this algorithm is also in the order of `n`.
#
# </font>
# </div>

# In[3]:


n = int(input())

nums = []
for i in range(1, n + 1):
    nums.append(i * i)
print(nums)


# # Asymptotic analysis
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-info">
# <font color=black>
#
# - Do we need the exact value of the equation? No, we don't! Instead, we use the highest order of the variable `n` as a representative of the space complexity.
# - This type of analysis is called **asymptotic analysis** and it evaluates how the performance changes as the input size increases.
# - In conclusion:
#     - `c*n + d` has an order of `n` space complexity.
#     - `c*n^2 + d*n + e` has an order of `n^2` space complexity.
#
# </font>
# </div>

# # Best, Worst, and Average Cases
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-info">
# <font color=black>
#
# - However asymptotic analysis is not all about worst case scenatio.
# - **Usually**, we consider three cases when analyzing an algorithm: best, worst, and average.
# - Scenarios:
#     - `k` is stored in the 0th index, just need one interation.
#     - `k` is NOT stored in the list, it takes `n+1` iterations
#
# - In linear search, the number of iterations the algorithm takes to complete execution follows this pattern.
#     - `When k is stored at the 0th index  -> 1 iteration`
#     - `When k is stored at the 1st index  -> 2 iterations`
#     - `When k is stored at the 2nd index  -> 3 iterations`
#     - `When k is stored at the 3rd index  -> 4 iterations`
#     - `:                                  :`
#     - `When k is stored at the nth index  -> n iterations`
#     - `When k is not in the list          -> n+1 iterations`
#
# - This can computed with this formula:
#
# </font>
# </div>

# ![image.png](attachment:image.png)

# In[36]:


import numpy as np


def linear_search(nums, n, k):
    """
    Linear search algorithm: a simple for
    loop to search if a given integer k is present
    in a list named nums of size n.
    """

    for i in range(n):
        if k == nums[i]:
            return i
    return -1


print("List being probed", list(np.arange(1, 7, 1)))
print(
    "Best case scenario, index found at", linear_search(list(np.arange(1, 7, 1)), 6, 1)
)
print(
    "Worst case scenario, index found at", linear_search(list(np.arange(1, 7, 1)), 6, 7)
)


# # Asymptotic notation
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-info">
# <font color=black>
#
# - There exhists 3 asymptotic notations:
#     - `Ω`(Big-Omega) notation for the lower bound. It's used to represent the **best-case** scenario of an algorithm.
#     - `O` (Big-O) notation for the upper bound. It's used to represent the **worst-case** scenario of an algorithm.
#     - `Θ` (Big-Theta) notation denotes an upper and a lower bound of a function. Therefore, it defines both at most and at least boundaries for the values the function can take for a given input. Big-theta notation is used to define the **average case** time and space complexity of an algorithm.
#
# </font>
# </div>

# ## Ω (Big-Omega) Notation definition

# <div class="alert alert-info">
# <font color=black>
#
# - `Ω(g(n)) = {f(n): there exist positive constants c and n0 such that 0 <= c*g(n) <= f(n) for all n >= n0}`
# <br><br>
# - Given `g(n) = n2` and `f(n) = 2n2 + 4` then `f(n) = Ω(g(n))` because:
# <br><br>
#     - `For c = 1 and n0 = 1, 0 <= c*g(n) <= f(n) for all n >= n0`
# <br><br>
# - Now, if we consider `f(n) = 3n + 5`, we can’t find values for constants c and n0 that satisfy the above conditions. Therefore, `f(n) = 3n + 5` doesn’t belong to big-omega of `g(n)`.
#
# </font>
# </div>

# ## O (Big-O) Notation definition

# <div class="alert alert-info">
# <font color=black>
#
# - `O(g(n)) = {f(n): there exist positive constants c and n0 such that 0 <= f(n) <= c*g(n) for all n >= n0}`
# <br><br>
# -  Given `g(n) = n2` and `f(n) = 2n2 + 4` then `f(n) = O(g(n))` because:
# <br><br>
#     - `For c = 5 and n0 = 1, 0 <= f(n) <= c*g(n) for all n >= n0`
# <br><br>
# - And if we consider `f(n) = n3+2`, it doesn’t belong to `O(g(n))` because no combinations of values for `c` and `n0` satisfies the required condition.
#
# </font>
# </div>

# ## Θ (Big-Theta) Notation definition

# <div class="alert alert-info">
# <font color=black>
#
# - `Θ(g(n)) = {f(n): there exist positive constants c1, c2 and n0 such that 0 <= c1*g(n) <= f(n) <= c2*g(n) for all n >= n0}`
# <br><br>
# - Given `g(n) = n2` and `f(n) = 2n2 + 4` then `f(n) = Θ(g(n))` because:
# <br><br>
#     - `For n0 = 1, c0 = 1, and c1 = 5, 0 <= c0*g(n) <= f(n) <= c1*g(n) for all n >= n0`
#
# </font>
# </div>

# # References
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-warning">
# <font color=black>
#
# - https://livecodestream.dev/post/complete-guide-to-understanding-time-and-space-complexity-of-algorithms/
# - [Asymptotic Analysis](https://www.geeksforgeeks.org/analysis-of-algorithms-set-1-asymptotic-analysis/?ref=ghm)
# - [Worst, Average and Best Case Analysis of Algorithms](https://www.geeksforgeeks.org/worst-average-and-best-case-analysis-of-algorithms/?ref=ghm)
#
# </font>
# </div>

# In[ ]:
