#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Introduction" data-toc-modified-id="Introduction-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Introduction</a></span></li><li><span><a href="#How-to-make-a-shallow-and-deep-copy-of-an-object" data-toc-modified-id="How-to-make-a-shallow-and-deep-copy-of-an-object-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>How to make a shallow and deep copy of an object</a></span></li><li><span><a href="#Shallow" data-toc-modified-id="Shallow-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Shallow</a></span></li><li><span><a href="#Deep-copy" data-toc-modified-id="Deep-copy-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>Deep copy</a></span></li><li><span><a href="#References" data-toc-modified-id="References-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>References</a></span></li></ul></div>

# # Introduction
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-warning">
# <font color=black>
# 
# **What?** A collection of not-so-obvious Python stuff
# 
# </font>
# </div>

# # How to make a shallow and deep copy of an object
# <hr style = "border:2px solid black" ></hr>

# In[3]:


from copy import deepcopy

list1 = [1,2]
list2 = list1           # reference
list3 = list1[:]        # shallow copy
list4 = list1.copy()    # shallow copy
list5 = deepcopy(list1) # deep copy

print('IDs:\nlist1: {}\nlist2: {}\nlist3: {}\nlist4: {}\nlist5: {}\n'
      .format(id(list1), id(list2), id(list3), id(list4), id(list5)))


# # Shallow
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
# 
# - If we use the assignment operator to assign one list to another list, we just create a new name reference to the original list.
# - If we want to create a new list object, we have to make a copy of the original list. This can be done via `a_list[:]` or `a_list.copy()`.
# 
# </font>
# </div>

# In[12]:


list1 = [1,2]
list2 = list1        # reference
list3 = list1[:]     # shallow copy
list4 = list1.copy() # shallow copy

print('IDs:\nlist1: {}\nlist2: {}\nlist3: {}\nlist4: {}\n'
      .format(id(list1), id(list2), id(list3), id(list4)))

list2[0] = 3
print('list1:', list1)

list3[0] = 4
list4[1] = 4
print('\nlist1:', list1)
print('list2:', list2)
print('list3:', list3)
print('list4:', list4)


# # Deep copy
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
# 
# - If we are dealing with compound objects (e.g., lists that contain other lists, for more information) it becomes a little trickier.
# - In the case of compound objects, a shallow copy would create a new compound object, **but** it would just insert the references to the contained objects into the new compound object. In contrast, a deep copy would go "deeper" and create also new objects for the objects found in the original compound object. 
# 
# </font>
# </div>

# In[13]:


from copy import deepcopy

list1 = [[1], [2]]
list2 = list1.copy()    # shallow copy
list3 = deepcopy(list1)  # deep copy

print('IDs:\nlist1: {}\nlist2: {}\nlist3: {}\n'
      .format(id(list1), id(list2), id(list3)))

list2[0][0] = 3
print('list1:', list1)

list3[0][0] = 5
print('\nlist1:', list1)
print('list2:', list2)
print('list3:', list3)


# # References
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-warning">
# <font color=black>
# 
# - https://nbviewer.org/github/rasbt/python_reference/blob/master/tutorials/not_so_obvious_python_stuff.ipynb?create=1
# - https://docs.python.org/2/library/copy.html
#     
# </font>
# </div>

# In[ ]:




