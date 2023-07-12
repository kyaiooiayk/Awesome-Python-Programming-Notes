#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Introduction" data-toc-modified-id="Introduction-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Introduction</a></span></li><li><span><a href="#Using-C-style-string-formatting" data-toc-modified-id="Using-C-style-string-formatting-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Using C-style string formatting</a></span></li><li><span><a href="#Using-the-Python-3-.format-method-from-strings" data-toc-modified-id="Using-the-Python-3-.format-method-from-strings-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Using the Python 3 <code>.format</code> method from strings</a></span></li><li><span><a href="#Using-f-strings,-from-Python-3.6+" data-toc-modified-id="Using-f-strings,-from-Python-3.6+-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>Using f-strings, from Python 3.6+</a></span></li><li><span><a href="#Conclusions" data-toc-modified-id="Conclusions-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>Conclusions</a></span></li><li><span><a href="#References" data-toc-modified-id="References-6"><span class="toc-item-num">6&nbsp;&nbsp;</span>References</a></span></li></ul></div>

# # Introduction
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-block alert-warning">
# <font color=black>
#
# **What?** String formatting
#
# </font>
# </div>

# # Using C-style string formatting
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
#
# - This string formatting, borrowed from the similar C syntax.
#
# - The C-style formatting, which is the one that has been around the longer, is characterised by a series of percent signs ("%") that show up in the template strings. (By “template strings”, I mean the strings in which we want to fill in the gaps.)
#
# - These percent signs indicate the places where the bits of information should go, and the character that
# comes next (above, we’ve seen "%s" and "%d") determine how the information being passed in is treated.
#
# </font>
# </div>

# In[4]:


def language_info_cstyle(language, users_estimate):
    return "%s rocks! Did you know that %s has around %d users?!" % (
        language,
        language,
        users_estimate,
    )


language_info_cstyle("Python", 10)


# # Using the Python 3 `.format` method from strings
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
#
# - This string formatting was introduced in PEP 3101.
#
# - The string method .format is, like the name suggests, a method of the string type. This means that you typically have a format string and, when you get access to the missing pieces of information, you just call the .format method on that string.
#
# - Strings that use the method .format for formatting are typically characterised by the occurrence of a series of curly braces "{}" within the string. It is also common to find that the method .format is called where/when the string literal is defined.
#
# </font>
# </div>

# In[5]:


def language_info_format(language, users_estimate):
    return "{} rocks! Did you know that {} has around {} users?!".format(
        language, language, users_estimate
    )


language_info_format("Python", 10)


# # Using f-strings, from Python 3.6+
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
#
#
# - This string formatting which uses the new f-strings was introduced in PEP 498 for Python 3.6+.
#
# - Literal string interpolation is the process through which you interpolate values into strings.
#
# - Interpolate here means insert.
#
# </font>
# </div>

# In[6]:


def language_info_fstring(language, users_estimate):
    return (
        f"{language} rocks! Did you know that {language}"
        + f" has around {users_estimate} users?!"
    )


language_info_fstring("Python", 10)


# # Conclusions
# <hr style = "border:2px solid black" ></hr>

#
# <div class="alert alert-danger">
# <font color=black>
#
# - Don’t use old-style string formatting: use `f-strings` whenever possible, and then `.format` in the
# other occasions.
#
# </font>
# </div>

# # References
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-block alert-warning">
# <font color=black>
#
# - https://mathspp.com/blog/pydonts
#
# </font>
# </div>

# In[ ]:
