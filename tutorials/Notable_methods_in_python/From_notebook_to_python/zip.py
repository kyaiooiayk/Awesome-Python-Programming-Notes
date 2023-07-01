#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Introduction" data-toc-modified-id="Introduction-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Introduction</a></span></li><li><span><a href="#What-is-it?" data-toc-modified-id="What-is-it?-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>What is it?</a></span></li><li><span><a href="#Example-#1" data-toc-modified-id="Example-#1-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Example #1</a></span></li><li><span><a href="#Example-#2" data-toc-modified-id="Example-#2-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>Example #2</a></span></li><li><span><a href="#Example-#3" data-toc-modified-id="Example-#3-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>Example #3</a></span></li><li><span><a href="#Example-#4" data-toc-modified-id="Example-#4-6"><span class="toc-item-num">6&nbsp;&nbsp;</span>Example #4</a></span></li><li><span><a href="#Example-#5" data-toc-modified-id="Example-#5-7"><span class="toc-item-num">7&nbsp;&nbsp;</span>Example #5</a></span></li><li><span><a href="#Example-#6" data-toc-modified-id="Example-#6-8"><span class="toc-item-num">8&nbsp;&nbsp;</span>Example #6</a></span></li><li><span><a href="#Example-#7" data-toc-modified-id="Example-#7-9"><span class="toc-item-num">9&nbsp;&nbsp;</span>Example #7</a></span></li><li><span><a href="#References" data-toc-modified-id="References-10"><span class="toc-item-num">10&nbsp;&nbsp;</span>References</a></span></li></ul></div>

# # Introduction
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-block alert-warning">
# <font color=black>
#
# **What?** `zip`
#
# </font>
# </div>

# # What is it?
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-block alert-info">
# <font color=black>
#
# - Return a zip object whose .next() method returns a tuple where the i-th element comes from the i-th iterable argument.
# - The `.next()` method continues until the shortest iterable in the argument sequence is exhausted and then it raises StopIteration.
#
# </font>
# </div>

# ![image.png](attachment:image.png)

# # Example #1
# <hr style = "border:2px solid black" ></hr>

# In[2]:


a_couple_of_letters = ["a", "b", "c", "d", "e", "f"]
some_numbers = [5, 3, 7, 9, 11, 2]


# In[3]:


print(zip(a_couple_of_letters, some_numbers))


# In[4]:


for t in zip(a_couple_of_letters, some_numbers):
    print(t, type(t))


# # Example #2
# <hr style = "border:2px solid black" ></hr>

# In[5]:


location = ["Helgoland", "Kiel", "Berlin-Tegel", "Konstanz", "Hohenpeißenberg"]
air_pressure = [1021.2, 1019.9, 1023.7, 1023.1, 1027.7]
temperatures = [6.0, 4.3, 2.7, -1.4, -4.4]
altitude = [4, 27, 37, 443, 977]
for t in zip(location, air_pressure, temperatures, altitude):
    print(t)


# # Example #3
# <hr style = "border:2px solid black" ></hr>

# In[6]:


food = ["ham", "spam", "cheese"]
for item in zip(range(1000, 1003), food):
    print(item)


# # Example #4
# <hr style = "border:2px solid black" ></hr>

# In[7]:


s = "Python"
for t in zip(s):
    print(t)


# # Example #5
# <hr style = "border:2px solid black" ></hr>

# In[8]:


# Different lengths!
colors = ["green", "red", "blue"]
cars = ["BMW", "Alfa Romeo"]
for car, color in zip(cars, colors):
    print(car, color)


# # Example #6
# <hr style = "border:2px solid black" ></hr>

# In[10]:


cities_and_population = [
    ("Zurich", 415367),
    ("Geneva", 201818),
    ("Basel", 177654),
    ("Lausanne", 139111),
    ("Bern", 133883),
    ("Winterthur", 111851),
]


# In[11]:


cities, populations = list(zip(*cities_and_population))
print(cities)
print(populations)


# # Example #7
# <hr style = "border:2px solid black" ></hr>

# In[12]:


abc = "abcdef"
morse_chars = [".-", "-...", "-.-.", "-..", ".", "..-."]
text2morse = dict(zip(abc, morse_chars))
print(text2morse)


# # References
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-block alert-warning">
# <font color=black>
#
# - https://python-course.eu/advanced-python/zip-tutorial.php
#
# </font>
# </div>

# In[ ]:
