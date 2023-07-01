#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Introduction" data-toc-modified-id="Introduction-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Introduction</a></span></li><li><span><a href="#What-is-a-serch-algorithm?" data-toc-modified-id="What-is-a-serch-algorithm?-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>What is a serch algorithm?</a></span></li><li><span><a href="#List-of-known-searching-algorithms" data-toc-modified-id="List-of-known-searching-algorithms-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>List of known searching algorithms</a></span></li><li><span><a href="#Linear-search" data-toc-modified-id="Linear-search-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>Linear search</a></span><ul class="toc-item"><li><span><a href="#Time-complexity" data-toc-modified-id="Time-complexity-4.1"><span class="toc-item-num">4.1&nbsp;&nbsp;</span>Time complexity</a></span></li><li><span><a href="#Space-complexity" data-toc-modified-id="Space-complexity-4.2"><span class="toc-item-num">4.2&nbsp;&nbsp;</span>Space complexity</a></span></li></ul></li><li><span><a href="#Binary-search" data-toc-modified-id="Binary-search-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>Binary search</a></span><ul class="toc-item"><li><span><a href="#Time-complexity" data-toc-modified-id="Time-complexity-5.1"><span class="toc-item-num">5.1&nbsp;&nbsp;</span>Time complexity</a></span></li><li><span><a href="#Space-complexity" data-toc-modified-id="Space-complexity-5.2"><span class="toc-item-num">5.2&nbsp;&nbsp;</span>Space complexity</a></span></li></ul></li><li><span><a href="#References" data-toc-modified-id="References-6"><span class="toc-item-num">6&nbsp;&nbsp;</span>References</a></span></li></ul></div>

# # Introduction
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-warning">
# <font color=black>
#
# **What?** Linear and binary search
#
# </font>
# </div>

# # What is a serch algorithm?
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-info">
# <font color=black>
#
# - Searching Algorithms are designed to check for an element or retrieve an element from any data structure where it is stored.
# - These algorithms are generally classified into two categories:
#     - **Sequential Search** where the list/array is traversed sequentially and every element is checked. For example: Linear Search.
#     - **Interval Search**  are specifically designed for searching in sorted data-structures. These type of searching algorithms are much more efficient than Linear Search as they repeatedly target the center of the search structure and divide the search space in half. For Example: Binary Search.
#
# </font>
# </div>

# # List of known searching algorithms
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-info">
# <font color=black>
#
# - Linear Search
# - Sentinel Linear Search
# - Binary Search
# - Meta Binary Search | One-Sided Binary Search
# - Ternary Search
# - Jump Search
# - Interpolation Search
# - Exponential Search
# - Fibonacci Search
# - The Ubiquitous Binary Search
#
# </font>
# </div>

# # Linear search
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-info">
# <font color=black>
#
# - Linear search algorithm goes through each item in the list to find out if a certain item is stored in it.
#
# </font>
# </div>

# In[1]:


def linear_search(nums, n, k):
    """
    returns: index of k if present otherwise
    returns -1
    """
    for i in range(n):
        if k == nums[i]:
            return i
    return -1


# In[2]:


a = [1, 2, 5, 8, 1, 99]
linear_search(a, len(a), 99)


# ## Time complexity

# <div class="alert alert-info">
# <font color=black>
#
# - This algorithm iterates through each item in the list once in the worst case. Therefore, it has a worst case time complexity of `O(n)`.
# - In the best case, search completes with one search iteration and has a time complexity of `O(1)`.
#
# </font>
# </div>

# ## Space complexity

# <div class="alert alert-info">
# <font color=black>
#
# - Linear search doesn’t use additional space to store items. Therefore, has a space complexity of `O(1)`.
#
# </font>
# </div>

# # Binary search
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-info">
# <font color=black>
#
# - Binary search algorithm is used to find a given item in a **sorted list** of items.
#
#     - Find the middle item of the list and compare it to the given item k.
#     - If the middle item is equal to k, the algorithm completes.
#     - If k is smaller than the middle item, perform binary search on the array to the left of the middle item.
#     - If k is larger than the middle item, perform binary search on the array to the right of the middle item.
#     - Continue this operation recursively until k is found or the fact that k is not in the list is certain.
#
# </font>
# </div>

# ![image.png](attachment:image.png)

# In[91]:


def binary_search(nums, left, right, k):
    print("Left and right index", left, right)
    """
    The goal is to returns the index of k
    Left and right are the index
    """
    if left <= right:
        mid = left + (right - left) // 2

        # Check if the mid item is equal to k
        if nums[mid] == k:
            return mid

        # If k is smaller than the middle item, check the left half of the list
        elif nums[mid] > k:
            return binary_search(nums, left, mid - 1, k)

        # If k is lerger than the middle item, check the right half of the list
        else:
            return binary_search(nums, mid + 1, right, k)

    return -1


# In[92]:


L = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
print("Length of the list: ", len(L))
print("First and last element: ", L[0], L[len(L) - 1])


# In[94]:


binary_search(a, 0, len(L) - 1, 16)


# In[93]:


binary_search(a, 0, len(L) - 1, 56)


# In[95]:


binary_search(a, 0, len(L) - 1, 23)


# <div class="alert alert-block alert-info">
# <font color=black>
#
# - This is another slightly **DIFFERENT** implementation.
# - We can take advantage of a **ordered list** by doing a binary search.
# - We start by searching in the middle, if it is not the item that we're searching for, we can use the ordered nature of the list to eliminate half of the remaining items.
# - Keep in mind that this approach **requires sorting the list**, which may not be ideal if we're simply going to search for 1 number on the very large list (since we have to first sort the list, which is not a cheap operation).
#
# </font>
# </div>

# In[98]:


def binary_search_V2(testlist, query):
    if not testlist:
        return False
    else:
        mid_idx = len(testlist) // 2
        mid = testlist[mid_idx]
        if mid == query:
            return True
        elif query < mid:
            return binary_search_V2(testlist[:mid_idx], query)
        else:
            return binary_search_V2(testlist[mid_idx + 1 :], query)


# In[99]:


# Check if the query number is in the list
testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42]
query = 19
print(binary_search_V2(testlist, query))
query = 3
print(binary_search_V2(testlist, query))


# ## Time complexity

# <div class="alert alert-info">
# <font color=black>
#
# - Binary search, similar to what you saw in the merge sort algorithm, uses a divide and conquer approach to solve the problem. It divides the array into two and searches for the given item on the relevant side of the array. In the worst case, the algorithm divides the array logn+1 times at most. Therefore, it has a worst case time complexity of `O(logn)`.
#
# - In the best case, the middle item of the passed list has to be the searched item. Therefore, as it completes in constant time, the best case time complexity is `Ω(1)`.
#
# </font>
# </div>

# ## Space complexity

# <div class="alert alert-info">
# <font color=black>
#
# - The best case space complexity of binary search is `Ω(1)`.
# - The worst case space complexity depends on the implementation.
# - With a recursive implementation as we have done, binary search has a space complexity of `O(logn)` due to storing additional data on mid, left, and right values for each recursive call. An iterative implementation can reduce the complexity to `O(1)`.
#
# </font>
# </div>

# # References
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-warning">
# <font color=black>
#
# - https://livecodestream.dev/post/complete-guide-to-understanding-time-and-space-complexity-of-algorithms/
# - https://medium.com/@siddharthgupta555t/finally-understanding-recursion-and-binary-search-trees-857c85e72978
# - [Problem Solving with Algorithms and Data Structures](http://interactivepython.org/runestone/static/pythonds/index.html).
# - https://runestone.academy/runestone/books/published/pythonds/SortSearch/TheMergeSort.html
# - https://www.geeksforgeeks.org/searching-algorithms/?ref=ghm
#
# </font>
# </div>

# In[ ]:
