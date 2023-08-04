#!/usr/bin/env python
# coding: utf-8

# # Introduction
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-warning">
# <font color=black>
# 
# **What?** Short-circuting
# 
# </font>
# </div>

# # What is it?
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-info">
# <font color=black>
# 
# - This mostly relevant because of the following property: and and or only evaluate the right operand if the left operand is not enough to determine the result of the operation. 
#     
# - This is what short-circuiting is: not evaluating the whole expression (stopping short of evaluating it) if we already have enough information to determine the final outcome.
# 
# - Together with the fact that the boolean operators `and` and `or` return the values of the operands and not necessarily a Boolean, means we can do some really neat things with them.
# 
# - **Why does it matter?** If the left operand to or is False or falsy, we know that or has to look at its right operand and will, therefore, return the value of its right operand after evaluating it. On the other hand, if the left operand is True or truthy, or will return the value of the left operand without even evaluating the right operand. *Hence* using short-circuiting can save you a lot of computational time.
# 
# </font>
# </div>

# # Example #1
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-info">
# <font color=black>
# 
# - `or` evaluates to True if any of its operands is truthy. 
# 
# - If the left operand to or is False (or falsy, for that matter) then the or operator has to look to its right operand in order to determine the final result.
# 
# - Therefore, we know that an expression like `val = False or y` will have the value of `y` in it, and in an if statement or in a while loop, it will evaluate the body of the construct only if `y` is truthy
#     
# </font>
# </div>

# In[3]:


# truthy value.
y = 5  


# In[5]:


# Let's verufy it
bool(y)


# In[6]:


if False or y:
    print("Got in!")
else:
    print("Didn't get in...")


# <div class="alert alert-info">
# <font color=black>
# 
# - If the left operand to or is False or falsy, then we need to look at the right operand to determine the value of the or.
# 
# </font>
# </div>

# In[8]:


# truthy value
y = []  


# In[9]:


# Let's verify it
bool(y)


# In[10]:


if False or y:
    print("Got in!")
else:
    print("Didn't get in...")


# # References
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-warning">
# <font color=black>
# 
# - https://mathspp.com/blog/pydonts
# 
# </font>
# </div>

# In[ ]:




