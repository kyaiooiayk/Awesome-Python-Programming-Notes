#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Introduction" data-toc-modified-id="Introduction-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Introduction</a></span></li><li><span><a href="#What-is-__new__?" data-toc-modified-id="What-is-__new__?-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>What is <code>__new__</code>?</a></span></li><li><span><a href="#Example-#1" data-toc-modified-id="Example-#1-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Example #1</a></span></li><li><span><a href="#Example-#2" data-toc-modified-id="Example-#2-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>Example #2</a></span></li><li><span><a href="#References" data-toc-modified-id="References-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>References</a></span></li></ul></div>

# # Introduction
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-block alert-warning">
# <font color=black>
#
# **What?** `Super()` `__init__` and `__new__`
#
# </font>
# </div>

# # What is `__new__`?
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-info">
# <font color=black>
#
# - Transforming from class to an object is called instantiation.
# - `__init__` is used to objects initialization and provide a class with a contructor.
#  - During object creation `__init__` method doesn’t get executed first, the method which gets executed first is `__new__`
#  - `__new__()` method gets most of the same arguments at `__init__` and it is responsible for actually creating the new object (prior to initializing object).
# - We can use `__new__` when we need to control the creation of a new instance.
#
# </font>
# </div>

# # Example #1
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-info">
# <font color=black>
#
# - Let's say we have a 3 classes, File ,TextFile(File) and ImageFile(File). We need instantiate TextFile for Text files, ImageFile for image file, and File for other type of files. We can obtain this by instantiating them directly.
#
# - But what if we could instantiate them only using the parent class (File) depending the file content? Yes, we want to instantiate child classes using parent class!
#
# </font>
# </div>

# In[3]:


class File:
    def __new__(cls, *args, **kwargs):
        file_type = kwargs.get("file_name").split(".")[-1]

        if file_type == "txt":
            for i in cls.__subclasses__():
                if i.__name__ == "TextFile":
                    return super().__new__(i)
        elif file_type in ["jpg", "png", "jpeg"]:
            for i in cls.__subclasses__():
                if i.__name__ == "ImageFile":
                    return super().__new__(i)
        else:
            return super().__new__(File)

    def __init__(self, file_name=""):
        self.file_name = file_name


class ImageFile(File):
    def __init__(self, *args, **kwargs):
        self.height = kwargs.get("height")
        self.width = kwargs.get("width")


class TextFile(File):
    def __init__(self, *args, **kwargs):
        self.file_size = kwargs.get("file_size")


# In[5]:


"""
Here, we are instantiating the TextFile, ImageFile and File classes using the File (parent)
class depending on content of file (file_type). 
"""
text_file = File(file_name="testfile.txt", height=100, width=100)
image_file = File(file_name="imagefile.png", file_size=500)
other_file = File(file_name="video_file.mp4")


# In[6]:


print(text_file)
print(image_file)
print(other_file)


# # References
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-block alert-warning">
# <font color=black>
#
# - https://medium.com/@taohidulii/playing-with-inheritance-in-python-73ea4f3b669e
# - https://www.python.org/download/releases/2.2/descrintro/#__new__
# - https://nbviewer.org/github/rasbt/python_reference/blob/master/tutorials/not_so_obvious_python_stuff.ipynb?create=1
#
# </font>
# </div>

# In[ ]:
