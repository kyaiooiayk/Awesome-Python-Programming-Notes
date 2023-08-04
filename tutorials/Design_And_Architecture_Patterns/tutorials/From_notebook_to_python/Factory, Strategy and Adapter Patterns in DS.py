#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Introduction" data-toc-modified-id="Introduction-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Introduction</a></span></li><li><span><a href="#Factory-pattern" data-toc-modified-id="Factory-pattern-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Factory pattern</a></span><ul class="toc-item"><li><span><a href="#Easy-extension" data-toc-modified-id="Easy-extension-2.1"><span class="toc-item-num">2.1&nbsp;&nbsp;</span>Easy extension</a></span></li><li><span><a href="#Another-example" data-toc-modified-id="Another-example-2.2"><span class="toc-item-num">2.2&nbsp;&nbsp;</span>Another example</a></span></li></ul></li><li><span><a href="#Strategy-pattern" data-toc-modified-id="Strategy-pattern-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Strategy pattern</a></span><ul class="toc-item"><li><span><a href="#Easy-extension" data-toc-modified-id="Easy-extension-3.1"><span class="toc-item-num">3.1&nbsp;&nbsp;</span>Easy extension</a></span></li><li><span><a href="#Another-example" data-toc-modified-id="Another-example-3.2"><span class="toc-item-num">3.2&nbsp;&nbsp;</span>Another example</a></span></li></ul></li><li><span><a href="#Adapter" data-toc-modified-id="Adapter-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>Adapter</a></span></li><li><span><a href="#References" data-toc-modified-id="References-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>References</a></span></li><li><span><a href="#Requirements" data-toc-modified-id="Requirements-6"><span class="toc-item-num">6&nbsp;&nbsp;</span>Requirements</a></span></li></ul></div>

# # Introduction
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-block alert-warning">
# <font color=black>
# 
# **What?** Factory, Strategy and Adapter Patterns in DS
#     
# </font>
# </div>

# # Factory pattern
# <hr style = "border:2px solid black" ></hr>

# ![image.png](attachment:image.png)

# ## Easy extension

# - What if I want to add a new loader via SQL?
# - This show how easy it would be to add this without breaking or writing any part of the previously written code.

# ![image.png](attachment:image.png)

# ## Another example

# ![image.png](attachment:image.png)

# # Strategy pattern
# <hr style = "border:2px solid black" ></hr>

# ![image.png](attachment:image.png)

# ## Easy extension

# - What if I want to add a new lemmantiser?
# - This show how easy it would be to add this without breaking or writing any part of the previously written code.

# ![image.png](attachment:image.png)

# ## Another example

# ![image.png](attachment:image.png)

# # Adapter
# <hr style = "border:2px solid black" ></hr>

# ![image.png](attachment:image.png)

# # References
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-block alert-warning">
# <font color=black>
# 
# - [You only need 2 design patterns to improve the quality of your code in a data science project](https://laszlo.substack.com/p/you-only-need-2-design-patterns-to)
# - [Machine learning is the continuation of software enginerring by other mens: PyData 2022](file:///Users/gm_main/Downloads/2942283f-12f6-4548-80c2-071d3edb08f4.pdf.pdf)
#     
# </font>
# </div>

# # Requirements
# <hr style="border:2px solid black"> </hr>

# In[6]:


get_ipython().run_line_magic('load_ext', 'watermark')
get_ipython().run_line_magic('watermark', '-v -iv -m')


# In[ ]:




