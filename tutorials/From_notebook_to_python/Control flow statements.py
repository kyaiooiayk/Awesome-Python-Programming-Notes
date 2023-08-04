#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Introduction" data-toc-modified-id="Introduction-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Introduction</a></span></li><li><span><a href="#if-elif-else" data-toc-modified-id="if-elif-else-2"><span class="toc-item-num">2&nbsp;&nbsp;</span><code>if-elif-else</code></a></span></li><li><span><a href="#for-loops" data-toc-modified-id="for-loops-3"><span class="toc-item-num">3&nbsp;&nbsp;</span><code>for</code> loops</a></span></li><li><span><a href="#while-loops" data-toc-modified-id="while-loops-4"><span class="toc-item-num">4&nbsp;&nbsp;</span><code>while</code> loops</a></span></li><li><span><a href="#Continue" data-toc-modified-id="Continue-5"><span class="toc-item-num">5&nbsp;&nbsp;</span><code>Continue</code></a></span></li><li><span><a href="#break-and-continue" data-toc-modified-id="break-and-continue-6"><span class="toc-item-num">6&nbsp;&nbsp;</span><code>break</code> and <code>continue</code></a></span></li><li><span><a href="#Loops-with-an-else-Block-not-if-else" data-toc-modified-id="Loops-with-an-else-Block-not-if-else-7"><span class="toc-item-num">7&nbsp;&nbsp;</span>Loops with an else Block not if-else</a></span></li><li><span><a href="#References" data-toc-modified-id="References-8"><span class="toc-item-num">8&nbsp;&nbsp;</span>References</a></span></li></ul></div>

# # Introduction
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-block alert-warning">
# <font color=black>
# 
# **What?** Control flow statements
# 
# </font>
# </div>

# # `if-elif-else`
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-info">
# <font color=black>
# 
# - `if`
# - `else`
# 
# </font>
# </div>

# In[1]:


x = -15

if x == 0:
    print(x, "is zero")
elif x > 0:
    print(x, "is positive")
elif x < 0:
    print(x, "is negative")
else:
    print(x, "is unlike anything I've ever seen...")


# # `for` loops
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-info">
# <font color=black>
# 
# - `for` loops
# - Notice the simplicity of the for loop: we specify the variable we want to use, the sequence we want to loop over, and use the `in` operator to link them together in an intuitive and readable way. More precisely, the object to the right of the `in` can be any Python **iterator**. 
# 
# </font>
# </div>

# In[2]:


for N in [2, 3, 5, 7]:
    print(N, end=' ') # print all on same line


# # `while` loops
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-info">
# <font color=black>
# 
# - `while` loop iterates until some condition is met.
# 
# </font>
# </div>

# In[3]:


i = 0
while i < 10:
    print(i, end=' ')
    i += 1


# # `Continue`
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-info">
# <font color=black>
# 
# - The `continue` statement continues with the next iteration of the loop
# 
# </font>
# </div>

# In[4]:


"""
Find odd number given a range
An odd number is a number divisable by 2
"""

for num in range(2,10):
    if num % 2 == 0:
        print("Found an even number", num)
        continue
    print("Not even number", num)


# In[5]:


"""
You can still use if and else but continue seems to be more convenient
"""
for n in range(2,10):
    # if the remainder of n / 2 is 0, skip the rest of the loop
    if n % 2 == 0:
        print("Found an even number", n)        
    else:        
        print("Not even number", n)


# In[6]:


"""
This is what happens if you do not use continue
"""
for num in range(2,10):
    if num % 2 == 0:
        print("Found an even number", num)
        #continue
    print("Not even number", num)


# # `break` and `continue`
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-info">
# <font color=black>
# 
# - There are used to **fine-tune** how they workflow is controlled:
# 
#     - The `break` statement breaks-out of the loop entirely
#     - The `continue` statement **skips the remainder of the current loop**, and goes to the next iteration
# 
# </font>
# </div>

# In[7]:


"""
This loop will fill a list with all Fibonacci numbers up to a certain value.
Notice that we use a while True loop, which will loop forever unless we have a break statement!
"""
a, b = 0, 1
amax = 100
L = []

while True:
    (a, b) = (b, a + b)
    if a > amax:
        break
    L.append(a)

print(L)


# # Loops with an else Block not if-else
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-info">
# <font color=black>
# 
# - One rarely used pattern available in Python is the ``else`` statement as part of a ``for`` or ``while`` loop.
# 
# - We discussed the ``else`` block earlier: it executes if all the ``if`` and ``elif`` statements evaluate to ``False``.
# - The loop-``else`` is perhaps one of the more confusingly-named statements in Python; I prefer to think of it as a ``nobreak`` statement: that is, the ``else`` block is executed only if the loop ends naturally, without encountering a ``break`` statement.
# 
# </font>
# </div>

# In[8]:


"""
Find all the prime number given a max number.
"""
L = []
nmax = 30

for n in range(2, nmax):
    for factor in L:
        if n % factor == 0:
            break            
    else: 
        """
        The else statement only executes if none of the factors 
        divide the given number. The else statement works similarly
        with the while loop.
        """
        L.append(n)
print(L)


# In[9]:


# A slightly different version of it is
for n in range(2, nmax):
    for x in range(2, n):
        if n % x == 0:
            print(n, "equals", x, "*0", n/x)
            break
    else:
        """
        Loop falls through withouth finding a factor
        Essentialy if the break is not hit by the end of the main loop
        """
        print(" ", n, "is a prime number")


# # References
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-block alert-warning">
# <font color=black>
# 
# - [Whirlwind Tour of Python](http://www.oreilly.com/programming/free/a-whirlwind-tour-of-python.csp)
# 
# </font>
# </div>
