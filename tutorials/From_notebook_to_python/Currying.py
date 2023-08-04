#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Introduction" data-toc-modified-id="Introduction-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Introduction</a></span></li><li><span><a href="#What-is-currying?" data-toc-modified-id="What-is-currying?-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>What is currying?</a></span></li><li><span><a href="#Composition-of-functions" data-toc-modified-id="Composition-of-functions-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Composition of functions</a></span></li><li><span><a href="#Compose-with-Arbitrary-Arguments" data-toc-modified-id="Compose-with-Arbitrary-Arguments-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>Compose with Arbitrary Arguments</a></span></li><li><span><a href="#References" data-toc-modified-id="References-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>References</a></span></li></ul></div>

# # Introduction
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-warning">
# <font color=black>
# 
# **What?** Currying
# 
# </font>
# </div>

# # What is currying?
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
# 
# - In mathematics and computer science, currying is the technique of breaking down the evaluation of a function that takes multiple arguments into evaluating a sequence of single-argument functions. 
# - Currying is also used in theoretical computer science, because it is often easier to transform multiple argument models into single argument models.
# 
# </font>
# </div>

# # Composition of functions
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
# 
# - The composition of two functions is a chaining process in which the output of the inner function becomes the input of the outer function.
# - We will use our compose function in the next example. Let's assume, we have a thermometer, which is not working accurately. The correct temperature can be calculated by applying the function readjust to the temperature values. Let us further assume that we have to convert our temperature values from Celsius to Fahrenheit. We can do this by applying compose to both functions:
# - The composition of two functions **is generally not commutative**, i.e. `compose(celsius2fahrenheit, readjust)` is different from `compose(readjust, celsius2fahrenheit)`.
# </font>
# </div>

# In[1]:


def compose(g, f):
    def h(x):
        return g(f(x))
    return h


# In[2]:


def celsius2fahrenheit(t):
    return 1.8 * t + 32
def readjust(t):
    return 0.9 * t - 0.5
convert = compose(readjust, celsius2fahrenheit)
print(convert(10), celsius2fahrenheit(10))


# In[3]:


# Incorrect use
convert2 = compose(celsius2fahrenheit, readjust)
print(convert2(10), celsius2fahrenheit(10))


# # Compose with Arbitrary Arguments
# <hr style = "border:2px solid black" ></hr>

# In[4]:


def compose(g, f):
    def h(*args, **kwargs):
        return g(f(*args, **kwargs))
    return h


# In[5]:


def BMI(weight, height):
    return weight / height**2
def evaluate_BMI(bmi):
    if bmi < 15:
        return "Very severely underweight"
    elif bmi < 16:
        return "Severely underweight"
    elif bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal (healthy weight)"
    elif bmi < 30:
        return "Overweight"
    elif bmi < 35:
        return "Obese Class I (Moderately obese)"
    elif bmi < 40:
        return "Obese Class II (Severely obese)"
    else:
        return "Obese Class III (Very severely obese)"
f = compose(evaluate_BMI, BMI)
again = "y"
while again == "y":
    weight = float(input("weight (kg) "))
    height = float(input("height (m) "))
    print(f(weight, height))
    again = input("Another run? (y/n)")


# # References
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-warning">
# <font color=black>
# 
# - https://python-course.eu/advanced-python/currying-in-python.php
#     
# </font>
# </div>

# In[ ]:




