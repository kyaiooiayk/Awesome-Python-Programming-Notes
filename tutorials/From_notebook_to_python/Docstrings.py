#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Introduction" data-toc-modified-id="Introduction-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Introduction</a></span></li><li><span><a href="#What-is-a-docstring?" data-toc-modified-id="What-is-a-docstring?-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>What is a docstring?</a></span></li><li><span><a href="#Quick-demo" data-toc-modified-id="Quick-demo-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Quick demo</a></span></li><li><span><a href="#Docstrings-vs.-Commenting" data-toc-modified-id="Docstrings-vs.-Commenting-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>Docstrings vs. Commenting</a></span></li><li><span><a href="#Docstring-format" data-toc-modified-id="Docstring-format-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>Docstring format</a></span><ul class="toc-item"><li><span><a href="#Sphinx-Style" data-toc-modified-id="Sphinx-Style-5.1"><span class="toc-item-num">5.1&nbsp;&nbsp;</span>Sphinx Style</a></span></li><li><span><a href="#Google-Style" data-toc-modified-id="Google-Style-5.2"><span class="toc-item-num">5.2&nbsp;&nbsp;</span>Google Style</a></span></li><li><span><a href="#Numpy-Style" data-toc-modified-id="Numpy-Style-5.3"><span class="toc-item-num">5.3&nbsp;&nbsp;</span>Numpy Style</a></span></li></ul></li><li><span><a href="#PyDoc" data-toc-modified-id="PyDoc-6"><span class="toc-item-num">6&nbsp;&nbsp;</span>PyDoc</a></span></li><li><span><a href="#References" data-toc-modified-id="References-7"><span class="toc-item-num">7&nbsp;&nbsp;</span>References</a></span></li></ul></div>

# # Introduction
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-warning">
# <font color=black>
# 
# **What?** Docstrings
# 
# </font>
# </div>

# # What is a docstring?
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-info">
# <font color=black>
# 
# - Python documentation string or commonly known as docstring, is a string literal, and it is used in the class, module, function, or method definition. 
# - Docstrings are accessible from the doc attribute `__doc__` for any of the Python objects and also with the built-in `help()` function.
# 
# </font>
# </div>

# # Quick demo
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-info">
# <font color=black>
# 
# - For example, let's say you installed the scikit-learn library and you would like to know all about the `sklearn` package like description, package modules, etc., you could simply use the help function to get all the information.
# - You would notice that the output of the `help` function is more verbose than the `__doc__` attribute.
# 
# </font>
# </div>

# In[1]:


import sklearn


# In[ ]:


help(sklearn)


# In[19]:


print(sklearn.__doc__)


# # Docstrings vs. Commenting
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-info">
# <font color=black>
# 
# - **Docstrings** act as documentation for the class, module, and packages. They are similar to comments, but they are enhanced, more logical, and useful version of commenting. They generally start with a triple quotes and can be access by `doc` or `help` python method.
# 
# - **Comments** are mainly used to explain non-obvious portions of the code and can be useful for comments on Fixing bugs and tasks that are needed to be done. They generally start with `#` and cannot be access neither by `doc` not `help` python method.
# 
# </font>
# </div>

# In[14]:


def square(a):
    """Returned argument a is squared.

    Parameters
    ----------
    a : float
        input

    Returns
    -------
    b : float
        Returning value
    """

    # b is defined as a to the second power
    b = a**2
    return b


# In[18]:


square.__doc__


# In[17]:


print(square.__doc__)


# In[16]:


help(square)


# # Docstring format
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-info">
# <font color=black>
# 
# - The most common formats used are listed below:
#     - [NumPy/SciPy docstrings](https://numpydoc.readthedocs.io/en/latest/format.html) Combination of reStructured and GoogleDocstrings and supported by Sphinx    
#     - [EpyDoc](http://epydoc.sourceforge.net/) Render Epytext as series of HTML documents and a tool for generating API documentation for Python modules based on their Docstrings
#     - [Google Docstrings](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html) Google's Style
# - [PyDoc](https://docs.python.org/3.10/library/pydoc.html) Standard documentation module for Python and supported by Sphinx    
# - The formats of all the Documentation strings are nearly similar. The patterns are similar, but there are only nitty-gritty changes in each format.
# 
# </font>
# </div>

# ## Sphinx Style

# <div class="alert alert-info">
# <font color=black>
# 
# - Sphinx is the easy and traditional style, verbose, and was initially created specifically for the Python Documentation. Sphinx uses a reStructured Text, which is similar in usage to Markdown.
# - Sphinx uses the keyword(reserved word); most of the programming language does. But it is explicitly called role in Sphinx. In the above code, Sphinx has the param as a role, and type is a role, which is the Sphinx data type for param. type role is optional, but param is mandatory. The return roles document the returned object. It is different from the param role. The return role is not dependent on the rtype and vice-versa. The rtype is the type of object returned from the given function
# 
# </font>
# </div>

# In[ ]:


class Vehicle(object):
    '''
    The Vehicle object contains lots of vehicles
    :param arg: The arg is used for ...
    :type arg: str
    :param `*args`: The variable arguments are used for ...
    :param `**kwargs`: The keyword arguments are used for ...
    :ivar arg: This is where we store arg
    :vartype arg: str
    '''

    def __init__(self, arg, *args, **kwargs):
        self.arg = arg

    def cars(self, distance, destination):
        '''We can't travel a certain distance in vehicles without fuels, so here's the fuels

        :param distance: The amount of distance traveled
        :type amount: int
        :param bool destinationReached: Should the fuels be refilled to cover required distance?
        :raises: :class:`RuntimeError`: Out of fuel

        :returns: A Car mileage
        :rtype: Cars
        '''
        pass


# ## Google Style

# <div class="alert alert-info">
# <font color=black>
# 
# - Google Style is easier and more intuitive to use. It can be used for the shorter form of documentation. A configuration of python file needs to be done to get started, so you need to add either sphinx.ext.napoleon or sphinxcontrib.napoleon to the extensions list in conf.py.
# - The Google Style is better than the Sphinx style. It also has an inconvenient feature, i.e., in the above code, the multi-line description of the distance would look **messy**.
# 
# </font>
# </div>

# In[ ]:


class Vehicles(object):
    '''
    The Vehicle object contains a lot of vehicles

    Args:
        arg (str): The arg is used for...
        *args: The variable arguments are used for...
        **kwargs: The keyword arguments are used for...

    Attributes:
        arg (str): This is where we store arg,
    '''

    def __init__(self, arg, *args, **kwargs):
        self.arg = arg

    def cars(self, distance, destination):
        '''We can't travel distance in vehicles without fuels, so here is the fuels

        Args:
            distance (int): The amount of distance traveled
            destination (bool): Should the fuels refilled to cover the distance?

        Raises:
            RuntimeError: Out of fuel

        Returns:
            cars: A car mileage
        '''
        pass


# ## Numpy Style

# <div class="alert alert-info">
# <font color=black>
# 
# - Numpy style has a lot of details in the documentation. It is more verbose than other documentation, but it is an excellent choice if you want to do detailed documentation, i.e., extensive documentation of all the functions and parameters.
# - The above example is more verbose than any other documentation. It is more lengthy and could only be used for the long and detailed documentation.
# 
# </font>
# </div>

# In[ ]:


class Vehicles(object):
    '''
    The Vehicles object contains lots of vehicles

    Parameters
    ----------
    arg : str
        The arg is used for ...
    *args
        The variable arguments are used for ...
    **kwargs
        The keyword arguments are used for ...

    Attributes
    ----------
    arg : str
        This is where we store arg,
    '''

    def __init__(self, arg, *args, **kwargs):
        self.arg = arg

    def cars(self, distance, destination):
        '''We can't travel distance in vehicles without fuels, so here is the fuels

        Parameters
        ----------
        distance : int
            The amount of distance traveled
        destination : bool
            Should the fuels refilled to cover the distance?

        Raises
        ------
        RuntimeError
            Out of fuel

        Returns
        -------
        cars
            A car mileage
        '''
        pass


# # PyDoc
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-info">
# <font color=black>
# 
# - As you learned that docstrings are accessible through the built-in Python __doc__ attribute and the help() function. You could also make use of the built-in module known as Pydoc, which is very different in terms of the features & functionalities it possesses when compared to the doc attribute and the help function.
# - Pydoc is a tool that would come handy when you want to share the code with your colleagues or make it open-source, in which case you would be targeting a much wider audience. It could generate web pages from your Python documentation and can also launch a web server.
# 
# </font>
# </div>

# # References
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-warning">
# <font color=black>
# 
# - https://www.datacamp.com/community/tutorials/docstrings-python
# - [Nice and coincise example for different docstring standards](https://github.com/NilsJPWerner/autoDocstring/tree/f7bc9f427d5ebcd87e6f5839077a87ecd1cbb404/docs)
#     
# </font>
# </div>

# In[ ]:




