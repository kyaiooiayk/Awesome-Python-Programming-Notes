#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Introduction" data-toc-modified-id="Introduction-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Introduction</a></span></li><li><span><a href="#Exception-Handling-in-Python" data-toc-modified-id="Exception-Handling-in-Python-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Exception Handling in Python</a></span></li><li><span><a href="#Multiple-Except-Clauses" data-toc-modified-id="Multiple-Except-Clauses-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Multiple Except Clauses</a></span></li><li><span><a href="#Custom-made-Exceptions" data-toc-modified-id="Custom-made-Exceptions-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>Custom-made Exceptions</a></span></li><li><span><a href="#try-and-finally" data-toc-modified-id="try-and-finally-5"><span class="toc-item-num">5&nbsp;&nbsp;</span><code>try</code> and <code>finally</code></a></span></li><li><span><a href="#try,-except-and-finally" data-toc-modified-id="try,-except-and-finally-6"><span class="toc-item-num">6&nbsp;&nbsp;</span><code>try</code>, <code>except</code> and <code>finally</code></a></span></li><li><span><a href="#else-clause" data-toc-modified-id="else-clause-7"><span class="toc-item-num">7&nbsp;&nbsp;</span><code>else</code> clause</a></span></li><li><span><a href="#References" data-toc-modified-id="References-8"><span class="toc-item-num">8&nbsp;&nbsp;</span>References</a></span></li><li><span><a href="#Requirements" data-toc-modified-id="Requirements-9"><span class="toc-item-num">9&nbsp;&nbsp;</span>Requirements</a></span></li></ul></div>

# # Introduction
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-block alert-warning">
# <font color=black>
#
# **What?** Exceptions
#
# </font>
# </div>

# # Exception Handling in Python
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
#
# - Exception handling in Python is very similar to Java.
# - The code, which harbours the risk of an exception, is embedded in a `try-except` block.
#
# </font>
# </div>

# In[12]:


def int_input(prompt):
    try:
        age = int(prompt)
        return age
    except ValueError as e:
        print("Not a proper integer! Try it again")


# In[13]:


int_input(22)


# In[14]:


int_input("five")


# # Multiple Except Clauses
# <hr style = "border:2px solid black" ></hr>

# In[15]:


import sys

try:
    f = open("integers.txt")
    s = f.readline()
    i = int(s.strip())
except IOError as e:
    errno, strerror = e.args
    print("I/O error({0}): {1}".format(errno, strerror))
    # e can be printed directly without using .args:
    # print(e)
except ValueError:
    print("No valid integer in line.")
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise


# # Custom-made Exceptions
# <hr style = "border:2px solid black" ></hr>

# In[16]:


raise SyntaxError("Sorry, my fault!")


# <div class="alert alert-info">
# <font color=black>
#
# - It's possible to create Exceptions yourself.
# - The best or the Pythonic way to do this, consists in defining an exception class which inherits from the Exception class.
#
# </font>
# </div>

# In[17]:


class MyException(Exception):
    pass


raise MyException("An exception doesn't always prove the rule!")


# # `try` and `finally`
# <hr style = "border:2px solid black" ></hr>

#
# <div class="alert alert-info">
# <font color=black>
#
# - So far the try statement had always been paired with except clauses.
# - But there is another way to use it as well. The try statement can be followed by a finally clause.
# - A `finally` clause  is called clean-up or termination clauses, because they must be executed under all circumstances, i.e. a "finally" clause is always executed regardless if an exception occurred in a try block or not.
#
#
# </font>
# </div>

# In[18]:


try:
    x = float(input("Your number: "))
    inverse = 1.0 / x
finally:
    print("There may or may not have been an exception.")
print("The inverse: ", inverse)


# # `try`, `except` and `finally`
# <hr style = "border:2px solid black" ></hr>

# In[20]:


try:
    x = float(input("Your number: "))
    inverse = 1.0 / x
except ValueError:
    print("You should have given either an int or a float")
except ZeroDivisionError:
    print("Infinity")
finally:
    print("There may or may not have been an exception.")


# # `else` clause
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
#
# - The `try`` and `except` statement has an optional else clause. An else block has to be positioned after all the except clauses.
# - An `else` clause will be executed if the try clause doesn't raise an exception.
#
# </font>
# </div>

# In[5]:


import sys

file_name = "./tests.txt"
text = []
try:
    fh = open(file_name, "r")
except IOError:
    print("cannot open", file_name)
else:
    text = fh.readlines()
    fh.close()

if text:
    print(text)


# # References
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-block alert-warning">
# <font color=black>
#
# - https://python-course.eu/python-tutorial/errors-and-exception-handling.php
#
# </font>
# </div>

# # Requirements
# <hr style = "border:2px solid black" ></hr>

# In[1]:


get_ipython().run_line_magic("load_ext", "watermark")
get_ipython().run_line_magic("watermark", "-v -iv")


# In[ ]:
