#!/usr/bin/env python
# coding: utf-8

# # Introduction
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-warning">
# <font color=black>
# 
# **What?** Broadcasting
# 
# </font>
# </div>

# # List - not supported
# <hr style="border:2px solid black"> </hr>

# In[1]:


# Python lists don't support broadcasting
nums = [-2, -1, 0, 1, 2]
nums ** 2


# # List loop - not efficient
# <hr style="border:2px solid black"> </hr>

# In[8]:


get_ipython().run_cell_magic('timeit', '-n100', '# For loop (inefficient option)\nsqrd_nums = []\nfor num in nums:\n    sqrd_nums.append(num ** 2)\n#print(sqrd_nums)\n')


# # List comprehension - better but not best
# <hr style="border:2px solid black"> </hr>

# In[6]:


get_ipython().run_cell_magic('timeit', '-n100', '# List comprehension (better option but not best)\nsqrd_nums = [num ** 2 for num in nums]\n#print(sqrd_nums)\n')


# # NumPy array  - best option
# <hr style="border:2px solid black"> </hr>

# In[4]:


get_ipython().run_cell_magic('timeit', '-n100', 'import numpy as np\nnums_np = np.array([-2, -1, 0, 1, 2]) \nnums_np ** 2\n')


# # References
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-warning">
# <font color=black>
# 
# - https://s3.amazonaws.com/assets.datacamp.com/production/course_13369/slides/chapter1.pdf
# 
# </font>
# </div>
