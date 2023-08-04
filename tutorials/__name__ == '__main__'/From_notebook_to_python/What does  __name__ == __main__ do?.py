#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Introduction" data-toc-modified-id="Introduction-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Introduction</a></span></li><li><span><a href="#The-basics" data-toc-modified-id="The-basics-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>The basics</a></span></li><li><span><a href="#The-problem" data-toc-modified-id="The-problem-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>The problem</a></span></li><li><span><a href="#A-better-way" data-toc-modified-id="A-better-way-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>A better way</a></span></li><li><span><a href="#Others" data-toc-modified-id="Others-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>Others</a></span></li><li><span><a href="#Conclusions" data-toc-modified-id="Conclusions-6"><span class="toc-item-num">6&nbsp;&nbsp;</span>Conclusions</a></span></li><li><span><a href="#References" data-toc-modified-id="References-7"><span class="toc-item-num">7&nbsp;&nbsp;</span>References</a></span></li></ul></div>

# # Introduction
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-warning">
# <font color=black>
# 
# **What?**  What does `if __name__ == "__main__"`: do?
# 
# </font>
# </div>

# # The basics
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-info">
# <font color=black>
# 
# - `__name__` is a global variable.
# 
# - `__name__` variable points to the namespace wherever the Python interpreter happens to be at the moment. 
# 
# - The global variable, __name__, in the module that is the entry point to your program, is `__main__`. 
#     
# - If you are not using the construct `__name__ == "__main__" the `__name__` is assigned to the name you import the module by.
# 
# - So, the code under the if block runs if the module is the entry point to your program.
# 
# - **In practice?** It allows the code in the module to be importable by other modules, without executing the code block beneath on import.
# 
# </font>
# </div>

# # The problem
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-info">
# <font color=black>
# 
# - Let's assume we have a script called `important.py`
# - Now I can call the script as normal with `python important.py` and this works OK.
# - However, what happens when I import this script from another script called `test_import.py`? The function `do_important()` get executed. 
# - **What if this is a behaviour we do not want?** This is where the `__name__ == "__main__"` construct comes to the rescue.
# 
# </font>
# </div>

# In[14]:


# Checking if the script is present
get_ipython().system('ls')


# In[15]:


# tunning the script
get_ipython().system('python important.py')


# In[17]:


# As you can see what is inside important.py get executed
get_ipython().system('python test_import.py')


# # A better way
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-info">
# <font color=black>
# 
# - `__name__` variable points to the namespace wherever the Python interpreter happens to be at the moment. 
# - Inside an imported module, it's the name of that module/script. 
# - There's a **Pythonic way** to improve on this. All we are trying to say is how to we call the script only when we want to do and how do we protect the script when we import the module but we do not want to runt it unless called specifically?
# - We are going to rewrite our to scripts. These are indicated by the `_new.py`
# 
# </font>
# </div>

# In[22]:


get_ipython().system('ls')


# In[28]:


# The model still behaves as before
get_ipython().system('python important_new.py')


# In[30]:


# The real difference is here. As you can see the function is not extecuted
get_ipython().system('python test_import_new.py')


# # Others
# <hr style="border:2px solid black"> </hr>

# In[31]:


# Importing but not executing it
import important_new


# In[33]:


# Executing explicitly the function defined under the main
important_new.main()


# # Conclusions
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-danger">
# <font color=black>
# 
# - `__name__` is a variable defined for each script that defines whether the script is being run as the main module or it is being run as an imported module.
# 
# - So it's possible to program different behaviour into a module for the two cases:
#     - As a module or
#     - As a script.
#  
# </font>
# </div>

# # References
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-warning">
# <font color=black>
# 
# - https://stackoverflow.com/questions/419163/what-does-if-name-main-do 
# 
# </font>
# </div>

# In[ ]:




