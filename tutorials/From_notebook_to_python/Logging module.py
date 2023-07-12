#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Introduction" data-toc-modified-id="Introduction-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Introduction</a></span></li><li><span><a href="#Imports" data-toc-modified-id="Imports-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Imports</a></span></li><li><span><a href="#Logging" data-toc-modified-id="Logging-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Logging</a></span></li><li><span><a href="#Exercise-#1" data-toc-modified-id="Exercise-#1-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>Exercise #1</a></span></li><li><span><a href="#Exercise-#2" data-toc-modified-id="Exercise-#2-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>Exercise #2</a></span></li><li><span><a href="#Logging-Exception" data-toc-modified-id="Logging-Exception-6"><span class="toc-item-num">6&nbsp;&nbsp;</span>Logging Exception</a></span></li><li><span><a href="#Clean-up" data-toc-modified-id="Clean-up-7"><span class="toc-item-num">7&nbsp;&nbsp;</span>Clean-up</a></span></li><li><span><a href="#References" data-toc-modified-id="References-8"><span class="toc-item-num">8&nbsp;&nbsp;</span>References</a></span></li></ul></div>

# # Introduction
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-block alert-warning">
# <font color=black>
#
# **What?** Logging module
#
# </font>
# </div>

# # Imports
# <hr style="border:2px solid black"> </hr>

# In[1]:


import logging
import traceback
from imp import reload


# # Logging
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-info">
# <font color=black>
#
# - Python's logging modules allows us to better control all out print statements. This become more and more important as our application grows in size an away from a quick and dirty code snippet.
#
# - There are 5 different kinds of logging levels. Levels allow us to to specify exactly what we want to log by separating them into categories. The description of each of these is as follows:
#
#     - `DEBUG`: Detailed debug information, typically of interest only when diagnosing problems.
#     - `INFO`: Confirmation that things are working as expected.
#     - `WARNING`: An indication that something unexpected happened, or indicative of some problem in the near future (e.g. disk space low). The software is still working as expected.
#     - `ERROR`: Due to a more serious problem, the software has not been able to perform some function.
#     - `CRITICAL`: A serious error, indicating that the program itself may be unable to continue running.
#
# - The default level is WARNING, meaning that it will capture anything that is a warning or above, and ignore the DEBUG and INFO level. we can change this behavior using the basicConfig method.
#
# </font>
# </div>

# # Exercise #1
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-info">
# <font color=black>
#
# - In the following not only did we change the logging level, but also specify a logging file to write the log to, and the format
# - The format we specified here is simply the time, the level name and the message that we'll later specify
#
# </font>
# </div>

# In[2]:


# jupyter notebook already uses logging, thus we reload the module to make it work in notebooks
reload(logging)


logging.basicConfig(
    filename="test.log",
    level=logging.DEBUG,
    format="%(asctime)s:%(levelname)s:%(message)s",
)


def add(x, y):
    """Add Function"""
    return x + y


def subtract(x, y):
    """Subtract Function"""
    return x - y


def multiply(x, y):
    """Multiply Function"""
    return x * y


def divide(x, y):
    """Divide Function"""
    return x / y


# In[3]:


num1 = 20
num2 = 10

# add logging debugrmation instead of print statement
# to record what was going on, note that if we were to
# run it for multiple
add_result = add(num1, num2)
logging.debug("Add: {} + {} = {}".format(num1, num2, add_result))

sub_result = subtract(num1, num2)
logging.debug("Sub: {} - {} = {}".format(num1, num2, sub_result))

mul_result = multiply(num1, num2)
logging.debug("Mul: {} * {} = {}".format(num1, num2, mul_result))

div_result = divide(num1, num2)
logging.debug("Div: {} / {} = {}".format(num1, num2, div_result))


# In[4]:


# Inspecting the file
get_ipython().system("cat test.log")


# # Exercise #2
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-info">
# <font color=black>
#
# - The code chunk logs the information in the root logger.
# - If we have multiple scripts that does the logging, they will get logged to the same place, which might not be ideal.
# - Thus we can create a separate logger for each module.
#
# </font>
# </div>

# In[5]:


# then specify the module's logger, the logger's level
# and add the handler to the logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)

# boiler plate, set the format using Formatter,
# and set the file to log to with FileHandler
formatter = logging.Formatter("%(asctime)s:%(levelname)s:%(message)s")
file_handler = logging.FileHandler("math.log")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

# note that we do not need to reload the logging
# module this time, as it will not have conflict
# with jupyter notebook's logging behavior


def add(x, y):
    """Add Function"""
    return x + y


def subtract(x, y):
    """Subtract Function"""
    return x - y


def multiply(x, y):
    """Multiply Function"""
    return x * y


def divide(x, y):
    """Divide Function"""
    try:
        result = x / y
    except ZeroDivisionError:
        # by calling .exception it will produce the traceback,
        # which is helpful for knowing where the bug occurred
        logger.exception("Tried to divide by 0")
    else:
        return result


# In[6]:


num1 = 20
num2 = 0

# note that we'll use the logger we explicitly created
# to log to message as oppose to logging in the last example
add_result = add(num1, num2)
logger.info("Add: {} + {} = {}".format(num1, num2, add_result))

sub_result = subtract(num1, num2)
logger.info("Sub: {} - {} = {}".format(num1, num2, sub_result))

mul_result = multiply(num1, num2)
logger.info("Mul: {} * {} = {}".format(num1, num2, mul_result))

div_result = divide(num1, num2)
logger.info("Div: {} / {} = {}".format(num1, num2, div_result))


# In[7]:


get_ipython().system("cat math.log")


# # Logging Exception
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-info">
# <font color=black>
#
# - In the previous section, we've were logging the exception to the log file. This is actually an important practice and should not be taken lightly.
# - When using try and except to catch exceptions, we should be more diligent in the way we handle the exceptions. In other words, NEVER do the following.
#
# </font>
# </div>

# In[8]:


num1 = 20
num2 = 0

result = None
try:
    result = num1 / num2
except:  # or except Exception:
    pass

result


# <div class="alert alert-info">
# <font color=black>
#
# - It might be quick for us as a developer to simply ignore the exception so that we can move on with our life and not worry about dealing with the exception. But when we do this, it is actually doing a massive disservice as it not only swallows up the various errors that might occur, even the ones we weren't expecting when writing try, expect block, but also throws away the stack trace, which provides useful information to speed up our bugging process when an error occurs.
#
# - This is not to say that we should not be using try and expect to catch Exception, as this ensures our critical or long-running process doesn't go down due to some unexpected error. It is to enforce the fact that we should **not be silently** swallowing the error.
#
# - The solution to this is to use a more specific exception type and log the full stack trace. In the function we've defined, we:
#
#     - Use the `ZeroDivisionError` to specify what errors we were expecting when writing the try, except block.
#     - We also leverage logging object's exception method.
#
# </font>
# </div>

# In[9]:


def divide(x, y):
    """Divide Function"""
    try:
        result = x / y
    except ZeroDivisionError:
        # by calling .exception it will produce the traceback,
        # which is helpful for knowing where the bug occurred
        logger.exception("Tried to divide by 0")
    else:
        return result


# <div class="alert alert-info">
# <font color=black>
#
# - If for some reason, our application does logging in some other way, then we can use the trackback module to format the exception's stack trace.
#
# </font>
# </div>

# In[10]:


def divide(x, y):
    """Divide Function"""
    try:
        result = x / y
        output = {"result": result}
    except ZeroDivisionError as ex:
        error_message = log_traceback(ex)
        output = {"result": None, "error": error_message}

    return output


def log_traceback(ex):
    """Format full stack trace into a single string."""
    traceback_lines = traceback.format_exception(ex.__class__, ex, ex.__traceback__)
    traceback_text = "".join(traceback_lines)
    return traceback_text


# In[11]:


output = divide(20, 0)
output


# # Clean-up
# <hr style="border:2px solid black"> </hr>

# In[12]:


get_ipython().system("rm math.log test.log")


# # References
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-block alert-warning">
# <font color=black>
#
# - http://nbviewer.jupyter.org/github/ethen8181/machine-learning/blob/master/python/logging.ipynb
# - [Youtube: Python Tutorial: Logging Basics - Logging to Files, Setting Levels, and Formatting](https://www.youtube.com/watch?v=-ARI4Cz-awo)
# - [Toutube: Python Tutorial: Logging Advanced - Loggers, Handlers, and Formatters](https://www.youtube.com/watch?v=jxmzY9soFXg&feature=youtu.be)
# - [Blog: The Most Diabolical Python Antipattern](https://realpython.com/the-most-diabolical-python-antipattern/)
# - https://docs.python.org/3/library/logging.html#logrecord-attributes
# - http://stackoverflow.com/questions/18786912/get-output-from-the-logging-module-in-ipython-notebook
#
# </font>
# </div>

# In[ ]:
