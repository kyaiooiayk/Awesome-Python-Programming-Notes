#!/usr/bin/env python
# coding: utf-8

# # Introduction

# <div class="alert alert-warning">
# <font color=black>
# 
# **What?** self and __init__
# 
# </font>
# </div>

# # Create a class

# <div class="alert alert-info">
# <font color=black>
# 
# - So in python everything is an object, but classess and objects are not exactly the same thing. You can create an object instantiating a class though.
# - Classes can be thought as **blueprint** for creating object. In other words, I've created a sort of instruction manual for constructing a customer object.
# 
# </font>
# </div>

# In[2]:


class Customer(object):
    """A customer of ABC bank with a checking. account.
    
    Customer have the following propperties:
    
    Atributes:
        name: a string representing the custome name
        balance: a float. tracking the current balance of the customer's account
    """
    
    def __init__(self, name, balance = 0.0):
        """Object initialisation.
        
        Returns a customers objkect whose name is name and stating
        balance is balance.
        """
        
        self.name = name
        self.balance = balance
        
    def withdraw(self, amount):
        """Withdraw.
        
        Returns the balance remaininga fter withdrawing ana mount.
        """
        
        if amount > self.balance:
            raise RuntimeError("Amount requested is greater than the current balance")
        self.balance -= amount
        
        return self.balance
    
    def deposit(self, amount):
        """Deposit.
        
        Returns the balance remaining after depositing some monies.
        """
        
        self.balance += amount
        
        return sel.balance


# <div class="alert alert-info">
# <font color=black>
# 
# - The class `Customer(object)` does not create a new customer, as we have created a blueprint only.
# - How do we create a real customer then? We;ll have to call the special class method `__init__` to create one.
# - This method is call automtically when we. instantiate the obejct with (for instance) `Customer("Charlier", 100)`. This is saying "hey create a customer named Charlie with 100GBP in his account!.
# 
# </font>
# </div>

# In[26]:


custormerA = Customer("Charlier", 100)
custormerB = Customer("Maria", 200)
customerNull = Customer("Null")


# In[27]:


custormerA.__dict__


# In[28]:


custormerB.__dict__


# In[29]:


customerNull.__dict__


# # What is self?

# <div class="alert alert-info">
# <font color=black>
# 
# - `self` is the instance itself!
# - When we say `withdraw(self, amount)`, we're saying: "here's how you  withdraw money from a Customer object (called `self`) and a money figure (called amount)."
# - Put in another way `customerA.withdraw(10)` is totally equivalent to `Customer.withdraw(customerA, 10)`.
# - But how can pass `customerA` is there is not `customerA` as yet? This is where `__init__` comes in.
# 
# </font>
# </div>

# # What is _ _init_ _ ?

# <div class="alert alert-info">
# <font color=black>
# 
# - Python allows us to extend the `self` pattern also to objects that are being constructed.
# - **This is the reason why** when we call `__init__` we initialise object by saying `self.name = name`.
# 
# </font>
# </div>

# # References

# <div class="alert alert-warning">
# <font color=black>
# 
# - Jeff Knupp, Everything I know about Python, old blog post no longer available online?
# 
# </font>
# </div>

# In[ ]:




