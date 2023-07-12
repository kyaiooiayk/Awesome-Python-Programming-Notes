#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Introduction" data-toc-modified-id="Introduction-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Introduction</a></span></li><li><span><a href="#Usage" data-toc-modified-id="Usage-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Usage</a></span></li><li><span><a href="#Storing-last-value" data-toc-modified-id="Storing-last-value-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Storing last value</a></span></li><li><span><a href="#For-Ignoring-the-values" data-toc-modified-id="For-Ignoring-the-values-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>For Ignoring the values</a></span></li><li><span><a href="#Give-special-meanings-to-name-of-variables-and-functions" data-toc-modified-id="Give-special-meanings-to-name-of-variables-and-functions-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>Give special meanings to name of variables and functions</a></span></li><li><span><a href="#Avoid-conflict-with-class-keyword" data-toc-modified-id="Avoid-conflict-with-class-keyword-6"><span class="toc-item-num">6&nbsp;&nbsp;</span>Avoid conflict with <code>class</code> keyword</a></span></li><li><span><a href="#__-double_leading_underscore" data-toc-modified-id="__-double_leading_underscore-7"><span class="toc-item-num">7&nbsp;&nbsp;</span><code>__</code> double_leading_underscore</a></span></li><li><span><a href="#Leading-and-trailing-dunder" data-toc-modified-id="Leading-and-trailing-dunder-8"><span class="toc-item-num">8&nbsp;&nbsp;</span>Leading and trailing dunder</a></span></li><li><span><a href="#As-Internationalization(i18n)/Localization(l10n)-functions" data-toc-modified-id="As-Internationalization(i18n)/Localization(l10n)-functions-9"><span class="toc-item-num">9&nbsp;&nbsp;</span>As Internationalization(i18n)/Localization(l10n) functions</a></span></li><li><span><a href="#To-separate-the-digits-of-number-literal-value" data-toc-modified-id="To-separate-the-digits-of-number-literal-value-10"><span class="toc-item-num">10&nbsp;&nbsp;</span>To separate the digits of number literal value</a></span></li><li><span><a href="#References" data-toc-modified-id="References-11"><span class="toc-item-num">11&nbsp;&nbsp;</span>References</a></span></li></ul></div>

# # Introduction
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-block alert-warning">
# <font color=black>
#
# **What?** Underscore (_)
#
# </font>
# </div>

# # Usage
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
#
# - There are 5 cases:
#     - For storing the value of last expression in interpreter.
#     - For ignoring the specific values. (so-called “I don’t care”)
#     - To give special meanings and functions to name of vartiables or functions.
#     - To use as ‘Internationalization(i18n)’ or ‘Localization(l10n)’ functions.
#     - To separate the digits of number literal value.
#
# </font>
# </div>

# # Storing last value
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
#
# - For storing the value of last expression in interpreter.
# - Useful if have just computed a huge result and you forgot to assign it to a variable.
#
# </font>
# </div>

# In[1]:


5


# In[2]:


_


# In[3]:


a = _
a


# # For Ignoring the values
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-block alert-info">
# <font color=black>
#
# - The underscore is also used for ignoring the specific values.
# - If you don’t need the specific values or the values are not used, just assign the values to underscore.
#
# </font>
# </div>

# In[7]:


# Ignore a value when unpacking
x, _, y = (1, 2, 3)
x


# In[8]:


# Ignore the multiple values. It is called "Extended Unpacking" which is available in only Python 3.
x, *_, y = (1, 2, 3, 4, 5)  # x = 1, y = 5


# In[9]:


x


# In[10]:


y


# In[11]:


# Ignore the index
a = 0
for _ in range(10):
    a += 1
print(a)


# # Give special meanings to name of variables and functions
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
#
# - This convention is used for declaring private variables, functions, methods and classes in a module. Anything with this convention are ignored in from module import *.
#
# - However, of course, Python does not supports truly private, so we can not force somethings private ones and also can call it directly from other modules. So sometimes we say it **weak internal use indicator**.
#
# </font>
# </div>

# In[22]:


class _Base:  # private
    _hidden_factor = 2  # private variable

    def __init__(self, price):
        self._price = price

    def _double_price(self):  # private method
        return self._price * self._hidden_factor

    def get_double_price(self):
        return self._double_price()


# In[23]:


obj = _Base(100)


# In[25]:


obj._hidden_factor


# In[27]:


obj._double_price()


# In[28]:


obj.get_double_price()


# # Avoid conflict with `class` keyword
# <hr style = "border:2px solid black" ></hr>

# In[ ]:


Tkinter.Toplevel(master, class_="ClassName")  # Avoid conflict with 'class' keyword

list_ = List.objects.get(1)  # Avoid conflict with 'list' built-in type


# # `__` double_leading_underscore
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
#
# - This is about syntax rather than a convention. double underscore will mangle the attribute names of a class to avoid conflicts of attribute names between classes.
#
# - This is the so-called **mangling** that means that the compiler or interpreter modify the variables or function names with some rules, not use as it is.
#
# - The mangling rule of Python is adding the `_ClassName` to front of attribute names are declared with double underscore. That is, if you write method named `__method` in a class, the name will be mangled in `_ClassName__method` form.
#
# </font>
# </div>

# In[33]:


class A:
    def _single_method(self):
        pass

    def __double_method(self):  # for mangling
        pass


# In[37]:


a = A()


# In[40]:


dir(a)


# <div class="alert alert-info">
# <font color=black>
#
#
# - Because of the attributes named with double underscore will be mangled like above, we can not access it with `ClassName.__method`.
# - Sometimes, some people use it as like real private ones using these features, but it is not for private and not recommended for that.
#
# </font>
# </div>

# # Leading and trailing dunder
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
#
# - This convention is used for special variables or methods (so-called “magic method”) such as `__init__`, `__len__`. These methods provides special syntactic features or does special things.
#
# - For example, `__file__` indicates the location of Python file, `__eq__` is executed when `a == b` expression is excuted.
#
# - A user of course can make custom special method, it is very rare case, but often might modify the some built-in special methods.
#
#
# </font>
# </div>

# # As Internationalization(i18n)/Localization(l10n) functions
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
#
# - It is just convention, does not have any syntactic functions. That is, the underscore does not means i18n/l10n, and it is just a convention that binds the i18n/l10n to underscore variable has been from C convention.
#
# - The built-in library gettext which is for i18n/l10n uses this convention, and Django which is Python web framework supports i18n/l10n also introduces and uses this convention.
#
# - **Localise your program**. Localising a program means making it suitable for different regions/countries. When you do that, one of the things that you have to do is translate the strings in your program, so that they can be read in many different languages.
#
# </font>
# </div>

# # To separate the digits of number literal value
# <hr style = "border:2px solid black" ></hr>

# In[42]:


dec_base = 1_000_000
bin_base = 0b_1111_0000
hex_base = 0x_1234_ABCD


# In[43]:


print(dec_base)


# In[44]:


print(bin_base)


# In[45]:


print(hex_base)


# # References
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-block alert-warning">
# <font color=black>
#
# - https://hackernoon.com/understanding-the-underscore-of-python-309d1a029edc
#
# </font>
# </div>

# In[ ]:
