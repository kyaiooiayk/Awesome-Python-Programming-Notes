#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Introduction" data-toc-modified-id="Introduction-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Introduction</a></span></li><li><span><a href="#What-is-the-ord-method?" data-toc-modified-id="What-is-the-ord-method?-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>What is the ord method?</a></span></li><li><span><a href="#What-is-unicode?" data-toc-modified-id="What-is-unicode?-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>What is unicode?</a></span></li><li><span><a href="#Example-#1" data-toc-modified-id="Example-#1-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>Example #1</a></span></li><li><span><a href="#Example-#2" data-toc-modified-id="Example-#2-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>Example #2</a></span></li><li><span><a href="#References" data-toc-modified-id="References-6"><span class="toc-item-num">6&nbsp;&nbsp;</span>References</a></span></li></ul></div>

# # Introduction

# <div class="alert alert-warning">
# <font color=black>
# 
# **What?** `ord` method
# 
# </font>
# </div>

# # What is the ord method?

# <div class="alert alert-info">
# <font color=black>
# 
# - The Python `ord()` method converts a character into its Unicode code.
# - This method returns an integer that represents that character in Unicode. 
# 
# 
# - **An example?** For example, you may be creating a profile update form in Python that needs to check each string for emojis and other special characters. These characters are not allowed to be used in the form.
# 
# 
# </font>
# </div>

# # What is unicode?

# <div class="alert alert-info">
# <font color=black>
# 
# - Letters that appear on computers are stored by computers as a list of numbers.
# - This all changed In 1991. In this year, an organization called the Unicode Consortium published a standardized specification for how characters could be represented with computers.
# 
# </font>
# </div>

# # Example #1

# In[2]:


string = ["a", "b", "c", "d", "e"]
for i in string:
    print("Unicode representation for ", i, "is", ord(i))


# # Example #2

# <div class="alert alert-info">
# <font color=black>
# 
# - `ord()` is the opposite of the `chr()` method. Whereas `chr()` returns the character correlated with a Unicode value, `ord()` returns the Unicode value of a particular character. 
# 
# </font>
# </div>

# In[4]:


for i in string:
    print("Unicode representation for ", i, "is", ord(i), ", checking the reverse conversion: ", chr(ord(i)))


# # References

# <div class="alert alert-warning">
# <font color=black>
# 
# - https://careerkarma.com/blog/python-ord/
# 
# </font>
# </div>

# In[ ]:




