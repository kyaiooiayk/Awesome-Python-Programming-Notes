#!/usr/bin/env python
# coding: utf-8

# # Introduction
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-warning">
# <font color=black>
# 
# **What?** Walrus Operator
# 
# </font>
# </div>

# # What is it?
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
# 
# - Each new version of Python adds new features to the language. For Python 3.8, the biggest change is the addition of **assignment expressions**.
# - Specifically, the `:=` operator gives you a new syntax for assigning variables in the middle of expressions. 
# - This operator is colloquially known as the walrus operator.
# - During early discussions, it was dubbed the walrus operator because the := syntax resembles the eyes and tusks of a sideways walrus. 
# - The `:=` operator does not do anything that isn’t possible without it. It **only makes** certain constructs more convenient and can sometimes communicate the intent of your code more clearly.
#     
# </font>
# </div>

# # Example No.1
# <hr style = "border:2px solid black" ></hr>

# In[11]:


# Evaluating this does not print anything!
walrus = False


# In[ ]:


walrus


# In[14]:


# Evaluating this does print something indeed!
(walrus := False)


# In[15]:


walrus


# In[16]:


# Also note you need the parantheses
walrus := False


# # References
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-warning">
# <font color=black>
# 
# - [Pydon'ts *by Rodrigo G I R Ã O S E R R Ã O*](https://mathspp.gumroad.com/l/pydonts)
# - https://realpython.com/python-walrus-operator/
#    
# </font>
# </div>

# In[ ]:




