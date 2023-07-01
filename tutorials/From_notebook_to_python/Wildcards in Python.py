#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Introduction" data-toc-modified-id="Introduction-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Introduction</a></span></li><li><span><a href="#What-is-a-wildcard?" data-toc-modified-id="What-is-a-wildcard?-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>What is a wildcard?</a></span></li><li><span><a href="#Example-#1" data-toc-modified-id="Example-#1-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Example #1</a></span></li><li><span><a href="#Example-#2" data-toc-modified-id="Example-#2-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>Example #2</a></span></li><li><span><a href="#References" data-toc-modified-id="References-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>References</a></span></li></ul></div>

# # Introduction

# <div class="alert alert-block alert-warning">
# <font color=black>
#
# **What?** How to implement wildcards in python
#
# </font>
# </div>

# # What is a wildcard?

# <div class="alert alert-block alert-info">
# <font color=black>
#
# - A wildcard is a symbol used to replace or represent one or more characters.
# - They are used to **simplify** search criteria.
# - The most common wildcards are the asterisk `*` and the question mark `?`.
# - In Python, we can implement wildcards using the `regex` (regular expressions) library.
#
# </font>
# </div>

# # Example #1

# <div class="alert alert-block alert-info">
# <font color=black>
#
# - The dot `.` character is used in place of the question mark `?` symbol.
# - Hence,to search for all words matching the `col?r` pattern, the code would look something like as follows.
#
# </font>
# </div>

# In[4]:


# Regular expression library
import re

# Add or remove the words in this list to vary the results
wordlist = ["color", "colour", "work", "working", "fox", "worker", "working"]

for word in wordlist:
    # The . symbol is used in place of ? symbol
    if re.search("col.r", word):
        print("Using one dot", word)
    elif re.search("col..r", word):
        print("Using two dot", word)


# # Example #2

# <div class="alert alert-block alert-info">
# <font color=black>
#
# - Similarly, the `.+` characters are used to match one or more characters (like the asterisk `*` symbol).
# Hence, in Python, to search for all words starting with the root `work`, our regex code would look like this:
#
# </font>
# </div>

# In[5]:


# Regular expression library
import re

# Add or remove the words in this list to vary the results
wordlist = ["color", "colour", "work", "working", "fox", "worker"]

for word in wordlist:
    # The .+ symbol is used in place of * symbol
    if re.search("work.+", word):
        print(word)


# # References

# <div class="alert alert-block alert-warning">
# <font color=black>
#
# - https://www.educative.io/edpresso/how-to-implement-wildcards-in-python
#
# </font>
# </div>

# In[ ]:
