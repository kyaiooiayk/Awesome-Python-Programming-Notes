#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Introduction" data-toc-modified-id="Introduction-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Introduction</a></span></li><li><span><a href="#Class-decorators" data-toc-modified-id="Class-decorators-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Class decorators</a></span></li><li><span><a href="#@property" data-toc-modified-id="@property-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>@property</a></span></li><li><span><a href="#Descriptors" data-toc-modified-id="Descriptors-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>Descriptors</a></span></li><li><span><a href="#Example-#1" data-toc-modified-id="Example-#1-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>Example #1</a></span><ul class="toc-item"><li><span><a href="#Will-not-work-at-instantiation" data-toc-modified-id="Will-not-work-at-instantiation-5.1"><span class="toc-item-num">5.1&nbsp;&nbsp;</span>Will not work at instantiation</a></span></li></ul></li><li><span><a href="#Example-#2" data-toc-modified-id="Example-#2-6"><span class="toc-item-num">6&nbsp;&nbsp;</span>Example #2</a></span></li><li><span><a href="#Avoid-running-a-specific-part-of-the-code" data-toc-modified-id="Avoid-running-a-specific-part-of-the-code-7"><span class="toc-item-num">7&nbsp;&nbsp;</span>Avoid running a specific part of the code</a></span></li><li><span><a href="#@property-with-no-setter-method" data-toc-modified-id="@property-with-no-setter-method-8"><span class="toc-item-num">8&nbsp;&nbsp;</span><code>@property</code> with no <code>setter</code> method</a></span></li><li><span><a href="#@property-vs.-object-attributes" data-toc-modified-id="@property-vs.-object-attributes-9"><span class="toc-item-num">9&nbsp;&nbsp;</span><code>@property</code> vs. object attributes</a></span></li><li><span><a href="#References" data-toc-modified-id="References-10"><span class="toc-item-num">10&nbsp;&nbsp;</span>References</a></span></li></ul></div>

# # Introduction
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-block alert-warning">
# <font color=black>
#
# **What?** @property
#
# </font>
# </div>

# # Class decorators
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-block alert-info">
# <font color=black>
#
# - `@property` The Pythonic way to introduce attributes is to make them public, and not introduce getters and setters to retrieve or change them.
# - `@classmethod` To add additional constructor to the class.
# - `@staticmethod` To attach functions to classes so people won't misuse them in wrong places.
#
# </font>
# </div>

# # @property
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-block alert-info">
# <font color=black>
#
# - The Pythonic way to introduce attributes is to make them public, and not introduce getters and setters to retrieve or change them.
# - Give access to the value like it is an attribute **instead** of a method
# - By using `@property`, you can "reuse" the name of a property to avoid creating new names for the getters, setters, and deleters.
# - They are often used to validate the value of an attribute. Essentially they make the process much easier.
# - This makes methods act as getters, setters, or deleters when we define properties in a class.
#
# </font>
# </div>

# # Descriptors
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-block alert-info">
# <font color=black>
#
# - Properties, a common kind of descriptor.
# - In general, a **descriptor** is an attribute value that has one of the methods in the descriptor protocol. Those methods are `__get__()`, `__set__()`, and `__delete__()`. If any of those methods are defined for an attribute, it is said to be a descriptor.
#
# </font>
# </div>

# # Example #1
# <hr style = "border:2px solid black" ></hr>

# In[1]:


class House:
    def __init__(self, price):
        self.price = price


# In[2]:


house1 = House(10)


# In[3]:


house1.price


# In[4]:


# Since the attribute is public I can access and modify it
house1.price = 20


# In[5]:


house1.price


# <div class="alert alert-block alert-info">
# <font color=black>
#
# - Let's say that you are asked to make this attribute protected (non-public) and validate the new value before assigning it.
# - Specifically, you need to check if the value is a positive float. How would you do that? Let's see.
# - With `@property` you will be able to add getters and setters "behind the scenes" **without affecting** the syntax that you used to access or modify the attribute when it was public.
#
# </font>
# </div>

# In[6]:


class House_v1:
    """House

    We'd like to create a class where it only
    attribute is its price. We'd like to enforce a check on
    this value: no negative value area allowed. So the user
    we'll never misuse them.
    """

    def __init__(self, price):
        """
        Please note that there is un underscored in
        front of price!
        """
        self._price = price

    # This is essentially the getter method
    @property
    def price(self):
        print("getter")
        return self._price

    @price.setter
    def price(self, new_price):
        print("setter")
        if new_price > 0 and isinstance(new_price, float):
            self._price = new_price
        else:
            print("Please enter a valid price: float and >0.0")

    @price.deleter
    def price(self):
        print("deleter")
        del self._price


# In[7]:


house2 = House_v1(10)


# In[8]:


house2.price


# <div class="alert alert-block alert-info">
# <font color=black>
#
# - Please note that the price attribute is now considered "protected" by the check.
# - To help developer ditinguish the two attribute we now add `_` before `price` as in `self._price`.
# - We are not changing the syntax at all, but we are actually using the getter as an intermediary to avoid accessing the data directly.
#
# </font>
# </div>

# In[9]:


house2.price = -10


# <div class="alert alert-block alert-info">
# <font color=black>
#
# - You can define three methods for a property:
#     - A `getter` - to access the value of the attribute.
#     - A `setter` - to set the value of the attribute.
#     - A `deleter` - to delete the instance attribute.
#
#
# - You don't necessarily have to define all three methods for every property.
#
# </font>
# </div>

# In[10]:


del house2.price


# In[11]:


# Which will throw an error as we have just destroyed that property
house2.price


# ## Will not work at instantiation
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
#
# - The decorator `@property` would not be called at instantiation!
#
# </font>
# </div>

# In[12]:


house2 = House_v1(-10)


# In[13]:


house2.price


# In[14]:


house2.price = -10


# # Example #2
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
#
# - When a method is decorated with `@property`, it can be accessed like an attribute (i.e., without parentheses) instead of like a method (i.e., with parentheses). This can be useful for creating a more intuitive and user-friendly API for a class.
# - Additionally, @property can be used with `@property_name.setter` method, which allows to set the value of the attribute. This allows for **read-only** properties, and it can be used to make sure that an attribute cannot be set to an invalid value.
# - It is important to note that, the methods decorated with `@property` are read-only, if you want to change the value of the attribute you need to use a `@property_name.setter` method.
# - It is a way to make sure that the attribute is always set to a valid value.
#
# </font>
# </div>

# In[21]:


class Person:
    def __init__(self):
        self._name = ""

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if len(value) > 3:
            self._name = value
        else:
            raise ValueError("name should be at least 3 characters long")


# In[23]:


p = Person()
p.name = "Nick"
name = p.name
name


# In[25]:


p = Person()
p.name = "N"
name = p.name
name


# In[ ]:


# # Avoid running a specific part of the code
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
#
# - Let's assume we have a routine made of many parts.
# - One of the section of the code is very expensive and we'd like to run only once.
# - We could use property to trigger this.
#
# </font>
# </div>

# In[1]:


class A:
    def __init__(self):
        self._value = None
        self.expensive_output = None

    @property
    def value(self):
        if not self._value:
            print("computing for the first time!")
            # Suppose this is a very expensive process!
            self._value = 100
        return self._value

    def compute_result(self):
        return self.value


# In[2]:


a = A()


# In[3]:


# Call it once for the first time
a.value


# In[4]:


# Does not recompute again!
a.value


# # `@property` with no `setter` method
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
#
# - In this example, the value method is decorated with the `@property` decorator, which makes it a read-only property.
# - Attempting to set the value of value raises an AttributeError because there is no setter method for the property.
# - **Why would you want to do it?** Useful in situations where you want to make sure that the property cannot be modified from outside the class.
# - Example where you may want to use this approach:
#     - You want to ensure that the property is always computed based on some other data or state, and cannot be set directly.
#     -You want to make sure that the property is only modified through specific methods or actions in the class, to maintain the integrity of the data or state.
#     - You want to make sure that the property is read-only, and that any attempt to set it will raise an error.
#     - Additionally, this approach can also be useful to provide a simple and consistent way of accessing data that is stored within a class, but should not be modified directly.
#     - In general, this approach can be useful to create a more robust and maintainable codebase by enforcing encapsulation, and by providing a clear and consistent interface for interacting with the class.
#
# </font>
# </div>

# In[27]:


class MyClass:
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value


# In[29]:


obj = MyClass(5)


# In[ ]:


# prints 5
print(obj.value)


# In[30]:


# raises AttributeError, because there is no setter method for 'value
obj.value = 10


# # `@property` vs. object attributes
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
#
# - With a property you have complete control of its `getter`, `setter` and `deleter` methods, which you don't have (if not using caveats) with an attribute.
# - **If not using caveats** meant in a non-pythonic way.
# - This ("complete control") can be done with "non-property" attributes as well though, just without such simple decorators.
#
# </font>
# </div>

# # References
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-block alert-warning">
# <font color=black>
#
# - https://www.freecodecamp.org/news/python-property-decorator/
# - https://stackoverflow.com/questions/7374748/whats-the-difference-between-a-python-property-and-attribute
# - https://python-course.eu/oop/properties-vs-getters-and-setters.php
# - [Having @property only run once](https://stackoverflow.com/questions/50934180/having-property-only-run-once)
# - [What is a descriptor?](https://docs.python.org/3/howto/descriptor.html#descriptor-protocol)
#
# </font>
# </div>

# In[ ]:
