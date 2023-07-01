#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Introduction" data-toc-modified-id="Introduction-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Introduction</a></span></li><li><span><a href="#Motivation" data-toc-modified-id="Motivation-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Motivation</a></span></li><li><span><a href="#Example" data-toc-modified-id="Example-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Example</a></span></li><li><span><a href="#Conclusions" data-toc-modified-id="Conclusions-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>Conclusions</a></span></li><li><span><a href="#References" data-toc-modified-id="References-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>References</a></span></li></ul></div>

# # Introduction
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-warning">
# <font color=black>
# 
# **What?** Match - case statement
# 
# </font>
# </div>

# # Motivation
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
# 
# - This feature is available from `python 3.10` onward only.
# - The `match - case` syntax is similar to **switch statements** in other Object-oriented languages, and it is meant to make matching a structure to a case easier
# 
# </font>
# </div>

# # Example
# <hr style = "border:2px solid black" ></hr>

# In[1]:


def greeting(message):
    match message.split():
        case["hello"]:
            print("this message says hello")
        case["hello", name]:
            print("This message is a personal greeting to {name}")
        case _:
            print("The message didn’t match with anything")


# In[ ]:


greeting("hello")


# In[ ]:


greeting("hello George")


# In[ ]:


greeting("hello George Johnson")


# # Conclusions
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-danger">
# <font color=black>
# 
# - It does not mean the match statement will be the best alternative always and, in particular, the match statement is generally being misused if you use it as a **simple switch**.
# - short and basic match statements could be vanilla if statements.
#     
# </font>
# </div>

# # References
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-warning">
# <font color=black>
# 
# - https://blog.teclado.com/python-match-case/
# 
# </font>
# </div>

# In[ ]:




