#!/usr/bin/env python
# coding: utf-8

# # Introduction
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-warning">
# <font color=black>
#
# **What?** The __future__ module
#
# </font>
# </div>

# # What is it there for?
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
#
# - The `__future__` is a real module.
# - It serves three purposes:
#
#     - **Purpouse #1**: To avoid confusing existing tools that analyze import statements and expect to find the modules they’re importing.
#     - **Purpouse #2**: To ensure that future statements run under releases prior to 2.1 at least yield runtime exceptions (the import of __future__ will fail, because there was no module of that name prior to 2.1).
#     - **Purpouse #3**: To document when incompatible changes were introduced, and when they will be — or were — made mandatory. This is a form of executable documentation, and can be inspected programmatically via importing __future__ and examining its contents.
#
# </font>
# </div>

# # Example #1
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
#
# - **Case #1**: In python 2.7.x without `__future__` import:
# ```
# print(8/7)  # prints 1
# print(8//7) # prints 1
# ```
# - **Case #1**: In python 2.7.x with `__future__` import:
# ```
# print(8/7)  # prints 1.1428571428571428
# print(8//7) # prints 1
# ```
# - The internal difference is that without that import, `/` is mapped to the `__div__()` method, while with it, `__truediv__()` is used. In any case, `//` calls `__floordiv__()`.
#
# </font>
# </div>

# <div class="alert alert-info">
# <font color=black>
#
# - **Case #3**: In python 3.x:
# ```
# print(8/7)  # prints 1.1428571428571428
# print(8//7) # prints 1
# ```
#
# </font>
# </div>

# # Example #2
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
#
# - `__future__` is a pseudo-module which programmers can use to enable new language features which are not compatible with the current interpreter. For example, the expression 11/4 currently evaluates to 2. If the module in which it is executed had enabled true division by executing:
# ```
# from __future__ import division
# ```
#
# - The expression 11/4 would evaluate to 2.75. By importing the __future__ module and evaluating its variables, you can see when a new feature was first added to the language and when it will become the default:
# ```
# >>> import __future__
# >>> __future__.division
# _Feature((2, 2, 0, 'alpha', 2), (3, 0, 0, 'alpha', 0), 8192)
# ```
#
# </font>
# </div>

# # Conclusions
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-danger">
# <font color=black>
#
# - `__future__` is a pseudo-module which programmers can use to enable new language features which are not compatible with the current interpreter.
#
# </font>
# </div>

# # References
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-warning">
# <font color=black>
#
# - https://docs.python.org/3/library/__future__.html
# - https://stackoverflow.com/questions/7075082/what-is-future-in-python-used-for-and-how-when-to-use-it-and-how-it-works
#
# </font>
# </div>

# In[ ]:
