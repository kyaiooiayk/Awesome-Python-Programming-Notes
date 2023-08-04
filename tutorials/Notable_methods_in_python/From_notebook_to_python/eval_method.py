#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Introduction" data-toc-modified-id="Introduction-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Introduction</a></span></li><li><span><a href="#What-is-the-ord-method?" data-toc-modified-id="What-is-the-ord-method?-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>What is the ord method?</a></span></li><li><span><a href="#Example-#1" data-toc-modified-id="Example-#1-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Example #1</a></span></li><li><span><a href="#Example-#2" data-toc-modified-id="Example-#2-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>Example #2</a></span></li><li><span><a href="#References" data-toc-modified-id="References-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>References</a></span></li></ul></div>

# # Introduction

# <div class="alert alert-warning">
# <font color=black>
# 
# **What?** `eval` method
# 
# </font>
# </div>

# # What is the ord method?

# <div class="alert alert-info">
# <font color=black>
# 
# - The `eval()` method parses the expression passed to this method and runs python expression (code) within the program.
# 
# </font>
# </div>

# # Example #1

# In[3]:


number = 9
# eval performs the multiplication passed as argument
square_number = eval('number * number')
print(square_number)

# but you can also pass the a string as well
number = "9"
square_number = eval(number) * eval(number)

print(square_number)


# # Example #2

# In[5]:


# Perimeter of Square
def calculatePerimeter(l):
    return 4*l

# Area of Square
def calculateArea(l):
    return l*l

expression = input("Type a function: ")

for l in range(1, 5):
    if (expression == 'calculatePerimeter(l)'):
        print("If length is ", l, ", Perimeter = ", eval(expression))

    elif (expression == 'calculateArea(l)'):
        print("If length is ", l, ", Area = ", eval(expression))

    else:
        print('Wrong Function')
        break


# # References

# <div class="alert alert-warning">
# <font color=black>
# 
# - https://www.programiz.com/python-programming/methods/built-in/eval
# 
# </font>
# </div>

# In[ ]:




