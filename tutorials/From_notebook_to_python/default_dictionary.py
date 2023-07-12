#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Introduction" data-toc-modified-id="Introduction-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Introduction</a></span></li><li><span><a href="#Imports" data-toc-modified-id="Imports-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Imports</a></span></li><li><span><a href="#Explanation" data-toc-modified-id="Explanation-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Explanation</a></span></li><li><span><a href="#Example" data-toc-modified-id="Example-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>Example</a></span><ul class="toc-item"><li><span><a href="#Using-normal-dictionary" data-toc-modified-id="Using-normal-dictionary-4.1"><span class="toc-item-num">4.1&nbsp;&nbsp;</span>Using normal dictionary</a></span></li><li><span><a href="#Using-defaultdict" data-toc-modified-id="Using-defaultdict-4.2"><span class="toc-item-num">4.2&nbsp;&nbsp;</span>Using <code>defaultdict</code></a></span></li></ul></li><li><span><a href="#References" data-toc-modified-id="References-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>References</a></span></li></ul></div>

# # Introduction
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-warning">
# <font color=black>
#
# **What?** Default dictionary
#
# </font>
# </div>

# # Imports
# <hr style = "border:2px solid black" ></hr>

# In[1]:


from collections import defaultdict


# # Explanation
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
#
# - Usually, a Python dictionary throws a `KeyError` if you try to get an item with a key that is not currently in the dictionary.
#
# - The defaultdict in contrast will simply create any items that you try to access (provided of course they do not exist yet).
#
# - To create such a "default" item, it calls the function object that you pass to the constructor (more precisely, it's an arbitrary "callable" object, which includes function and type objects).
#
# - For instance:
#     - `a = defaultdict(int)` default items are created using `int()` which will return the integer object 0.
#     - `b = defaultdict(list)` default items are created using `list()` which returns a new empty list object.
#
# </font>
# </div>

# # Example
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
#
# - Implement a group_by_owners function that: Accepts a dictionary containing the file owner name for each file name.
# - Returns a dictionary containing a list of file names for each owner name, in any order.
# - For example, for dictionary {'Input.txt': 'Randy', 'Code.py': 'Stan', 'Output.txt': 'Randy'} the group_by_owners function should return {'Randy': ['Input.txt', 'Output.txt'], 'Stan': ['Code.py']}.
#
# </font>
# </div>

# ## Using normal dictionary

# In[2]:


def group_by_owners(files):
    # Using a simple dictionary
    owners = {}

    for owned, owner in files.items():
        print(owned, owner)
        # Whilw trying to append will throw an error
        owners[owner].append(owned)

    return dict(owners)
    # return owners


files = {"Input.txt": "Randy", "Code.py": "Stan", "Output.txt": "Randy"}
print(group_by_owners(files))


# ## Using `defaultdict`

# In[ ]:


def group_by_owners(files):
    owners = defaultdict(list)

    for owned, owner in files.items():
        print(owned, owner)
        owners[owner].append(owned)

    return dict(owners)
    # return owners


files = {"Input.txt": "Randy", "Code.py": "Stan", "Output.txt": "Randy"}
print(group_by_owners(files))


# # References
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-warning">
# <font color=black>
#
# - [TestDome home page](https://www.testdome.com/tests/python-online-test/45)
# - [elegant solution](https://github.com/jozo/testdome-python-solutions/blob/master/01_file_owners.py)
# - [python `defaultdict`](https://stackoverflow.com/questions/5900578/how-does-collections-defaultdict-work)
#
# </font>
# </div>
