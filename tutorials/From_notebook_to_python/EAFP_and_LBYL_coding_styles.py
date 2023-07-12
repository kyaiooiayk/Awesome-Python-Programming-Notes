#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Introduction" data-toc-modified-id="Introduction-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Introduction</a></span></li><li><span><a href="#EAFP" data-toc-modified-id="EAFP-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>EAFP</a></span></li><li><span><a href="#LBYL" data-toc-modified-id="LBYL-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>LBYL</a></span></li><li><span><a href="#Conclusions" data-toc-modified-id="Conclusions-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>Conclusions</a></span></li><li><span><a href="#References" data-toc-modified-id="References-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>References</a></span></li></ul></div>

# # Introduction
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-warning">
# <font color=black>
#
# **What?** EAFP and LBYL coding styles
#
# </font>
# </div>

# # EAFP
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
#
# - EAFP Stands for “Easier to Ask for Forgiveness than Permission”.
# - A coding practice that is more or less the opposite of the LBYL.
# - For example, if you want to ask the user for a number whose default value will be 1, you can use the code:
#
# </font>
# </div>

# In[11]:


print("Type a positive integer (defaults to 1):")
s = input(" >> ")
print("Given value:", s)
if s.isnumeric():
    n = int(s)
else:
    n = 1
print(n)


# In[8]:


str.isnumeric.__doc__


# <div class="alert alert-info">
# <font color=black>
#
# - If failing is expected to happen not very often, then EAFP is faster: you just run a piece of code (your operation) instead of two (the “look” and the “leap”).
#
# </font>
# </div>

# # LBYL
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
#
# - LBYL stands for “Look Before You Leap”.
# - LBYL means you first check if a given operation can be made successfully, and then proceed to do it.
# - For example, if you want to ask the user for a number whose default value will be 1, you can use the code:
#
# </font>
# </div>

# In[16]:


print("Type a positive integer (defaults to 1):")
s = input(" >> ")
try:
    n = int(s)
except ValueError:
    n = 1
print(n)


# <div class="alert alert-info">
# <font color=black>
#
# - With EAFP, you first try to perform whatever operation it is you want to do, and then use a try block to capture an eventual exception that your operation might throw in case it is not successful.
# - We simply try to convert s into an integer and in case a `ValueError` exception is raised, we set the default value.
# - LBYL may still fail. When interacting with the environment, for example with the Internet or with the OS, in between the time it takes for you to do your safety check and then perform the operation, circumstances may change and your operation may no longer be viable.
# - If you are trying to perform a complex operation that might fail in several ways, it might be easier to just enumerate the exceptions that might be raised instead of writing a really, really long if statement that performs all the necessary checks in advance.
#
# </font>
# </div>

# # Conclusions
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-danger">
# <font color=black>
#
# - EAFP **is NOT** the absolute best way to go in every single situation, but EAFP code can be very readable and performant!
#
# </font>
# </div>

# # References
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-warning">
# <font color=black>
#
# - https://mathspp.com/blog/pydonts
#
# </font>
# </div>

# In[ ]:
