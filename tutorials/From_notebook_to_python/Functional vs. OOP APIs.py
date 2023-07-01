#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Introduction" data-toc-modified-id="Introduction-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Introduction</a></span></li><li><span><a href="#Comparing-apples-with-bananas!" data-toc-modified-id="Comparing-apples-with-bananas!-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Comparing apples with bananas!</a></span></li><li><span><a href="#What-is-OOP?" data-toc-modified-id="What-is-OOP?-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>What is OOP?</a></span></li><li><span><a href="#Functional-vs.-method" data-toc-modified-id="Functional-vs.-method-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>Functional vs. method</a></span></li><li><span><a href="#Functional-vs.-OOP" data-toc-modified-id="Functional-vs.-OOP-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>Functional vs. OOP</a></span></li><li><span><a href="#Problem" data-toc-modified-id="Problem-6"><span class="toc-item-num">6&nbsp;&nbsp;</span>Problem</a></span><ul class="toc-item"><li><span><a href="#FP" data-toc-modified-id="FP-6.1"><span class="toc-item-num">6.1&nbsp;&nbsp;</span>FP</a></span></li><li><span><a href="#OOP" data-toc-modified-id="OOP-6.2"><span class="toc-item-num">6.2&nbsp;&nbsp;</span>OOP</a></span></li></ul></li><li><span><a href="#Mixing-OOP-and-FP-in-production" data-toc-modified-id="Mixing-OOP-and-FP-in-production-7"><span class="toc-item-num">7&nbsp;&nbsp;</span>Mixing OOP and FP in production</a></span></li><li><span><a href="#References" data-toc-modified-id="References-8"><span class="toc-item-num">8&nbsp;&nbsp;</span>References</a></span></li><li><span><a href="#Requirements" data-toc-modified-id="Requirements-9"><span class="toc-item-num">9&nbsp;&nbsp;</span>Requirements</a></span></li></ul></div>

# # Introduction
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-block alert-warning">
# <font color=black>
#
# **What?** Functional vs. OOP APIs
#
# </font>
# </div>

# # Comparing apples with bananas!
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
#
# - One is not superior to the other when comparing functional to object-oriented programming in Python.
# - This is because the two are not comparable since they are used for different purposes.
# - They are not pitted against each other when discussing programming and are not the only approaches that could serve you.
# - Your choice of a programming approach will depend on what you are trying to do within your application.
# - **Python supports both.**
#
# </font>
# </div>

# # What is OOP?
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
#
# - **Functional programming** is a technique that emphasizes the evaluation of functions. It gets its name from writing functions that provide the main source of logic in a program. The concept behind functional programming is for the functions to be stateless and rely only on the given inputs to produce an output. Functional programming is a paradigm that treats computation as the evaluation of mathematical functions and avoids changing states and mutable data. It is based on different concepts, including pure functions, recursion, high order functions, type systems, and referential transparency.
#
# - **OOP** is a paradigm based on the concept of objects which contain data structures in the fields known as attributes and codes in the form of procedures, also known as methods. The most popular object-oriented programming language is class-based, which means objects are presented as instances of classes. The main features of object-oriented programming are an abstraction, inheritance, polymorphism, and encapsulation.
#
# </font>
# </div>

#

# # Functional vs. OOP
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-block alert-info">
# <font color=black>
#
# - FP emphasizes the evaluation of functions, while OOP is based on the concept of objects.
# - Secondly, FP follows the declarative model compared to the imperative programming model of OOP.
# - FP uses immutable data, compared to OOP that uses mutable data.
# - FP states that data and behavior are distinctively different and should be kept separate for clarity. In contrast, OOP says that bringing together data and behavior in a single location makes it easier to understand how a program works.
# - FP is considered declarative programming because it is done with expressions rather than states.
# - FP focuses on what we are doing, while the OOP focus on how we are doing it.
# - FP provides high performance in the processing of large data for applications, the OOP cannot be used for big data processing.
#
# </font>
# </div>

# ![image.png](attachment:image.png)

# # Problem
# <hr style = "border:2px solid black" ></hr>

# - Given a list of integers, find the largest odd number in the list.

# ## FP

# In[2]:


numbers = [2, 4, 6, 7, 9, 10, 13]

largest_odd = max(filter(lambda x: x % 2 != 0, numbers))

print(largest_odd)


# ## OOP

# In[4]:


class LargestOddNumber:
    def __init__(self, numbers):
        self.numbers = numbers

    def find_largest_odd(self):
        largest_odd = None
        for num in self.numbers:
            if num % 2 != 0 and (largest_odd is None or num > largest_odd):
                largest_odd = num
        return largest_odd


numbers = [2, 4, 6, 7, 9, 10, 13]
solver = LargestOddNumber(numbers)

print(solver.find_largest_odd())


# # Mixing OOP and FP in production
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-block alert-info">
# <font color=black>
#
# - Is this used anywhere? Yes, and the best example out there are: FastAPI and Pydantic. FastAPI is a lightweight API framework for Python, and Pydantic is a data validation and settings management library.
# - **Pydantic** allows you to define data structures using Python classes, and then validate incoming data and access it via object attributes.
# - **FastAPI** allows you to define your API routes as functions, wrapping each one with a decorator (which is a very FP-like concept) to encapsulate your logic.
#
# </font>
# </div>

# # References
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-block alert-warning">
# <font color=black>
#
# - [Functional Vs. Object-Oriented Programming in Python](https://beapython.dev/2020/01/21/functional-vs-object-oriented-programming-in-python/)
# - [Python: To OOP or to FP?](https://towardsdatascience.com/python-to-oop-or-to-fp-13ac79a43b16)
# - [Compare Functional Programming, Imperative Programming and Object Oriented Programming](https://www.digitalocean.com/community/tutorials/functional-imperative-object-oriented-programming-comparison)
# - [Functional vs. OO: The Debate that Imprecise Language Destroyed](https://chelseatroy.com/2021/02/22/functional-vs-oo-the-debate-that-imprecise-language-destroyed/)
#
# </font>
# </div>

# # Requirements
# <hr style = "border:2px solid black" ></hr>

# In[1]:


get_ipython().run_line_magic("load_ext", "watermark")
get_ipython().run_line_magic("watermark", "-v -iv")


# In[ ]:
