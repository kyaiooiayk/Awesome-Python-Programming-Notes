#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Introduction" data-toc-modified-id="Introduction-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Introduction</a></span></li><li><span><a href="#Errors-and-Exceptions" data-toc-modified-id="Errors-and-Exceptions-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Errors and Exceptions</a></span><ul class="toc-item"><li><span><a href="#Runtime-Errors" data-toc-modified-id="Runtime-Errors-2.1"><span class="toc-item-num">2.1&nbsp;&nbsp;</span>Runtime Errors</a></span></li></ul></li><li><span><a href="#try-and-except" data-toc-modified-id="try-and-except-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>try and except</a></span><ul class="toc-item"><li><span><a href="#try/except-block-that-catches-all-exceptions?" data-toc-modified-id="try/except-block-that-catches-all-exceptions?-3.1"><span class="toc-item-num">3.1&nbsp;&nbsp;</span><code>try</code>/<code>except</code> block that catches all exceptions?</a></span></li></ul></li><li><span><a href="#Raising-Exceptions" data-toc-modified-id="Raising-Exceptions-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>Raising Exceptions</a></span></li><li><span><a href="#raise-vs.-sys.exit()" data-toc-modified-id="raise-vs.-sys.exit()-5"><span class="toc-item-num">5&nbsp;&nbsp;</span><code>raise</code> vs. <code>sys.exit()</code></a></span></li><li><span><a href="#exit-vs.-sys.exit" data-toc-modified-id="exit-vs.-sys.exit-6"><span class="toc-item-num">6&nbsp;&nbsp;</span><code>exit</code> vs. <code>sys.exit</code></a></span></li><li><span><a href="#finally-clause" data-toc-modified-id="finally-clause-7"><span class="toc-item-num">7&nbsp;&nbsp;</span><code>finally</code> clause</a></span></li><li><span><a href="#Assertions" data-toc-modified-id="Assertions-8"><span class="toc-item-num">8&nbsp;&nbsp;</span>Assertions</a></span></li><li><span><a href="#References" data-toc-modified-id="References-9"><span class="toc-item-num">9&nbsp;&nbsp;</span>References</a></span></li><li><span><a href="#Requirements" data-toc-modified-id="Requirements-10"><span class="toc-item-num">10&nbsp;&nbsp;</span>Requirements</a></span></li></ul></div>

# # Introduction
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-block alert-warning">
# <font color=black>
#
# **What?** Errors and exceptions
#
# </font>
# </div>

# # Errors and Exceptions
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
#
# - There are three type of errors:
#
#     - **Syntax errors:** Errors where the code is not valid Python (generally easy to fix)
#     - **Runtime errors:** Errors where syntactically valid code fails to execute, perhaps due to invalid user input (sometimes easy to fix)
#     - **Semantic errors:** Errors in logic: code executes without a problem, but the result is not what you expect (often very difficult to track-down and fix)
#
#
# - Here we're going to focus on how to deal cleanly with *runtime errors*.
# - As we'll see, Python handles runtime errors via its *exception handling* framework.
#
# </font>
# </div>

# ## Runtime Errors
#
# If you've done any coding in Python, you've likely come across runtime errors.
# They can happen in a lot of ways.
#
# For example, if you try to reference an undefined variable:

# In[3]:


print(Q)


# Or if you try an operation that's not defined:

# In[4]:


1 + "abc"


# Or you might be trying to compute a mathematically ill-defined result:

# In[5]:


2 / 0


# Or maybe you're trying to access a sequence element that doesn't exist:

# In[6]:


L = [1, 2, 3]
L[1000]


# Note that in each case, Python is kind enough to not simply indicate that an error happened, but to spit out a *meaningful* exception that includes information about what exactly went wrong, along with the exact line of code where the error happened.
# Having access to meaningful errors like this is immensely useful when trying to trace the root of problems in your code.

# # try and except
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-info">
# <font color=black>
#
# - The main tool Python gives you for handling runtime exceptions is the try...except clause. Its basic structure is this:
#
# </font>
# </div>

# In[7]:


try:
    print("this gets executed first")
except:
    print("this gets executed only if there is an error")


# Note that the second block here did not get executed: this is because the first block did not return an error.
# Let's put a problematic statement in the ``try`` block and see what happens:

# In[8]:


try:
    print("let's try something:")
    x = 1 / 0  # ZeroDivisionError
except:
    print("something bad happened!")


# Here we see that when the error was raised in the ``try`` statement (in this case, a ``ZeroDivisionError``), the error was caught, and the ``except`` statement was executed.
#
# One way this is often used is to check user input within a function or another piece of code.
# For example, we might wish to have a function that catches zero-division and returns some other value, perhaps a suitably large number like $10^{100}$:

# In[9]:


def safe_divide(a, b):
    try:
        return a / b
    except:
        return 1e100


# In[10]:


safe_divide(1, 2)


# In[11]:


safe_divide(2, 0)


# There is a subtle problem with this code, though: what happens when another type of exception comes up? For example, this is probably not what we intended:

# In[12]:


safe_divide(1, "2")


# <div class="alert alert-info">
# <font color=black>
#
# - Dividing an integer and a string raises a `TypeError`, which our over-zealous code caught and assumed was a ``ZeroDivisionError``!
# - For this reason, it's **nearly always a better idea** to catch exceptions *explicitly*:
# - Please note that we're now catching zero-division errors only, and letting all other errors pass through un-modified.
#
# </font>
# </div>

# In[13]:


def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return 1e100


# In[14]:


safe_divide(1, 0)


# In[15]:


safe_divide(1, "2")


# ## `try`/`except` block that catches all exceptions?

# <div class="alert alert-info">
# <font color=black>
#
# - Sometimes is it tedious to try to catch all the exception, so someone may be tempted to try to write a **catch all statement**.
# - In most cases you are, probably, doing **something wrong** if you are trying to catch any exception. I mean you can simply misspell something in your code and you will even don't know about it. It is a **good practice** to catch specific exceptions.
# - To be more precise, catching all possible exceptions is only a problem if they are **caught silently**.
# - An exception to this general rule is when the caught error messages are printed to `sys.stderr` and possibly logged. That is a perfectly valid and common exception.
# - A simple but not perfect solution is to use `except Exception as e:`.
#
# </font>
# </div>

# In[ ]:


import traceback
import logging

try:
    whatever()
except Exception as e:
    logging.error(traceback.format_exc())
    # Logs the error appropriately.


# In[ ]:


try:
    a = 2 / 0
except Exception as e:
    print(e.__doc__)
    print(e.message)


# <div class="alert alert-info">
# <font color=black>
#
# - The advantage of except Exception over the bare except is that there are a few exceptions that it wont catch, most obviously `KeyboardInterrupt` and `SystemExit`.
#
# </font>
# </div>

# # Raising Exceptions
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-info">
# <font color=black>
#
# - The way you raise your **OWN exceptions** is with the raise statement.
# - We can call `raise` directly as in `raise RuntimeError("my error message")` to see how it works.
# - Keep in mind that `raise` is a python name recognised by python but `RuntimeError` is something you decide. For instance,  something like `value_error` would have been equally OK.
#
# </font>
# </div>

# In[4]:


# Let start with a very simple example
raise RuntimeError("my error message")


# In[6]:


# We'd like to let users know that only positive numbers are allowed!
def fibonacci(N):
    if N < 0:
        raise ValueError("N must be non-negative")
    L = []
    a, b = 0, 1
    while len(L) < N:
        a, b = b, a + b
        L.append(a)
    return L


# In[7]:


fibonacci(10)


# In[8]:


fibonacci(-10)


# <div class="alert alert-info">
# <font color=black>
#
# - There is another option: we could even use a try...except block to handle it!
#
# </font>
# </div>

# In[21]:


N = -10
try:
    print("trying this...")
    print(fibonacci(N))
except ValueError:
    print("Bad value: need to do something else")


# <div class="alert alert-info">
# <font color=black>
#
# - Let's say we'd like to **access** the error message itself.
# - We can do that with this contruct `except ZeroDivisionError as err`.
# - Keep in mind that python needs to know `ZeroDivisionError` exihists. If you had ued something like this `ZeroDivisionError_` it would not have worked.
#
# </font>
# </div>

# In[11]:


try:
    x = 1 / 0
except ZeroDivisionError as err:
    print("Error class is:  ", type(err))
    print("Error message is:", err)


# <div class="alert alert-info">
# <font color=black>
#
# - In addition to built-in exceptions, it is possible to define **custom** exceptions through *class inheritance*.
# - For instance, if you want a special kind of ``ValueError``, you can do this:
#
# </font>
# </div>

# In[13]:


class MySpecialError(ValueError):
    pass


# How you'd call this
raise MySpecialError("here's the message")


# This would allow you to use a ``try``...``except`` block that only catches this type of error:

# In[14]:


try:
    print("do something")
    raise MySpecialError("[informative error message here]")
except MySpecialError:
    print("do something else")


# # `raise` vs. `sys.exit()`
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
#
# - **Why raising an error is better than exiting the program?**
#     - You might be able to skip importing sys.
#     - It makes the code more reusable and portable, so calling code can catch the exception if they want.
#     - It makes it a lot easier to print something to standard error.
#
# </font>
# </div>

# In[2]:


value = 1
import sys

if value < 2:
    sys.exit(1)


# In[3]:


value = 1
if value < 2:
    raise Exception("value <2!")


# <div class="alert alert-info">
# <font color=black>
#
# - Dive a bit more, please remember that `sys.exit()` is the same as raising an exception.
# - This means that python internally calls `sys.exit()` when you raise an exception, but of course the printout is different.
#
# </font>
# </div>

# In[4]:


help(sys.exit)


# <div class="alert alert-info">
# <font color=black>
#
# - However, there is a cacth! `sys.exit` raises an exception, but `SystemExit` is a special type of exception that will not be caught by `except Exception`, so it's harder to work with for consumers of your library than something like a ValueError or IOError.
#
# </font>
# </div>

# In[6]:


# except statement catches the exception whereas
import sys

try:
    sys.exit()
except:
    print("Caught")


# In[7]:


# exits without error
import sys

try:
    sys.exit()
except Exception:
    print("Caught")


# <div class="alert alert-info">
# <font color=black>
#
# - From the discussion above there is that at the end of the day, raising instead of exiting, changes the output.
# - **Why not passing an informative message to exit?** this can be done and you can pass messages to sys.exit.
#
# </font>
# </div>

# # `exit` vs. `sys.exit`
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
#
#
#
# - `exit` is a helper for the interactive shell while `sys.exit` is intended for use in programs.
# - In practice:
#     - If you  use `exit()` in a code and run it in the shell, it shows a message asking whether I want to kill the program or not.
#     - If you use `sys.exit()`,  It closes the program and doesn't create any dialogue box.
#
# - This is because it is designed for use in the interactive shell. So even if you want the dialog, sys.exit() should be used inside programs.
#
# </font>
# </div>

# # `finally` clause
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
#
# - A `finally` clause is always executed before leaving the `try` statement, whether an exception has occured or not.
# - The `finally` clause is also executed on the way out when any other clause of the `try` statement is left via a `break`, `continue` or `return` statement.
#
#
# - In the real world, the `finally` clause is used for releasing external resources that are always useful regardless of what happens inside the function.
#
# </font>
# </div>

# In[2]:


def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("Division by zero!")
    else:
        print("Result is:", result)
    finally:
        print("Executing finally clause")


# In[3]:


divide(2, 1)


# In[4]:


divide(2, 0)


# In[5]:


divide("2", "1")


# # Assertions
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
#
# - Assert statements are a convenient way to insert debugging assertions into a program.
# - Don't use assertions in place of exceptions because assertions can be disabled at run time.
#
# </font>
# </div>

# In[2]:


import numpy as np


def get_variance(y):
    n = len(y)
    assert n > 1, "Sample size must be greater than one."
    return np.sum((y - y.mean()) ** 2) / float(n - 1)


# In[10]:


get_variance(np.array([2, 2, 2]))


# In[11]:


get_variance(np.array([2]))


# # References
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-block alert-warning">
# <font color=black>
#
# - [Whirlwind Tour of Python](http://www.oreilly.com/programming/free/a-whirlwind-tour-of-python.csp)
# - https://stackoverflow.com/questions/4990718/how-can-i-write-a-try-except-block-that-catches-all-exceptions
# - [Don't use sys.exit(1). Raise an Exception or assert False instead.](https://www.reddit.com/r/pythontips/comments/d0aysf/dont_use_sysexit1_raise_an_exception_or_assert/)
# - [Don't use assertions in place of exceptions](https://docs.python.org/3/reference/simple_stmts.html#assert)
# - [Difference between exit() and sys.exit() in Python](https://www.reddit.com/r/pythontips/comments/d0aysf/dont_use_sysexit1_raise_an_exception_or_assert/)
# - [Difference between calling sys.exit() and throwing exception](https://stackoverflow.com/questions/10796821/difference-between-calling-sys-exit-and-throwing-exception)
#
# </font>
# </div>

# # Requirements
# <hr style = "border:2px solid black" ></hr>

# In[1]:


get_ipython().run_line_magic("load_ext", "watermark")
get_ipython().run_line_magic("watermark", "-v -iv")


# In[ ]:
