#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Introduction" data-toc-modified-id="Introduction-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Introduction</a></span></li><li><span><a href="#Dependency-Inversion" data-toc-modified-id="Dependency-Inversion-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Dependency Inversion</a></span></li><li><span><a href="#Example" data-toc-modified-id="Example-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Example</a></span></li><li><span><a href="#References" data-toc-modified-id="References-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>References</a></span></li><li><span><a href="#Requirements" data-toc-modified-id="Requirements-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>Requirements</a></span></li></ul></div>

# # Introduction
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-block alert-warning">
# <font color=black>
#
# **What?** Dependency Inversion
#
# </font>
# </div>

# # Dependency Inversion
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-block alert-info">
# <font color=black>
#
# - Instead of directly calling a function, you get an adapter, and you call that adapter’s interface.
# - Instead of fixing the behaviour of your program, you allow it to be modified as needed without any change.
# - Different behaviours can be constructed to fit the caller’s intentions.
#
# </font>
# </div>

# # Example
# <hr style = "border:2px solid black" ></hr>

# ![image.png](attachment:image.png)

# In[ ]:


# # References
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-block alert-warning">
# <font color=black>
#
# - [Dependency Inversion](https://laszlo.substack.com/p/clean-architecture-in-data-science)
# - [Wikipedia article](https://en.wikipedia.org/wiki/Dependency_inversion_principle)
#
# </font>
# </div>

# # Requirements
# <hr style="border:2px solid black"> </hr>

# In[1]:


get_ipython().run_line_magic("load_ext", "watermark")
get_ipython().run_line_magic("watermark", "-v -iv -m")


# In[ ]:
