#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Introduction" data-toc-modified-id="Introduction-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Introduction</a></span></li><li><span><a href="#What-is-it?" data-toc-modified-id="What-is-it?-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>What is it?</a></span></li><li><span><a href="#Task" data-toc-modified-id="Task-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Task</a></span></li><li><span><a href="#Refactor-step-#1---automatic-style-formatting" data-toc-modified-id="Refactor-step-#1---automatic-style-formatting-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>Refactor step #1 - automatic style formatting</a></span></li><li><span><a href="#Refactor-step-#2---Naming" data-toc-modified-id="Refactor-step-#2---Naming-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>Refactor step #2 - Naming</a></span></li><li><span><a href="#Refactor-step-#3---Traversing-data-and-indices" data-toc-modified-id="Refactor-step-#3---Traversing-data-and-indices-6"><span class="toc-item-num">6&nbsp;&nbsp;</span>Refactor step #3 - Traversing data and indices</a></span></li><li><span><a href="#Refactor-step-#4---Nest-only-what-is-needed" data-toc-modified-id="Refactor-step-#4---Nest-only-what-is-needed-7"><span class="toc-item-num">7&nbsp;&nbsp;</span>Refactor step #4 - Nest only what is needed</a></span></li><li><span><a href="#Refactor-step-#5---Conditional-assignment-and-conditional-expressions" data-toc-modified-id="Refactor-step-#5---Conditional-assignment-and-conditional-expressions-8"><span class="toc-item-num">8&nbsp;&nbsp;</span>Refactor step #5 - Conditional assignment and conditional expressions</a></span></li><li><span><a href="#Refactor-step-#6---Truthy-and-Falsy" data-toc-modified-id="Refactor-step-#6---Truthy-and-Falsy-9"><span class="toc-item-num">9&nbsp;&nbsp;</span>Refactor step #6 - Truthy and Falsy</a></span></li><li><span><a href="#Refactor-step-#7---List-comprehensions-versus-appending" data-toc-modified-id="Refactor-step-#7---List-comprehensions-versus-appending-10"><span class="toc-item-num">10&nbsp;&nbsp;</span>Refactor step #7 - List comprehensions versus appending</a></span></li><li><span><a href="#Refactor-step-#8---Avoid-long-lines" data-toc-modified-id="Refactor-step-#8---Avoid-long-lines-11"><span class="toc-item-num">11&nbsp;&nbsp;</span>Refactor step #8 - Avoid long lines</a></span></li><li><span><a href="#Refactor-step-#9---Auxiliary-variables" data-toc-modified-id="Refactor-step-#9---Auxiliary-variables-12"><span class="toc-item-num">12&nbsp;&nbsp;</span>Refactor step #9 - Auxiliary variables</a></span></li><li><span><a href="#Refactor-step-#10---Reduntant-list-comprehensions" data-toc-modified-id="Refactor-step-#10---Reduntant-list-comprehensions-13"><span class="toc-item-num">13&nbsp;&nbsp;</span>Refactor step #10 - Reduntant list comprehensions</a></span></li><li><span><a href="#References" data-toc-modified-id="References-14"><span class="toc-item-num">14&nbsp;&nbsp;</span>References</a></span></li></ul></div>

# # Introduction
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-warning">
# <font color=black>
#
# **What?** Code refactoring
#
# </font>
# </div>

# # What is it?
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-info">
# <font color=black>
#
# - **Short definition of refactoring**: changing the code without changing its behaviour
#
# - Refactoring the source code of an application or piece of software aims to improve operation without altering functionality.
#
# - Making your code better might mean different things:
#     - Easier to maintain
#     - Easier to explain
#     - Faster
#     - etc ...
#
# </font>
# </div>

# # Task
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-info">
# <font color=black>
#
# - Write a function that changes the casing of its letters:
#     - letters in even positions should become uppercase
#     - letters in odd positions should become lowercase
#
# </font>
# </div>

# In[ ]:


def myfunc(a): empty=[]
    for i in range(len(a)):
        if i%2==0:
            empty.append(a[i].upper())
        else:
            empty.append(a[i].lower())
    return "".join(empty)


# # Refactor step #1 - automatic style formatting
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
#
# - The very first step you can take towards writing code that is as elegant as possible is running an auto formatter. If you use `black`, for example, you can fix many style issues and inconsistencies right from the get-go.
#
# - Also, one could use `flake8` which does a little more than what `black` does. It will also suggest changes to your code.
#
# - In this particula case the only changes made was adding spaces around `=` and `==` which gives your code rooom to breath.
#
#
# </font>
# </div>

# In[ ]:


def myfunc(a):
    empty = []
    for i in range(len(a)):
        if i % 2 == 0:
            empty.append(a[i].upper())
        else:
            empty.append(a[i].lower())

    return "".join(empty)


# # Refactor step #2 - Naming
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
#
# - Names should reflect the intent, or a very important property, of the thing they refer to.
#
# - Here are the changes one could use:
#     - myfunc -> alternate_casing
#     - a -> text
#     - empty -> letters
#     - i -> idx (because of my personal preference).
#
# - **On the index `i`**: a notable exception is the usage of i in for loops. Generally it is left to the coder whether to keep using the bare letter or to use something more verbose as in `idx` instead of `i`.
#
# </font>
# </div>

# In[ ]:


def alternate_casing(text):
    letters = []
    for idx in range(len(text)):
        if idx % 2 == 0:
    letters.append(text[idx].upper()) else:
        letters.append(text[idx].lower())

    return "".join(letters)


# # Refactor step #3 - Traversing data and indices
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
#
# - In our function we need the indices and the data, because we need the index to determine the operation to do, and then we need the data (the actual letter) to change its casing. `enumerate` is the way to go here.
#
# - Not only we were able to remove the explicit indexing, therefore cutting down on one operation, but we also express our intent more clearly: when someone finds an enumerate, they should immediately understand that to mean “in this loop I need both the indices and the data I’m traversing”.
#
# </font>
# </div>

# In[ ]:


def alternate_casing(text):
    letters = []
    for idx, letter in enumerate(text):
        if idx % 2 == 0:
            letters.append(letter.upper())
        else:
            letters.append(letter.lower())

return "".join(letters)


# # Refactor step #4 - Nest only what is needed
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
#
# - **Nesting code** means we need to keep track of many contexts in our head while we read the code, and even though you might not notice it, that’s exhausting. Going in and out of all those indented structures, making all those context switches, consumes brain power. Flatter code places less strain on our brains and makes it easier to keep up with the code.
#
# - Notice that we are doing a `letters.append` regardless of the branch we are in, which makes it less clear that the thing that is changing from one branch to the other is the choice of method that we call on `letter`.
#
# </font>
# </div>

# In[ ]:


def alternate_casing(text):
    letters = []
    for idx, letter in enumerate(text):
        if idx % 2 == 0:
            capitalised = letter.upper()
        else:
            capitalised = letter.lower()
        letters.append(capitalised)

return "".join(letters)


# # Refactor step #5 - Conditional assignment and conditional expressions
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
#
# - Having factored out the `.append()` to outside of the if makes it blatantly clear that the if statement is only there to decide on what to assign to capitalised. This opens the door for another simplification, that will come in the form of a conditional expression.
#
# - Conditional expressions are like condensed `if-else` blocks that are great for conditional assignment.
#
# </font>
# </div>

# In[ ]:


def alternate_casing(text):
    letters = []
    for idx, letter in enumerate(text):
        letters.append(letter.upper() if idx % 2 == 0 else letter.lower())

return "".join(letters)


# # Refactor step #6 - Truthy and Falsy
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
#
# - The next step concerns itself with simplifying the condition of the if statement. In Python, we have this won- derful thing which allows us to interpret many objects as Booleans, even if they are not Booleans themselves. This is often referred to as the Truthy/Falsy value of an object in Python,
#
# - For our case, what matters is that the number 0 is treated as `False` and any other integer is treated as `True`.
# </font>
# </div>

# In[ ]:


def alternate_casing(text):
    letters = []
    for idx, letter in enumerate(text):
        letters.append(letter.lower() if idx % 2 else letter.upper())
    return "".join(letters)


# # Refactor step #7 - List comprehensions versus appending
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
#
# - One thing that you can also learn to spot is when you are building a list by calling `.append()` on it successively. When that is the case, look for an opportunity to use a list comprehension.
#
# - List comprehensions are very Pythonic when used well, and they allow you to initialise a variable with the correct contents right from the start, instead of having to initialise a variable to change it right away.
#
# </font>
# </div>

# In[ ]:


def alternate_casing(text):
    letters = [letter.lower() if idx % 2 else letter.upper() for idx, letter in enumerate(text)]
    return "".join(letters)


# # Refactor step #8 - Avoid long lines
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
#
# - **Horizontal scrolling** in code is to be avoided at all costs, and that means lines shouldn’t get too long.
#
# - The names inside the list comprehension only live inside the list comprehension, so they are very short-lived and have a very specific role.
#
# </font>
# </div>

# In[ ]:


def alternate_casing(text):
    letters = [l.lower() if i % 2 else l.upper() for i, l in enumerate(text)]
    return "".join(letters)


# <div class="alert alert-info">
# <font color=black>
#
# - Another option could've been to split the list comprehension instead.
#
#
# </font>
# </div>

# In[ ]:


def alternate_casing(text):
    letters = [
        letter.lower() if idx % 2 else letter.upper()
        for idx, letter in enumerate(text)
    ]
return "".join(letters)


# # Refactor step #9 - Auxiliary variables
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
#
# - Once again, auxiliary variables aren’t always needed. Whether you have the broken up list comprehension or the one with the short names, you can just get rid of the auxiliary variable and call `.join()` on those letters directly.
#
# </font>
# </div>

# In[ ]:


def alternate_casing(text):
return "".join([l.lower() if i % 2 else l.upper() for i, l in enumerate(text)])


# In[ ]:


def alternate_casing(text):
    return "".join([
        letter.lower() if idx % 2 else letter.upper()
        for idx, letter in enumerate(text)
    ])


# # Refactor step #10 - Reduntant list comprehensions
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
#
# - We have come so far, but there is one final thing we can do, and that is related to how we can get rid of the `[]` of the list comprehension. I mean we can literally delete them.
#
# - Now, instead of a list comprehension, we have a generator expression. Generator expressions are amazing, in my opinion, and they come with memory and speed benefits, so try to use them when you can. In practice, when you are calling a function with a list comprehension, you can often omit the [] altogether to switch to a **generator** expression.
#
# </font>
# </div>

# In[ ]:


def alternate_casing(text):
    return "".join(l.lower() if i % 2 else l.upper() for i, l in enumerate(text))


# In[ ]:


def alternate_casing(text):
    return "".join(
        letter.lower() if idx % 2 else letter.upper()
        for idx, letter in enumerate(text)
    )


# # References
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-warning">
# <font color=black>
#
# - https://mathspp.com/blog/pydonts
# - Martin Fowler: Refactoring, Improving the Design of Existing Code
#
# </font>
# </div>

# In[ ]:
