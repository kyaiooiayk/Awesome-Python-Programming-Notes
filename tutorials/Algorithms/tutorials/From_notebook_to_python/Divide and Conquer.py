#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Introduction" data-toc-modified-id="Introduction-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Introduction</a></span></li><li><span><a href="#What-is-Divide-and-Conquer?" data-toc-modified-id="What-is-Divide-and-Conquer?-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>What is Divide and Conquer?</a></span></li><li><span><a href="#Divide-and-Conquer-vs.-Dynamic-Programming" data-toc-modified-id="Divide-and-Conquer-vs.-Dynamic-Programming-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Divide and Conquer vs. Dynamic Programming</a></span></li><li><span><a href="#Example-#1" data-toc-modified-id="Example-#1-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>Example #1</a></span></li><li><span><a href="#Conclusions" data-toc-modified-id="Conclusions-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>Conclusions</a></span></li><li><span><a href="#References" data-toc-modified-id="References-6"><span class="toc-item-num">6&nbsp;&nbsp;</span>References</a></span></li></ul></div>

# # Introduction
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-warning">
# <font color=black>
# 
# **What?** Divide and Conquer
# 
# </font>
# </div>

# # What is Divide and Conquer?
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-block alert-info">
# <font color=black>
# 
# - Divide and Conquer is an algorithmic paradigm in which the problem is solved using the following 3 steps:
#     1. Divide: This involves dividing the problem into smaller sub-problems.
#     2. Conquer: Solve sub-problems by calling recursively until solved.
#     3. Combine: Combine the sub-problems to get the final solution of the whole problem.
#     
# The following are some standard algorithms that follow Divide and Conquer algorithm: Quicksort and Merge Sort.
#     
# </font>
# </div>

# # Divide and Conquer vs. Dynamic Programming
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-block alert-info">
# <font color=black>
# 
# - Both paradigm divide the given problem into subproblems and solve subproblems. 
# - Divide and Conquer should be used when the same subproblems are not evaluated many times. Otherwise Dynamic Programming or Memoization should be used. 
# - For example, Quicksort is a Divide and Conquer algorithm, we never evaluate the same subproblems again. On the other hand, for calculating the nth Fibonacci number, Dynamic Programming should be preferred (See this for details).
#     
# </font>
# </div>

# # Example #1
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-block alert-info">
# <font color=black>
#     
# - To find the maximum and minimum element from a given array is an application for divide and conquer. 
# 
# </font>
# </div>

# In[3]:


def DAC_Max(a, index, l):
    """
    Function to find the maximum no in a given array.
    Demonstrate Divide and Conquer Algorithm     
    """
    max = -1
    if(l - 1 == 0):
        return arr[index]
    if (index >= l - 2):
        if (a[index] > a[index + 1]):
            return a[index]
        else:
            return a[index + 1]

    # Logic to find the Maximum element
    # in the given array.
    max = DAC_Max(a, index + 1, l)

    if (a[index] > max):
        return a[index]
    else:
        return max


# In[4]:


def DAC_Min(a, index, l):
    """
    Function to find the minimum no in a given array.
    Demonstrate Divide and Conquer Algorithm     
    """
    min = 0
    if(l - 1 == 0):
        return arr[index]
    if (index >= l - 2):
        if (a[index] < a[index + 1]):
            return a[index]
        else:
            return a[index + 1]

    # Logic to find the Minimum element
    # in the given array.
    min = DAC_Min(a, index + 1, l)

    if (a[index] < min):
        return a[index]
    else:
        return min


# In[5]:


# Defining the variables
min, max = 0, -1

# Initializing the array
a = [70, 250, 50, 80, 140, 12, 14]

# Recursion - DAC_Max function called
max = DAC_Max(a, 0, 7)

# Recursion - DAC_Max function called
min = DAC_Min(a, 0, 7)
print("The minimum number in a given array is : ", min)
print("The maximum number in a given array is : ", max)


# # Conclusions
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-danger">
# <font color=black>
# 
# - **Advantages** of Divide and Conquer Algorithm:
#     - The difficult problem can be solved easily.
#     - It divides the entire problem into subproblems thus it can be solved parallelly ensuring multiprocessing
#     - Efficiently uses cache memory without occupying much space
#     - Reduces time complexity of the problem
# 
# - **Disadvantages** of Divide and Conquer Algorithm:
#     - It involves recursion which is sometimes slow
#     - Efficiency depends on the implementation of logic
#     - It may crash the system if the recursion is performed rigorously
# 
# </font>
# </div>

# # References
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-warning">
# <font color=black>
# 
# - https://www.geeksforgeeks.org/introduction-to-divide-and-conquer-algorithm-data-structure-and-algorithm-tutorials/
# 
# </font>
# </div>

# In[ ]:




