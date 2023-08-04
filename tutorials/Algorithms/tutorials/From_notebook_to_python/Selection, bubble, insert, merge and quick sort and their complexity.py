#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Introduction" data-toc-modified-id="Introduction-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Introduction</a></span></li><li><span><a href="#Selection-Sort" data-toc-modified-id="Selection-Sort-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Selection Sort</a></span><ul class="toc-item"><li><span><a href="#Time-complexity" data-toc-modified-id="Time-complexity-2.1"><span class="toc-item-num">2.1&nbsp;&nbsp;</span>Time complexity</a></span></li><li><span><a href="#Space-complexity" data-toc-modified-id="Space-complexity-2.2"><span class="toc-item-num">2.2&nbsp;&nbsp;</span>Space complexity</a></span></li></ul></li><li><span><a href="#Bubble-sort" data-toc-modified-id="Bubble-sort-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Bubble sort</a></span><ul class="toc-item"><li><span><a href="#Time-complexity" data-toc-modified-id="Time-complexity-3.1"><span class="toc-item-num">3.1&nbsp;&nbsp;</span>Time complexity</a></span></li><li><span><a href="#Space-complexity" data-toc-modified-id="Space-complexity-3.2"><span class="toc-item-num">3.2&nbsp;&nbsp;</span>Space complexity</a></span></li></ul></li><li><span><a href="#Insert-sort" data-toc-modified-id="Insert-sort-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>Insert sort</a></span><ul class="toc-item"><li><span><a href="#Time-complexity" data-toc-modified-id="Time-complexity-4.1"><span class="toc-item-num">4.1&nbsp;&nbsp;</span>Time complexity</a></span></li><li><span><a href="#Space-complexity" data-toc-modified-id="Space-complexity-4.2"><span class="toc-item-num">4.2&nbsp;&nbsp;</span>Space complexity</a></span></li></ul></li><li><span><a href="#Merge-sort" data-toc-modified-id="Merge-sort-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>Merge sort</a></span><ul class="toc-item"><li><span><a href="#Time-complexity" data-toc-modified-id="Time-complexity-5.1"><span class="toc-item-num">5.1&nbsp;&nbsp;</span>Time complexity</a></span></li><li><span><a href="#Space-complexity" data-toc-modified-id="Space-complexity-5.2"><span class="toc-item-num">5.2&nbsp;&nbsp;</span>Space complexity</a></span></li></ul></li><li><span><a href="#Quick-sort" data-toc-modified-id="Quick-sort-6"><span class="toc-item-num">6&nbsp;&nbsp;</span>Quick sort</a></span></li><li><span><a href="#References" data-toc-modified-id="References-7"><span class="toc-item-num">7&nbsp;&nbsp;</span>References</a></span></li></ul></div>

# # Introduction
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-warning">
# <font color=black>
# 
# **What?** Selection, bubble, insert, merge and quick sort and their complexity
# 
# </font>
# </div>

# # Selection Sort
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-info">
# <font color=black>
# 
# - The selection sort algorithm is used to **sort a list of items**.
# - It iterates through the list once and finds the minimum item and puts it at the starting index of the list.
# - Then, in the next iteration, it finds the second minimum item and puts it in the second place.
# - This pattern continues until all the items in the list are sorted.
# 
# </font>
# </div>

# ![image.png](attachment:image.png)

# In[7]:


def selection_sort(nums, n):
    """
    nums: the list of numbers to sort
    n: the length of the list
    """
    for i in range(n-1):

        min_index = i
        # Search the unsorted indexes for the next minimum number
        for j in range(i+1, n):
            if (nums[j] < nums[min_index] ):
                min_index = j
        # Swap the next minimum number with the earliest unsorted number
        nums[i], nums[min_index] = nums[min_index], nums[i]
    
    return nums


# In[8]:


a = [26,54,93,17,77,31,44,55,20]
selection_sort(a, len(a))


# ## Time complexity

# <div class="alert alert-info">
# <font color=black>
# 
# - The best-case occurs when the passed list of numbers is already in sorted order. However, the selection sort algorithm still has to complete all the iteration steps because it **doesn’t have** a mechanism to know whether the list is already sorted or not.
# - The best case time complexity of the selection sort is `Ω(n2)`.
# - The worst case time complexity of the selection sort is `O(n2)`.
# - Thus average-case time complexities is `Θ(n2)`.
# 
# </font>
# </div>

# ## Space complexity

# <div class="alert alert-info">
# <font color=black>
# 
# - Selection sort doesn’t store additional data in the memory. It only modifies the original list. 
# - Therefore, it has a **constant** space complexity of `O(1)`.
# 
# </font>
# </div>

# # Bubble sort
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-info">
# <font color=black>
# 
# - The bubble sort algorithm compares adjacent items in the list and swaps them if the first item is smaller than the second item. It continues this operation until no swaps are performed while iterating through the list (i.e., the list is sorted).
# - For example, `[22, 12]` are two adjacent items in the list, bubble sort swaps them and changes the order to `[12, 22]`.
# 
# </font>
# </div>

# ![image.png](attachment:image.png)

# In[15]:


def bubble_sort(nums, n):
    for i in range(n-1):
        swapped = False
        for j in range(n-i-1):
            if (nums[j] > nums[j+1]):
                # Swap the adjacent numbers to keep them in ascending order
                nums[j], nums[j+1] = nums[j+1], nums[j]
                swapped = True
            #print(swapped)
        if not swapped:
            break
    return nums


# In[16]:


a = [26,54,93,17,77,31,44,55,20]
bubble_sort(a, len(a))


# ## Time complexity

# <div class="alert alert-info">
# <font color=black>
# 
# - In the best case when the passed list is already sorted, the algorithm performs `n-1` operations, which is in the order of `n`. Therefore, its best-case time complexity is `Ω(n)`. This means it loops trough the list, it checks and  if soted it does not swap anythng. This saves us a loop!
# 
# - In the worst case, when the items in the list are in descending order, the algorithm performs a number of operations in the order of `n2`. Therefore, bubble sort has a worst-case time complexity of `O(n2)`.
# - The average time complexity of the algorithm is also `Θ(n2)`.
# 
# </font>
# </div>

# ## Space complexity

# <div class="alert alert-info">
# <font color=black>
# 
# - Similar to selection sort, bubble sort has a constant space complexity of `O(1)`. 
# 
# </font>
# </div>

# # Insert sort
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-info">
# <font color=black>
# 
# - Insertion sort algorithm follows these steps to sort a list of items.
#     - Iterate through the array starting from the 0th index.
#     - Check if the current item is smaller than its predecessor.
#     - If yes, compare the current item to the item before the predecessor.
#     - Continue this until an item smaller or equal to the current item is found.
#     - Place the current item next to the smaller item by moving the greater items one position up.
#  
# </font>
# </div>

# ![image.png](attachment:image.png)

# In[18]:


def insertion_sort(nums, n):
    for i in range(1, n):
        current = nums[i]
        
        # Check the previous items to find where current item fits in the sorting order
        j = i-1
        while j >= 0 and nums[j] > current:
            nums[j+1] = nums[j]
            j -= 1
        nums[j+1] = current
    return nums


# In[19]:


a = [4,3,2,10,12,1,5,6]
insertion_sort(a, len(a))


# ## Time complexity

# <div class="alert alert-info">
# <font color=black>
# 
# - In the best case, the insertion sort algorithm takes only `n` operations because the list is already sorted. Therefore, it has `Ω(n)` best case time complexity. 
# - In the worst case, the algorithm takes number of operations to complete, which is in the order of `n2`. So the worst case time complexity is `O(n2)`.
# 
# </font>
# </div>

# ## Space complexity

# <div class="alert alert-info">
# <font color=black>
# 
# - Since this algorithm modifies the list in place without using additional memory, it has a space complexity of `O(1)`.
# 
# </font>
# </div>

# # Merge sort
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-info">
# <font color=black>
# 
# - Merge sort divides the given list into shorter lists and sorts them before combining them together to create a fully sorted list. The steps involved in the algorithm are as follows.
# 
#     - Divide the list into two halves by its middle point.
#     - Merge sort the first and second halves of the list separately.
#     - Merge the two sorted halves to create the final sorted list.
# 
# - As you might have guessed, merge sort is a recursive algorithm that calls the mergeSort function again and again on halved lists until the initial list is separated into singular items. Then, it merges these items back in the sorted order. 
# 
# </font>
# </div>

# ![image.png](attachment:image.png)

# In[21]:


def merge(arr, left, right):

    i = j = k = 0

    #Compare the elements in the two lists starting from the first items
    #Add the smallest item to the merged list 
    #Continue this until all items of one list are added
    while i < len(left) and j < len(right):
        if (left[i] < right[j]):
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    #Check if there are more items in left list and merge them in order
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    #Check if there are more items in right list and merge them in order
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1


def merge_sort(arr, n):
    if (n > 1):
        mid = n//2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left, len(left))
        merge_sort(right, len(right))

        #Merge left and right lists in sorted order
        merge(arr, left, right)
    return arr


# In[22]:


a = [1,5,3,4,2,6]
merge_sort(a, len(a))


# <div class="alert alert-block alert-info">
# <font color=black><br>
# 
# - This is a slightly **DIFFERENT** implementation.
# - We now turn our attention to using a divide and conquer strategy as a way to improve the performance of sorting algorithms. The first algorithm we will study is the merge sort. Merge sort is a recursive algorithm that continually splits a list in half. 
# - If the list is empty or has one item, it is sorted by definition (the base case). If the list has more than one item, we split the list and recursively invoke a merge sort on both halves. Once the two halves are sorted, the fundamental operation, called a merge, is performed. Merging is the process of taking two smaller sorted lists and combining them together into a single, sorted, new list  
# 
# <br></font>
# </div>

# ![image.png](attachment:image.png)

# In[1]:


def merge_sort(alist):
    if len(alist) > 1:
        mid = len(alist) // 2
        left_half = alist[:mid]
        right_half = alist[mid:]
        merge_sort(left_half)
        merge_sort(right_half)
        
        # loop through the left and right half,
        # compare the value and fill them back
        # to the original list
        i, j, k = 0, 0, 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                alist[k] = left_half[i]
                i += 1
            else:
                alist[k] = right_half[j]
                j += 1
            k += 1
        
        # after filling in the sorted value,
        # there will be left-over values on
        # either the left or right half, simply
        # append all the left-over values back
        while i < len(left_half):
            alist[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            alist[k] = right_half[j]
            j += 1
            k += 1
            
    return alist


# In[2]:


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
merge_sort(alist)


# ## Time complexity

# <div class="alert alert-info">
# <font color=black>
# 
# - Merge sort has time complexities with the same order in best, worst, and average case scenarios. Let’s see how we can find this order of the algorithm.
# 
#     - Merge sort algorithm divides a list of `n` items into two continuously until there are `n` number of lists with single items.
#     - If `n = 2x`, this takes `x` number of divisions by `2` to get to the base level. So it creates `x` number of levels, each level containing arrays of size `n/2, n/4, …, n/2x-1, n/2x`. We can calculate the value of x using logarithms: `log_2(n)`.
#     - If `2x+1 > n > 2x`, it takes x+1 number of divisions by 2 to get to the base level. This results in creating `x+1` levels. We can round up the value of `log2n+1` to find the value of `x+1`.
#     - In each level, the merge sort algorithm iterates once through each item in separated lists while merging left and right lists together. Because there n items in total, each level takes `n` number of operations to complete the merge.
#     - Since there are, at most, `logn+1` levels, the total number of operations the algorithm carries out is `n*( logn+1)`. It’s in the order of `n*logn`.
# 
# - Therefore, the best, worst, and average time complexity of merge sort is respectively, `Ω(n*logn)`,`O(n*logn)`, and `Θ(n*logn)`. 
# 
# </font>
# </div>

# ## Space complexity

# <div class="alert alert-info">
# <font color=black>
# 
# - Merge sort uses additional n space to store the items in the divided arrays. 
# - Therefore, it has a space complexity of `Ω(n)`, `O(n)`, and `Θ(n)` in best, worst, and average cases.
# 
# </font>
# </div>

# # Quick sort
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-info">
# <font color=black>
# 
# - The quick sort uses divide and conquer to gain the same advantages as the merge sort, **while not** using additional storage. As a trade-off, however, it is possible that the list may not be divided in half. 
# - When this happens, we will see that performance is **diminished**.
# 
# </font>
# </div>

# ![image.png](attachment:image.png)

# In[3]:


def quick_sort(alist):
    _sort(alist, 0, len(alist) - 1)
    
def _sort(alist, first, last):
    if first < last:
        split_point = _partition(alist, first, last)
        _sort(alist, first, split_point - 1)
        _sort(alist, split_point + 1, last)
        
def _partition(alist, first, last):
    right = last
    left = first + 1
    pivot_value = alist[first]
    
    # find the split point of the pivot and move all other
    # items to the appropriate side of the list (i.e. if
    # the item is greater than pivot, then it should be
    # on the right hand side and vice versa)
    done = False
    while not done: 
        while left <= right and alist[left] <= pivot_value:
            left += 1
        while alist[right] >= pivot_value and right >= left:
            right -= 1
        
        if right <= left:
            done = True
        else:
            alist[right], alist[left] = alist[left], alist[right]
    
    # swap pivot value to split point
    alist[first], alist[right] = alist[right], alist[first]
    return right


# In[4]:


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
quick_sort(alist)
alist


# # References
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-warning">
# <font color=black>
# 
# - https://livecodestream.dev/post/complete-guide-to-understanding-time-and-space-complexity-of-algorithms/
# 
# </font>
# </div>

# In[ ]:




