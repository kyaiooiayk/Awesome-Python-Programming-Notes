#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Introduction" data-toc-modified-id="Introduction-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Introduction</a></span></li><li><span><a href="#Data-structures" data-toc-modified-id="Data-structures-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Data structures</a></span></li><li><span><a href="#Tree" data-toc-modified-id="Tree-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Tree</a></span></li><li><span><a href="#Implementation-of-binary-tree" data-toc-modified-id="Implementation-of-binary-tree-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>Implementation of binary tree</a></span></li><li><span><a href="#Binary-Search-Tree" data-toc-modified-id="Binary-Search-Tree-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>Binary Search Tree</a></span></li><li><span><a href="#Trie" data-toc-modified-id="Trie-6"><span class="toc-item-num">6&nbsp;&nbsp;</span>Trie</a></span></li><li><span><a href="#Suffix-tree" data-toc-modified-id="Suffix-tree-7"><span class="toc-item-num">7&nbsp;&nbsp;</span>Suffix tree</a></span></li><li><span><a href="#References" data-toc-modified-id="References-8"><span class="toc-item-num">8&nbsp;&nbsp;</span>References</a></span></li></ul></div>

# # Introduction
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-warning">
# <font color=black>
# 
# **What?** Data structure: trees
# 
# </font>
# </div>

# # Data structures
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-info">
# <font color=black>
# 
# - A data structure is a storage that is used to store and organize data. It is a way of arranging data on a computer so that it can be accessed and updated efficiently.
# - A data structure is not only used for organizing the data. It is also used for processing, retrieving, and storing data.
# 
# </font>
# </div>

# ![image.png](attachment:image.png)

# # Tree
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-info">
# <font color=black>
# 
# - A tree is a popular data structure that is non-linear in nature. 
# - Unlike other data structures like an array, stack, queue, and linked list which are linear in nature, a tree represents a hierarchical structure.
# - The ordering information of a tree is not important.
# - A tree contains nodes and 2 pointers: these two pointers are the left child and the right child of the parent node.
# 
# </font>
# </div>

# ![image.png](attachment:image.png)

# # Implementation of binary tree
# <hr style="border:2px solid black"> </hr>

# In[2]:


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


# In[6]:


root = Node(1)
root.val


# In[11]:


# adding first level
root.left = Node(2)
root.right = Node(3)
print("left", root.left.val)
print("right",root.right.val)


# In[13]:


# adding left side on the first left level
# 4 becomes left child of 2
root.left.left = Node(4)
root.left.left.val


# # Binary Search Tree
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-info">
# <font color=black>
# 
# - Binary Search Tree is a node-based binary tree data structure which has the following properties:
#     - The left subtree of a node contains only nodes with keys lesser than the node’s key.
#     - The right subtree of a node contains only nodes with keys greater than the node’s key.
#     - The left and right subtree each must also be a binary search tree.
# 
# - This means that:
#     - Everything to the left of the root is less than the value of the root
#     - Everything to the right of the root is greater than the value of the root. 
# 
# - In practice: 
#     - Due to this performing, a binary search is very easy.
#     - There must be no duplicate nodes.
# 
# </font>
# </div>

# ![image.png](attachment:image.png)

# # Trie
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-info">
# <font color=black>
# 
# - In a trie, each alphabet of all the strings in the prescribed string is parsed one by one and represented by a single node. 
# - If two or more words start with the same sub-string, the identical sub-string is represented by the same chain of nodes. The chain breaks where the sub-string ends and the unique suffix begins.
# - Subsequently, each alphabet of the remaining suffix is represented by a separate node.
# - A simple illustration of the trie for this list `MACAW PANDA LEAOPARD RAT RHINO PARROT MACKERAL` of animal names would look like this:
# 
# </font>
# </div>

# ![image-2.png](attachment:image-2.png)

# # Suffix tree
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-info">
# <font color=black>
#     
# - Suffix tree is a tree data structure typically used to store a list of strings. It is also referred to as the compressed version of a trie, as, unlike a trie, each unique suffix in the list is compressed together and represented by a single node or branch in a suffix tree.
# - There are many ways to construct a suffix tree, but the semantics that is shared by most if not all types of suffix trees are as follows:
#     - A special character is appended to each sub-string.
#     - Each leaf node contains the starting position or index of the suffix it represents.
#     - The alphabets of any suffix are compressed and represented by a single node.
# - **How is this used?** Suppose we have preprocessed the text (building suffix tree of text), we can search any pattern in `O(m)` time where `m` is length of the pattern. 
# - A simple illustration of the suffix tree for this list `MACAW PANDA LEAOPARD RAT RHINO PARROT MACKERAL` of animal names would look like this:
#     
# </font>
# </div>

# ![image.png](attachment:image.png)

# # References
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-warning">
# <font color=black>
# 
# - [Data Structures](https://www.geeksforgeeks.org/data-structures/?ref=shm)
# - [Introduction to Binary Tree – Data Structure and Algorithm Tutorials](https://www.geeksforgeeks.org/introduction-to-binary-tree-data-structure-and-algorithm-tutorials/)
# - [Introduction to Binary Search Tree](https://www.geeksforgeeks.org/introduction-to-binary-search-tree-data-structure-and-algorithm-tutorials/)
# - https://www.educative.io/answers/what-is-a-suffix-tree
# 
# </font>
# </div>

# In[ ]:




