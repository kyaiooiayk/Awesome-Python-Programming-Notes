#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Introduction" data-toc-modified-id="Introduction-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Introduction</a></span></li><li><span><a href="#Imports" data-toc-modified-id="Imports-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Imports</a></span></li><li><span><a href="#Data-class-vs.-other-data-structures" data-toc-modified-id="Data-class-vs.-other-data-structures-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Data class vs. other data structures</a></span><ul class="toc-item"><li><span><a href="#Tuple" data-toc-modified-id="Tuple-3.1"><span class="toc-item-num">3.1&nbsp;&nbsp;</span><code>Tuple</code></a></span></li><li><span><a href="#dict" data-toc-modified-id="dict-3.2"><span class="toc-item-num">3.2&nbsp;&nbsp;</span><code>dict</code></a></span></li><li><span><a href="#namedtuple" data-toc-modified-id="namedtuple-3.3"><span class="toc-item-num">3.3&nbsp;&nbsp;</span><code>namedtuple</code></a></span></li></ul></li><li><span><a href="#Regular-class" data-toc-modified-id="Regular-class-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>Regular class</a></span></li><li><span><a href="#Behind-the-scene" data-toc-modified-id="Behind-the-scene-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>Behind the scene</a></span></li><li><span><a href="#Data-class" data-toc-modified-id="Data-class-6"><span class="toc-item-num">6&nbsp;&nbsp;</span>Data class</a></span></li><li><span><a href="#Data-class---used-as-a-dictionary" data-toc-modified-id="Data-class---used-as-a-dictionary-7"><span class="toc-item-num">7&nbsp;&nbsp;</span>Data class - used as a dictionary</a></span></li><li><span><a href="#When-not-to-use-dataclass?" data-toc-modified-id="When-not-to-use-dataclass?-8"><span class="toc-item-num">8&nbsp;&nbsp;</span>When not to use dataclass?</a></span></li><li><span><a href="#Conclusions" data-toc-modified-id="Conclusions-9"><span class="toc-item-num">9&nbsp;&nbsp;</span>Conclusions</a></span></li><li><span><a href="#References" data-toc-modified-id="References-10"><span class="toc-item-num">10&nbsp;&nbsp;</span>References</a></span></li><li><span><a href="#Requirements" data-toc-modified-id="Requirements-11"><span class="toc-item-num">11&nbsp;&nbsp;</span>Requirements</a></span></li></ul></div>

# # Introduction
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-warning">
# <font color=black>
# 
# **What?** Data class
# 
# </font>
# </div>

# # Imports
# <hr style="border:2px solid black"> </hr>

# In[1]:


from collections import namedtuple
from dataclasses import dataclass


# # Data class vs. other data structures
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-info">
# <font color=black>
# 
# - For simple data structures, you have can use a `tuple`, `dict` and `namedtuple`. 
# - If `namedtuple` offers a lot of flexibiliy why even bother with data classes? First of all, data classes come with many more features. At the end of day even if `namedtuple` comes very close to what data class has to offer, by design is a `namedtuple` is a regular `tuple`.
# 
# </font>
# </div>

# ## `Tuple`

# In[2]:


queen_of_hearts_tuple = ('Q', 'Hearts')


# In[3]:


# Has no name access, just positional
queen_of_hearts_tuple[0]


# ## `dict`

# In[4]:


queen_of_hearts_dict = {'rank': 'Q', 'suit': 'Hearts'}


# In[5]:


# Would be nicer with .suit
queen_of_hearts_dict['suit']


# ## `namedtuple`

# In[6]:


NamedTupleCard = namedtuple('NamedTupleCard', ['rank', 'suit'])


# In[7]:


queen_of_hearts = NamedTupleCard('Q', 'Hearts')
queen_of_hearts.rank


# In[8]:


queen_of_hearts.suit


# # Regular class
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-info">
# <font color=black>
# 
# - Let's we'd like to build a class to describe a deck of cards.
# - At the same we'd like to specifically build a `print`and `=` methods inside the class.
# - We'll then compare this against the data classes.
# 
# </font>
# </div>

# In[9]:


class RegularCard:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __repr__(self):
        return (f'{self.__class__.__name__}'
                f'(rank={self.rank!r}, suit={self.suit!r})')

    def __eq__(self, other):
        if other.__class__ is not self.__class__:
            return NotImplemented
        return (self.rank, self.suit) == (other.rank, other.suit)


# In[10]:


# Instantiate the class
queen_of_hearts = RegularCard('Q', 'Hearts')


# In[11]:


queen_of_hearts.rank


# In[12]:


queen_of_hearts.suit


# In[13]:


# Calling hte __repr__ method
queen_of_hearts


# In[14]:


# Calling the method __eq__
queen_of_hearts == RegularCard('Q', 'Hearts')


# # Behind the scene
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-info">
# <font color=black>
# 
# - The following are all equivalent syntax
# 
# ```
# @dataclass
# class C:
#     ...
# 
# @dataclass()
# class C:
#     ...
# 
# @dataclass(init=True, repr=True, eq=True, order=False, unsafe_hash=False, frozen=False,
#            match_args=True, kw_only=False, slots=False, weakref_slot=False)
# class C:
#     ...
# ```
# 
# </font>
# </div>

# # Data class
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-info">
# <font color=black>
# 
# - Can we simplify what we have done above with a regular python class? Specifically can we reduce the amount of boiler plate code?
# - To give an idea why this may be beneficial look at `rank` and how many times is repeated: 3!
# - In short `dataclass` allows you to avoid having to write the class's constructor.
#     
# </font>
# </div>

# In[15]:


@dataclass
class DataClassCard:
    rank: str
    suit: str


# In[16]:


# Instantiate the class
queen_of_hearts = DataClassCard('Q', 'Hearts')


# In[17]:


queen_of_hearts.rank


# In[18]:


queen_of_hearts.suit


# In[23]:


# Calling the __repr__ method
queen_of_hearts


# In[20]:


# Calling the __str__ method
print(queen_of_hearts)


# In[21]:


# Calling the method __eq__
queen_of_hearts == DataClassCard('Q', 'Hearts')


# # Data class - used as a dictionary
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-info">
# <font color=black>
# 
# - If you would like to use the class as a key in a dictionary (instead of some hack I mentioned above like extracting IDs from classes and using them as keys), turn the class into “frozen”. 
# - This will auto-define the required `__hash__()` function.    
#     
# </font>
# </div>

# In[34]:


@dataclass(frozen=True)
class Foo:
    name: str
    int_valie: str
    float_value: float


# In[36]:


{Foo('foo', 1, 1/3)}


# In[46]:


@dataclass(frozen=True, order=True)
class Foo:
    name: str
    int_valie: str
    float_value: float


# In[45]:


sorted([Foo('foo', 1, 1/3), Foo("foo", 2, 1/2)])


# # When not to use dataclass?
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-info">
# <font color=black>
# 
# - Define a class as a dataclass if that class is small and only has a few attributes, having some 2 or 3 methods; otherwise, a regular class should be defined.
# - Do not use dataclass when most of the attributes are not initialised through arguments.
# - Do not use dataclass when you need to perform special actions in `__init__()`.
# - Do not use dataclass for custum `__init__` and custom `__new__`
# - Do not use daclass for various patterns that use inheritance.
# - Data classes are great when every attribute of the class is public. In contrast, they're not meant for classes that have private attributes.
#     
# </font>
# </div>

# # Conclusions
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-danger">
# <font color=black>
# 
# - Dataclasses are very useful to create classes that **just store attributes**.
# - Dataclasses resemble a lot with NamedTuples however namedtuples are immutable whereas dataclasses aren't (unless the frozen parameter is set to `True`.)
# - Dataclasses auto-generate automatically a lot of dunder methods for the user-defined classes
# 
#     
# </font>
# </div>

# # References
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-warning">
# <font color=black>
# 
# - [Data Classes in Python 3.7+ (Guide)](https://realpython.com/python-data-classes/)
# - [Python: To OOP or to FP?](https://towardsdatascience.com/python-to-oop-or-to-fp-13ac79a43b16)
# - [dataclasses — Data Classes](https://docs.python.org/3/library/dataclasses.html)
# - [Any reason not to use dataclasses everywhere?](https://www.reddit.com/r/Python/comments/ycn5ae/any_reason_not_to_use_dataclasses_everywhere/)
#     
# </font>
# </div>

# # Requirements
# <hr style="border:2px solid black"> </hr>

# In[ ]:


get_ipython().run_line_magic('load_ext', 'watermark')
get_ipython().run_line_magic('watermark', '-v -iv')


# In[ ]:




