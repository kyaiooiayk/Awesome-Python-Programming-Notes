#!/usr/bin/env python
# coding: utf-8

# # Binary Search

# The figures below provide a short illustration of how the implementation works on a toy example:
#
# ![](images/binary_search/ex-1-1.png)
#
# ![](images/binary_search/ex-1-2.png)

# ![image.png](attachment:image.png)

# ![image.png](attachment:image.png)

# ## Binary Search Implementation

# In[2]:


def binary_search(array, value):
    ary = array
    min_idx = 0
    max_idx = len(array)

    while min_idx < max_idx:
        middle_idx = (min_idx + max_idx) // 2

        if array[middle_idx] == value:
            return middle_idx
        elif array[middle_idx] < value:
            min_idx = middle_idx + 1
        else:
            max_idx = middle_idx

    return None


# In[3]:


binary_search(array=[], value=1)


# In[4]:


binary_search(array=[1, 2, 4, 7, 8, 10, 11], value=1)


# In[5]:


binary_search(array=[1, 2, 4, 7, 8, 10, 11], value=2)


# In[6]:


binary_search(array=[1, 2, 4, 7, 8, 10, 11], value=4)


# In[7]:


binary_search(array=[1, 2, 4, 7, 8, 10, 11], value=11)


# In[8]:


binary_search(array=[1, 2, 4, 7, 8, 10, 11], value=99)


# ## Binary Search using Recursion

# Note that this implementation of recursive binary search deliberately avoid slicing the `array` (e.g., `array[:middle_idx]`), because slicing Python lists is expensive due to the random memory access. E.g., slicing a Python list with as `a_list[:k]` is an O(k) operation.

# In[9]:


def recursive_binary_search(array, value, start_idx=None, end_idx=None):
    len_ary = len(array)

    if start_idx is None:
        start_idx = 0
    if end_idx is None:
        end_idx = len(array) - 1

    if not len_ary or start_idx >= end_idx:
        return None

    middle_idx = (start_idx + end_idx) // 2
    if array[middle_idx] == value:
        return middle_idx

    elif array[middle_idx] > value:
        return recursive_binary_search(
            array, value, start_idx=start_idx, end_idx=middle_idx
        )
    else:
        return recursive_binary_search(
            array, value, start_idx=middle_idx + 1, end_idx=len_ary
        )
    return None


# In[10]:


recursive_binary_search(array=[], value=1)


# In[11]:


recursive_binary_search(array=[1, 2, 4, 7, 8, 10, 11], value=1)


# In[12]:


recursive_binary_search(array=[1, 2, 4, 7, 8, 10, 11], value=4)


# In[13]:


recursive_binary_search(array=[1, 2, 4, 7, 8, 10, 11], value=11)


# In[14]:


recursive_binary_search(array=[1, 2, 4, 7, 8, 10, 11], value=99)


# # References
# - https://nbviewer.org/github/rasbt/algorithms_in_ipython_notebooks/blob/master/ipython_nbs/search/binary_search.ipynb
# - https://en.wikipedia.org/wiki/Binary_search_algorithm.

# In[ ]:
