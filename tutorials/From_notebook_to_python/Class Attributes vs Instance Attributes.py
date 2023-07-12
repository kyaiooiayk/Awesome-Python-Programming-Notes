#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Introduction" data-toc-modified-id="Introduction-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Introduction</a></span></li><li><span><a href="#What-is-encapsulation?" data-toc-modified-id="What-is-encapsulation?-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>What is encapsulation?</a></span></li><li><span><a href="#Example-#1" data-toc-modified-id="Example-#1-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Example #1</a></span></li><li><span><a href="#Example-#2" data-toc-modified-id="Example-#2-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>Example #2</a></span></li><li><span><a href="#References" data-toc-modified-id="References-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>References</a></span></li><li><span><a href="#Requirements" data-toc-modified-id="Requirements-6"><span class="toc-item-num">6&nbsp;&nbsp;</span>Requirements</a></span></li></ul></div>

# # Introduction
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-warning">
# <font color=black>
#
# **What?** Class Attributes vs Instance Attributes
#
# </font>
# </div>

# # What is encapsulation?
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
#
# - Class attributes are the variables defined directly in the class that are shared by all objects of the class.
# - Instance attributes are attributes or properties attached to an instance of a class. Instance attributes are defined in the constructor.
#
#
# | Class Attribute | Instance Attribute |
# |---|---|
# | Defined directly inside a class | Defined inside a constructor using the self parameter |
# | Shared across all objects | Specific to object |
# | classname.class_attribute or object.class_attribute | only object.instance_attribute |
# | Changing value by using classname.class_attribute = value will be reflected to all the objects. | Changing value of instance attribute will not be reflected to other objects |
#
# </font>
# </div>

# # Example #1
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
#
# - The following example demonstrates the use of class attribute count.
# - `count` is an attribute in the Student class. Whenever a new object is created, the value of count is incremented by 1.
#
# </font>
# </div>

# In[1]:


class Student:
    count = 0

    def __init__(self):
        Student.count += 1


# In[2]:


Student.count


# In[3]:


std1 = Student()
print(Student.count)
# print(std1.count)

std2 = Student()
print(Student.count)
# print(std2.count)


# In[4]:


Student.count


# # Example #2
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
#
# - The following demonstrates the instance attributes.
# - Now, you can specify the values while creating an instance, as shown below.
#
# </font>
# </div>

# In[5]:


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age


# In[6]:


std = Student("Bill", 25)
std.age


# In[7]:


std.name = "Steve"
std.age = 45
print(std.name)
print(std.age)


# # References
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-warning">
# <font color=black>
#
# - https://www.tutorialsteacher.com/articles/class-attributes-vs-instance-attributes-in-python
#
# </font>
# </div>

# # Requirements
# <hr style = "border:2px solid black" ></hr>

# In[8]:


get_ipython().run_line_magic("load_ext", "watermark")
get_ipython().run_line_magic("watermark", "-v -iv")
