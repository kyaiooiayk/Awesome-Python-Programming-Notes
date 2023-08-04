#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Introduction" data-toc-modified-id="Introduction-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Introduction</a></span></li><li><span><a href="#Things-to-know-about-python-functions" data-toc-modified-id="Things-to-know-about-python-functions-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Things to know about python functions</a></span></li><li><span><a href="#List-of-function-special-methods" data-toc-modified-id="List-of-function-special-methods-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>List of function special methods</a></span></li><li><span><a href="#__annotations__" data-toc-modified-id="__annotations__-4"><span class="toc-item-num">4&nbsp;&nbsp;</span><code>__annotations__</code></a></span></li><li><span><a href="#__call__" data-toc-modified-id="__call__-5"><span class="toc-item-num">5&nbsp;&nbsp;</span><code>__call__</code></a></span></li><li><span><a href="#__class__" data-toc-modified-id="__class__-6"><span class="toc-item-num">6&nbsp;&nbsp;</span><code>__class__</code></a></span></li><li><span><a href="#__closure__" data-toc-modified-id="__closure__-7"><span class="toc-item-num">7&nbsp;&nbsp;</span><code>__closure__</code></a></span></li><li><span><a href="#__code__" data-toc-modified-id="__code__-8"><span class="toc-item-num">8&nbsp;&nbsp;</span><code>__code__</code></a></span></li><li><span><a href="#__defaults__" data-toc-modified-id="__defaults__-9"><span class="toc-item-num">9&nbsp;&nbsp;</span><code>__defaults__</code></a></span></li><li><span><a href="#__delattr__" data-toc-modified-id="__delattr__-10"><span class="toc-item-num">10&nbsp;&nbsp;</span><code>__delattr__</code></a></span></li><li><span><a href="#__dict__" data-toc-modified-id="__dict__-11"><span class="toc-item-num">11&nbsp;&nbsp;</span><code>__dict__</code></a></span></li><li><span><a href="#__dir__" data-toc-modified-id="__dir__-12"><span class="toc-item-num">12&nbsp;&nbsp;</span><code>__dir__</code></a></span></li><li><span><a href="#__doc__" data-toc-modified-id="__doc__-13"><span class="toc-item-num">13&nbsp;&nbsp;</span><code>__doc__</code></a></span></li><li><span><a href="#__eq__" data-toc-modified-id="__eq__-14"><span class="toc-item-num">14&nbsp;&nbsp;</span><code>__eq__</code></a></span></li><li><span><a href="#__format__" data-toc-modified-id="__format__-15"><span class="toc-item-num">15&nbsp;&nbsp;</span><code>__format__</code></a></span></li><li><span><a href="#__ge__" data-toc-modified-id="__ge__-16"><span class="toc-item-num">16&nbsp;&nbsp;</span><code>__ge__</code></a></span></li><li><span><a href="#__get__" data-toc-modified-id="__get__-17"><span class="toc-item-num">17&nbsp;&nbsp;</span><code>__get__</code></a></span></li><li><span><a href="#__getattribute__" data-toc-modified-id="__getattribute__-18"><span class="toc-item-num">18&nbsp;&nbsp;</span><code>__getattribute__</code></a></span></li><li><span><a href="#__globals__" data-toc-modified-id="__globals__-19"><span class="toc-item-num">19&nbsp;&nbsp;</span><code>__globals__</code></a></span></li><li><span><a href="#__gt__" data-toc-modified-id="__gt__-20"><span class="toc-item-num">20&nbsp;&nbsp;</span><code>__gt__</code></a></span></li><li><span><a href="#__hash__" data-toc-modified-id="__hash__-21"><span class="toc-item-num">21&nbsp;&nbsp;</span><code>__hash__</code></a></span></li><li><span><a href="#__init__" data-toc-modified-id="__init__-22"><span class="toc-item-num">22&nbsp;&nbsp;</span><code>__init__</code></a></span></li><li><span><a href="#__init_subclass__" data-toc-modified-id="__init_subclass__-23"><span class="toc-item-num">23&nbsp;&nbsp;</span><code>__init_subclass__</code></a></span></li><li><span><a href="#__kwdefaults__" data-toc-modified-id="__kwdefaults__-24"><span class="toc-item-num">24&nbsp;&nbsp;</span><code>__kwdefaults__</code></a></span></li><li><span><a href="#__le__" data-toc-modified-id="__le__-25"><span class="toc-item-num">25&nbsp;&nbsp;</span><code>__le__</code></a></span></li><li><span><a href="#__lt__" data-toc-modified-id="__lt__-26"><span class="toc-item-num">26&nbsp;&nbsp;</span><code>__lt__</code></a></span></li><li><span><a href="#__name__" data-toc-modified-id="__name__-27"><span class="toc-item-num">27&nbsp;&nbsp;</span><code>__name__</code></a></span></li><li><span><a href="#__module__" data-toc-modified-id="__module__-28"><span class="toc-item-num">28&nbsp;&nbsp;</span><code>__module__</code></a></span></li><li><span><a href="#__ne__" data-toc-modified-id="__ne__-29"><span class="toc-item-num">29&nbsp;&nbsp;</span><code>__ne__</code></a></span></li><li><span><a href="#__new__" data-toc-modified-id="__new__-30"><span class="toc-item-num">30&nbsp;&nbsp;</span><code>__new__</code></a></span></li><li><span><a href="#__next__" data-toc-modified-id="__next__-31"><span class="toc-item-num">31&nbsp;&nbsp;</span><code>__next__</code></a></span></li><li><span><a href="#__qualname__" data-toc-modified-id="__qualname__-32"><span class="toc-item-num">32&nbsp;&nbsp;</span><code>__qualname__</code></a></span></li><li><span><a href="#__reduce__" data-toc-modified-id="__reduce__-33"><span class="toc-item-num">33&nbsp;&nbsp;</span><code>__reduce__</code></a></span></li><li><span><a href="#__reduce_ex__" data-toc-modified-id="__reduce_ex__-34"><span class="toc-item-num">34&nbsp;&nbsp;</span><code>__reduce_ex__</code></a></span></li><li><span><a href="#__repr__-&amp;-__str__" data-toc-modified-id="__repr__-&amp;-__str__-35"><span class="toc-item-num">35&nbsp;&nbsp;</span><code>__repr__</code> &amp; <code>__str__</code></a></span></li><li><span><a href="#__setitem__" data-toc-modified-id="__setitem__-36"><span class="toc-item-num">36&nbsp;&nbsp;</span><code>__setitem__</code></a></span></li><li><span><a href="#__setattr__" data-toc-modified-id="__setattr__-37"><span class="toc-item-num">37&nbsp;&nbsp;</span><code>__setattr__</code></a></span></li><li><span><a href="#__sizeof__" data-toc-modified-id="__sizeof__-38"><span class="toc-item-num">38&nbsp;&nbsp;</span><code>__sizeof__</code></a></span></li><li><span><a href="#__subclasshook__" data-toc-modified-id="__subclasshook__-39"><span class="toc-item-num">39&nbsp;&nbsp;</span><code>__subclasshook__</code></a></span></li><li><span><a href="#Check-them-all-in-a-loop" data-toc-modified-id="Check-them-all-in-a-loop-40"><span class="toc-item-num">40&nbsp;&nbsp;</span>Check them all in a loop</a></span></li><li><span><a href="#References" data-toc-modified-id="References-41"><span class="toc-item-num">41&nbsp;&nbsp;</span>References</a></span></li></ul></div>

# # Introduction
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-warning">
# <font color=black>
# 
# **What?** Dunder (double underscore) methods
# 
# </font>
# </div>

# # Things to know about python functions

# - Each function in python is treated as an object.
# - Each function in python has special method identified by a preceeding and trainling dunder: `__`
# - Dunder (Doble UNDERscore) methods are also called **magic method**.
# - This notebook explore each one of them through examples.
# - Python functions are first class objects.

# # List of function special methods

# - Let us create a dummy function which takes no arguments and returns nothing.
# - We'll then apply the method `dir` and explore what methods are available.
# - The **common pattern** here is that the magic method is there to customise the result of python built-in funciton. So for instance, - `__subclasscheck__` is one of the methods to customise the result of `issubclass()` built-in function. 

# In[1]:


def func():
    pass


# In[2]:


dir(func)


# - Just in case you are wondering.
# - This looks fairly similar to the output of `dir(class_instantiation)`.
# - What are the differences?

# In[3]:


class A():
    pass


# In[4]:


a = A()


# In[5]:


dir(a)


# # `__annotations__`

# - They are generally used to attach metadata to functions describing their parameters and return values.
# - The symbol0 `->` marks the return function annotation.
# - Annotation are dictionary.
# - You can also provide another dictionary rather than a simple string.

# In[6]:


def func_1(a: "this is argument a") -> "This is a squared":
    return a**2


# In[7]:


# first way to call
func_1


# In[8]:


# second way to call
func_1.__annotations__


# In[9]:


# Annotations is a dictionary
'{:,} {}'.format(func_1(2),
                 func_1.__annotations__['return'])


# In[10]:


rd = {'type': float, 'units': 'Joules',
      'docstring': 'Given mass and velocity returns kinetic energy in Joules'}

def func_2() -> rd:
    pass


# In[11]:


for i in ['type', "units", "docstring"]:
    print(func_2.__annotations__['return'][i])


# # `__call__`

# - `__call__` is a built-in method which enables to write classes where the **instances behave like functions** and can be called like a function.
# - In practice: `object()` is shorthand for `object.__call__()`
# - `__init__()` is properly defined as Class Constructor which builds an instance of a class, whereas `__call__` makes such a instance callable as a function and therefore can be modifiable.
# - Technically `__init__` is called once by `__new__` when object is created, so that it can be initialised
# - But there are many scenarios where you might want to redefine your object, say you are done with your object, and may find a need for a new object. With `__call__` you can redefine the same object as if it were new.

# In[12]:


class Product():
    def __init__(self):
        print("Instance created")

    # Defining __call__ method
    def __call__(self, a, b):
        print("Instance is called via special method __call__")
        print(a*b)


# In[13]:


p = Product()


# In[14]:


# This is equivalent to
p.__init__()


# In[15]:


# Since Product has  a __call_ method, p can be called like a function
p(2,3)


# In[16]:


# The cell above is equivalent to this call
p.__call__(2,3)


# # `__class__`

# - `__class__` is an attribute on the object that refers to the class from which the object was created.
# - As functions are also objects in Python, we can find their `type` or class using the type function or the `__class__` attribute.

# In[17]:


def simple_function():
    pass


# In[18]:


type(simple_function)


# In[19]:


simple_function.__class__


# # `__closure__`

# - A closure is a function object **that remembers values** in enclosing scopes **even if** they are not present in memory. 
# - The `__closure__` attribute of a closure function returns a tuple of cell objects. 
# - This cell object also has an attribute called cell_contents, which returns returns the contents of the cell.
# - In the above example, the nested function power has `__closure__` attribute associated with it and it returns a tuple of cell objects. 
# - The cell_contents attribute returns the value 3 as it was closed inside the cell object.

# In[20]:


# this is a nested function
def gfg(raise_power_to):

    def power(number):
        return number ** raise_power_to
    return power


# In[21]:


raise_power_to_3 = gfg(3)


# In[22]:


print(raise_power_to_3.__closure__)


# In[23]:


print(raise_power_to_3.__closure__[0].cell_contents)


# # `__code__`

# - Every function in Python has a __code__ attribute that holds its code object.
# - When called, we get back some representation of the code object, which is almost useless to us. What's a lot more useful is to inspect further attributes on this code object:
#     
#     - `co_nlocals` — is the number of local variables used by the function (including arguments).
#     - `co_argcount` — is the total number of positional arguments (including positional-only arguments and arguments with default values).
#     - `co_varnames` — is a tuple containing the names of the local variables (starting with the argument names).
#     - `co_names` — is a tuple containing the names used by the bytecode.
#     - `co_cellvars` — is a tuple containing the names of local variables that are referenced by nested functions.
#     - `co_freevars` — is a tuple containing the names of free variables; co_code is a string representing the sequence of bytecode instructions.
#     - `co_posonlyargcount` — is the number of positional-only arguments (including arguments with default values).
#     - `co_kwonlyargcount` — is the number of keyword-only arguments (including arguments with default values).
#     - `co_firstlineno` — is the first line number of the function.
#     - `co_lnotab` — is a string encoding the mapping from bytecode offsets to line numbers (for details see the source code of the interpreter).
#     - `co_stacksize` — is the required stack size.
#     - `co_code' — is a string representing the sequence of bytecode instructions.
#     - `co_consts` — is a tuple containing the literals used by the bytecode.
#     - `co_flags` — is an integer encoding a number of flags for the interpreter.

# In[24]:


def func_3(x):
    return x


# In[25]:


func_3.__code__


# In[26]:


func_3.__code__.co_nlocals


# In[27]:


func_3.__code__.co_argcount


# # `__defaults__`

# - Shows the default attribute of the function.
# - `__defaults__` is a tuple containing default argument values for those arguments that have defaults (r None if no arguments have a default value.
# - Their default arguments values are evaluated on definition and stored in the special attributes.`__defaults__` and `__kwdefaults__`.
# - Default argument values are stored in the function object and not the code object (since they represent values calculated at runtime).

# In[28]:


def func(a, b):
    pass


# In[29]:


print(func.__defaults__)


# In[30]:


func.__defaults__ is None


# In[31]:


def foobar(element, data=[]):
    data.append(element)
    return data


# In[32]:


# Before execution
foobar.__defaults__


# In[33]:


foobar(12)


# In[34]:


foobar(12)


# In[35]:


foobar.__defaults__


# # `__delattr__`

# - Called when an attribute deletion is attempted.
# - Like `__setattr__()` but for attribute deletion instead of assignment. 
# - This should only be implemented if del `obj.name` is meaningful for the object.

# In[36]:


class Frob():
    def __delattr__(self, name):
        print("deleting `{}`".format(str(name)))
        del self.__dict__[name]
        print("`{}` deleted".format(str(name)))


# In[37]:


f = Frob()


# In[38]:


dir(f)


# In[39]:


# Adding a class (instance?) attribute
f.dummy = 10


# In[40]:


# Now you show be able to see "dummy" listed there
dir(f)


# In[41]:


del f.dummy


# # `__dict__`

# - Basically it contains all the attributes which describe the object in question. It can be used to alter or read the attributes.

# In[3]:


def func_1():
    pass

func_1.temp = 1

print(func_1.__dict__)


# In[4]:


def func_2():
    pass

print(func_2.__dict__)


# In[5]:


class TempClass:
    a = 1

    def temp_function(self):
        pass


print(TempClass.__dict__)


# - As we saw above, the namespace can be accessed with `__dict__`.
# - Another way to see its contents is to type `vars()`.

# In[6]:


import math
vars(math).items()


# In[7]:


dir(math)


# # `__dir__`

# - `dir([object])`¶ Without arguments, return the list of names in the current local scope. With an argument, attempt to return a list of valid attributes for that object.
# 
# - If the object has a method named `__dir__()`, this method will be called and must return the list of attributes. This allows objects that implement a custom `__getattr__()` or `__getattribute__()` function to customize the way `dir()` reports their attributes.
# 
# - If the object does not provide `__dir__()`, the function tries its best to gather information from the object’s `__dict__`attribute, if defined, and from its type object. The resulting list is not necessarily complete, and may be inaccurate when the object has a custom `__getattr__()`.
# 
# - `dir` calls `__dir__` internally.

# In[45]:


class Hello():
    def __dir__(self):
        print("calling __dir__")
        return [1, 2, 3]


# In[46]:


hello = Hello()


# In[47]:


dir(hello)


# In[48]:


hello.__dir__()


# # `__doc__`

# - Python objects have an attribute called __doc__ that provides a documentation of the object. 
# - For example, you simply call Dog.__doc__ on your class Dog to retrieve its documentation as a string. 

# In[49]:


class Dog:
    """Your best friend."""

    def do_nothing(self):
        pass


# In[50]:


print(Dog.__doc__)


# In[51]:


# It works the same even after instantiation
dog = Dog()
dog.__doc__


# # `__eq__`

# - Implement the Python `__eq__` method to define the equality logic for comparing two objects using the equal operator `==`.
# - Python automatically calls the `__eq__` method of a class when you use the `==` operator to compare the instances of the class. By default, Python uses the is operator if you don’t provide a specific implementation for the `__eq__` method.
# - 

# In[52]:


class Person:
    """
    The following shows how to implement the __eq__ method 
    in the Person class that returns True if two person 
    objects have the same age:
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __eq__(self, other):
        print("calling dunder method __eq__")
        return self.age == other.age


# In[53]:


john = Person('John', 'Doe', 25)
jane = Person('Jane', 'Doe', 25)
print(john == jane)


# # `__format__`

# - Each Python type can control formatting of its instances by defining a __format__ method. 
# 
# - The `__format__` method is responsible for interpreting the format specifier, formatting the value, and returning the resulting string.
# 
# - The new, global built-in function `format` simply calls this special method, similar to how `len()` and `str()` simply call their respective special methods.

# In[54]:


# custom __format__() method
class Person:
    def __format__(self, format):
        if(format == 'age'):
            return '23'
        return 'None'


# In[55]:


# The format() function internally runs Person().__format__("age") to return 23.
format(Person(), "age")


# # `__ge__`

# - To customize the behavior of the greather than or equal to operator x >= y, override the `__ge__()` dunder method in your class definition.
# - Python internally calls `x.__ge__(y)` to obtain a return value when comparing two objects using `x >= y`.

# In[56]:


class Person:
    def __init__(self, age):
        self.age = age

    def __ge__(self, other):
        print("Calling dunder method __ge__")
        return self.age >= other.age


# In[57]:


alice = Person(18)
bob = Person(17)
carl = Person(18)


# In[58]:


print(alice >= bob)
print(alice >= carl)
print(bob >= alice)


# # `__get__`

# - Called to get the attribute of the owner class (class attribute access) or of an instance of that class (instance attribute access).

# In[59]:


# This is our descriptor object
class Bar():
    def __init__(self):
        self.value = ''

    def __get__(self, instance, owner):
        print("returned from descriptor object")
        return self.value

    def __set__(self, instance, value):
        print("set in descriptor object")
        self.value = value

    def __delete__(self, instance):
        print("deleted in descriptor object")
        del self.value


class Foo(object):
    bar = Bar()


# In[60]:


f = Foo()


# In[61]:


f.bar = 10


# In[62]:


print(f.bar)


# In[63]:


del f.bar


# # `__getattribute__`

# - `__getattr__` called when an attribute lookup **has not found** the attribute in the usual places.
# - Note that if the attribute is found through the normal mechanism, `__getattr__()` is not called. 
# - This is done both for efficiency reasons and because otherwise `__getattr__()` would have no way to access other attributes of the instance.
# - Note that at least for instance variables, you can fake total control by not inserting any values in the instance attribute dictionary (but instead inserting them in another object). See the `__getattribute__()` method below for a way to actually get total control in new-style classes.

# In[64]:


class Yeah(object):
    def __init__(self, name):
        # Gets called when an attribute is accessed
        self.name = name

    def __getattribute__(self, item):
        print('__getattribute__ ', item)
        # Calling the super class to avoid recursion
        # Gets called when the item is not found via __getattribute__
        return super(Yeah, self).__getattribute__(item)

    def __getattr__(self, item):
        print('__getattr__ ', item)
        return super(Yeah, self).__setattr__(item, 'orphan')


# In[65]:


y1 = Yeah('yes')
y1.name


# In[66]:


y1.foo


# In[67]:


y1.foo


# In[68]:


y1.goo


# In[69]:


y1.__dict__


# # `__globals__`

# - Python functions keep a reference to the non-local variables used in the following attributes
#     - `__globals__` This is a reference to the module globals dict.
#     - `__closure__` Variables used in the function closure.
# 

# In[70]:


def one():
    return 'one'

def three(param):
    def two():
        print(one(), param)
    return two


# In[71]:


inst = three('hello')


# In[72]:


inst()


# In[73]:


# This would not work well in a notebook as it keeping all the variables run in this notebook!
inst.__globals__


# In[74]:


inst.__closure__


# In[75]:


inst.__closure__[0].cell_contents


# # `__gt__`

# - To customize the behavior of the greather than operator `x > y`, override the `__gt__()` dunder method in your class definition.
# - Python internally calls `x.__gt__(y)` to obtain a return value when comparing two objects using `x > y`.

# In[76]:


class Person:
    def __init__(self, age):
        self.age = age

    def __gt__(self, other):
        return self.age > other.age


# In[77]:


alice = Person(18)
bob = Person(17)
carl = Person(18)


# In[78]:


print(alice > bob)
print(alice > carl)
print(bob > alice)


# # `__hash__`

# - An object hash is an integer number representing the value of the object and can be obtained using the `hash()` function if the object is hashable.
# - To make a class hashable, it has to implement both the `__hash__(self)` method and the aforementioned `__eq__(self, other)` method. 
# - As with equality, the inherited `object.__hash__` method works by identity only: barring the unlikely event of a hash collision, two instances of the same class will always have different hashes, no matter what data they carry.
# - So hashes are important because sets and dictionaries use them for their lookup tables to quickly find their keys. To do that effectively, they make an important assumption that leads to our first gotcha:
# - The hash of an object must never change during its lifetime.

# In[79]:


class C:
    def __init__(self, x):
        self.x = x

    def __repr__(self):
        return f"C({self.x})"

    def __hash__(self):
        return hash(self.x)

    def __eq__(self, other):
        return (
            self.__class__ == other.__class__ and
            self.x == other.x
        )


# In[80]:


d = dict()
s = set()
c = C(1)
d[c] = 42
s.add(c)


# In[81]:


d, s


# In[82]:


c in s and c in d  # c is in both!


# In[83]:


c.x = 2


# In[84]:


c in s or c in d   # c is in neither!?


# In[85]:


d, s
#({C(2): 42}, {C(2)})   # but...it's right there!


# # `__init__`

# - In python everything is an object, but classess and objects are not exactly the same thing. You can create an object instantiating a class though.
# - Classes can be thought as blueprint for creating object. In other words, I've created a sort of instruction manual for constructing a customer object.

# In[116]:


class Customer(object):
    """A customer of ABC bank with a checking. account.
    
    Customer have the following propperties:
    
    Atributes:
        name: a string representing the custome name
        balance: a float. tracking the current balance of the customer's account
    """
    
    def __init__(self, name, balance = 0.0):
        """Object initialisation.
        
        Returns a customers objkect whose name is name and stating
        balance is balance.
        """
        
        self.name = name
        self.balance = balance
        
    def withdraw(self, amount):
        """Withdraw.
        
        Returns the balance remaininga fter withdrawing ana mount.
        """
        
        if amount > self.balance:
            raise RuntimeError("Amount requested is greater than the current balance")
        self.balance -= amount
        
        return self.balance
    
    def deposit(self, amount):
        """Deposit.
        
        Returns the balance remaining after depositing some monies.
        """
        
        self.balance += amount
        
        return sel.balance


# - The class Customer(object) does not create a new customer, as we have created a blueprint only.
# - How do we create a real customer then? We;ll have to call the special class method __init__ to create one.
# - This method is call automtically when we. instantiate the obejct with (for instance) Customer("Charlier", 100). This is saying "hey create a customer named Charlie with 100GBP in his account!.

# In[117]:


custormerA = Customer("Charlier", 100)
custormerB = Customer("Maria", 200)
customerNull = Customer("Null")


# In[118]:


custormerA.__dict__


# In[119]:


custormerB.__dict__


# In[120]:


customerNull.__dict__


# # `__init_subclass__`

# - It offers a simpler form of customization for classes. 
# - This is like a shortcut to extend the functionalities of base classes without having to handle with metaclasses.

# In[121]:


class Philosopher:
    def __init_subclass__(cls, default_name, **kwargs):
        super().__init_subclass__(**kwargs)
        print(f"Called __init_subclass({cls}, {default_name})")
        cls.default_name = default_name


class AustralianPhilosopher(Philosopher, default_name="Bruce"):
    pass


class GermanPhilosopher(Philosopher, default_name="Nietzsche"):
    default_name = "Hegel"
    print("Set name to Hegel")


# In[122]:


Bruce = AustralianPhilosopher()
Mistery = GermanPhilosopher()
print(Bruce.default_name)
print(Mistery.default_name)


# # `__kwdefaults__`

# - The `__kwdefaults__` attribute holds a dict containing defaults for keyword-only arguments.

# In[123]:


def func(a, b='Default value'):
    pass


# In[124]:


func.__defaults__


# In[125]:


print(func.__kwdefaults__)


# # `__le__`

# In[126]:


class Person:
    """
    The following shows how to implement the __eq__ method 
    in the Person class that returns True if two person 
    objects have the same age:
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __le__(self, other):
        print("calling dunder method __eq__")
        return self.age == other.age


# In[127]:


john = Person('John', 'Doe', 25)
jane = Person('Jane', 'Doe', 26)
print(john <= jane)


# # `__lt__`

# In[128]:


class Person:
    """
    The following shows how to implement the __eq__ method 
    in the Person class that returns True if two person 
    objects have the same age:
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __lt__(self, other):
        print("calling dunder method __eq__")
        return self.age == other.age


# In[129]:


john = Person('John', 'Doe', 25)
jane = Person('Jane', 'Doe', 26)
print(john < jane)


# # `__name__`
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
#     
# - `__name__` is a variable defined for each script that defines whether the script is being run as the main module or it is being run as an imported module.
# 
# - `__name__` variable points to the namespace wherever the Python interpreter happens to be at the moment.
# 
# - The global variable, name, in the module that is the entry point to your program, is __main__.
# 
# - So, the code under the if block runs if the module is the entry point to your program.
# 
# - **In practice?** It allows the code in the module to be importable by other modules, without executing the code block beneath on import.
#     
# - In other words, the statement `if__name__=="__main__"` is a very Pythonic way of making sure some code only
# runs if the program is ran directly.
# 
# </font>
# </div>

# ![image.png](attachment:image.png)

# <div class="alert alert-info">
# <font color=black>
# 
# - **If you are not** using the construct `__name__ == "__main__"` the name` is assigned to the name you import the module by.
# 
# </font>
# </div>

# In[130]:


def func_3():
    pass


# In[131]:


func_3.__name__


# # `__module__`

# - Every Python class has a built-in class attribute __module__ which is the name of the module in which the class is defined. 
# - A module in Python is a file (ending in .py) that contains a set of definitions (variables and functions) that you can use when they are imported. 
# - Modules are considered as objects, just as everything else is in Python. 
# - Many methods can operate on modules.

# In[132]:


from math import sin
# Function sin() came from the math module.
sin.__module__


# In[133]:


# Define a dummy class
class A:    
    pass


a = A
a.__module__


# In[ ]:





# # `__ne__`

# - Equality in Python is more complicated than most people realize but at its core you have to implement a `__eq__` (self, other) method. 
# 
# - It should return either a boolean value if your class knows how to compare itself to other or `NotImplemented` if it doesn’t. 
# 
# - For inequality checks using `!=`, the corresponding method is `__ne__(self, other)`.
# 
# - By default, those methods are inherited from the object class that compares two instances by their identity – therefore instances are only equal to themselves.
# 
# - A common mistake in Python 2 was to override only `__eq__()` and forget about `__ne__()`. Python 3 is friendly enough to implement an obvious `__ne__()` for you, if you don’t yourself.

# In[134]:


class Person:
    """
    The following shows how to implement the __eq__ method 
    in the Person class that returns True if two person 
    objects have the same age:
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __ne__(self, other):
        print("calling dunder method __ne__")
        return self.age != other.age


# In[135]:


john = Person('John', 'Doe', 25)
jane = Person('Jane', 'Doe', 26)
print(john != jane)


# # `__new__`

# - Transforming from class to an object is called instantiation.
# - `__init__` is used to objects initialization and provide a classs witha contructor.
#     - During object creation `__init__` method doesn’t get executed first, the method which gets executed first is __new__
#     - `__new__()` method gets most of the same arguments at init and it is responsible for actually creating the new object (prior to initializing object) .
# - We can use `__new__` when we need to control the creation of a new instance.
# - Consider this problem:
#     - Let we have a 3 classes, File ,TextFile(File) and ImageFile(File) . We need instantiate TextFile for Text files, ImageFile for image file, and File for other type of files. We can obtain this by instantiating them directly.
#     - But what if we could instantiate them only using the parent class (File ) depending the file content? Yes, we want to instantiate child classes using parent class!

# In[136]:


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


# In[137]:


"""
Here, we are instantiating the TextFile, ImageFile and File classes using the File (parent)
class depending on content of file (file_type). 
"""
text_file = File(file_name="testfile.txt", height=100, width=100)
image_file = File(file_name="imagefile.png", file_size=500)
other_file = File(file_name="video_file.mp4")


# In[138]:


print(text_file)
print(image_file)
print(other_file)


# # `__next__`

# - All iterators can be placed to the right of the in keyword in for loop statements.
# - The interpreter calls `iterator.___next___()` and repeats until a `StopIteration` error occurs.

# In[15]:


a = [1,2,3,4]


# In[16]:


for i in a:
    print(i)


# In[17]:


a = iter(a)
while True:
    print(a.__next__())


# # `__qualname__`

# - The `__qualname__` attribute means qualified name in Python. 
# - It gives you a **dotted path** to the name of the target object.
# - Using `__qualname__` is useful with nested structures, such as when you have a method inside a class
# - **Difference?** With nested structures:
#     - The `__qualname__` returns a path to the object
#     - The `__name__` attribute does not.

# In[139]:


class Example:
    def something_level_1():
        def something_level_2():
            pass


# In[140]:


print(Example.something_level_1.__qualname__)


# In[141]:


class Example:
    def something():
        pass
print(Example.something.__name__)
print(Example.something.__qualname__)


# - Using `__qualname__` is useful if you have a function and a method with the same names. 
# - Using `__qualname__` you are able to see the difference between the method and the function based on the path it returns.

# In[142]:


def something():
    pass


class Example:
    def something():
        pass


# In[143]:


# Using __name__ you would not be able to tell the difference
print(something.__name__)
print(Example.something.__name__)


# In[144]:


# Using __qualname__ you would not be able to tell the difference
print(something.__qualname__)
print(Example.something.__qualname__)


# # `__reduce__`

# - When you try to pickle an object, there might be some properties that don't serialize well. 
# - One example of this is an open file handle. Pickle won't know how to handle the object and will throw an error.
# - You can tell the pickle module how to handle these types of objects natively within a class directly.

# In[145]:


import pickle


class Test(object):
    def __init__(self, file_path="test1234567890.txt"):
        # An open file in write mode
        self.some_file_i_have_opened = open(file_path, 'wb')


my_test = Test()
# Now, watch what happens when we try to pickle this object: it should throw an error
pickle.dumps(my_test)


# In[146]:


import pickle


class Test(object):
    def __init__(self, file_path="test1234567890.txt"):
        # Used later in __reduce__
        self._file_name_we_opened = file_path
        # An open file in write mode
        self.some_file_i_have_opened = open(self._file_name_we_opened, 'wb')

    def __reduce__(self):
        # we return a tuple of class_name to call,
        # and optional parameters to pass when re-creating
        return (self.__class__, (self._file_name_we_opened, ))


my_test = Test()
saved_object = pickle.dumps(my_test)
# Just print the representation of the string of the object,
# because it contains newlines.
print(repr(saved_object))


# In[147]:


get_ipython().system('ls')


# In[148]:


# Getting rid of the save file
get_ipython().system('rm  ./test1234567890.txt')


# # `__reduce_ex__`

# - `__reduce_ex__` is what `__reduce__` should have been but never became. 
# - `__reduce_ex__` works like `__reduce__` but the pickle protocol is passed.
# - At pickling time `__reduce__()` will be called with no arguments, and it must return either a string or a tuple.
# - It is sometimes useful to know the protocol version and this can be done by implementing a method named `__reduce_ex__`.
# - `__reduce_ex__` is preferred over over `__reduce__` (you may still provide `__reduce__` for backwards compatibility). 
# - The `__reduce_ex__` method will be called with a single integer argument, the protocol version.

# # `__repr__` & `__str__`

# - They both represent the object but the `__repr__` method tells you more.
# - So much more that you can also reconstruct the object based on that information.
# - Also Python interpreter sessions use `__repr__` to inspect objects.
# - `__str__` should have a readable output.

# In[149]:


import numpy as np

class Tensor(object):
    
    def __init__(self, data):
        """__init__ method
        Given a list, tunrs it into an array
        """        
        self.data = np.array(data)
    
    def __add__(self, other):
        """__add__ method        
        Add two tensor together
        """
        return Tensor(self.data + other.data)
    
    def __repr__(self):
        print("calling __repr__")
        """__repr__ method
        Returns the object representation in string format.
        Retunrs and official string representation of the object,
        which can be ised to construt the object again.
        """
        return str(self.data.__repr__())
    
    def __str__(self):
        print("calling __str__")
        """
        Returns the string representation of the object. This method is called
        when print() or str() function is invoked on an object. Retunrs a 
        human-redeable string format.
        """
        return str(self.data.__str__())


# In[150]:


x = Tensor([1,2,3,4,5])
x


# In[151]:


repr(x)


# In[152]:


str(x)


# In[153]:


print(x)


# # `__setitem__`

# - The square bracket assignment notation is just a convenient interface to a method call.
# - What actually happens is that Python calls the `__setitem__` method.
# - If you wanted to you could modify the __setitem__ method, so that square bracket assignment does something totally different.

# In[1]:


x = ['a', 'b']
x[0] = 'aa'  # Item assignment using square bracket notation
x


# In[2]:


x = ['a', 'b']
x.__setitem__(0, 'aa')  # Equivalent to x[0] = 'aa'
x


# # `__setattr__`

# - Python’s magic method `__setattr__()` implements the built-in `setattr()` function that takes an object and an attribute name as arguments and **removes the attribute from the object**.
# - Let’s have a look at an example where you override the `__setattr__` magic method of a custom class.
# - Person to simply print out the arguments rather than really changing the attributes of the class as the default `setattr()` function would do.

# In[154]:


class Person:
    def __setattr__(self, attr_name, attr_value):
        print(attr_name, attr_value)


# In[155]:


alice = Person()
setattr(alice, 'age', 32)
# age 32


# - If we did not  overridden the `__setattr__()` magic method, Python would’ve created a new attribute for the alice instance, so when calling `alice.age`, you’d have obtained the value 32. 

# In[156]:


class Person_diff:
    pass


# In[157]:


alice_diff = Person_diff()
setattr(alice_diff, 'age', 32)


# In[158]:


alice_diff.__dict__


# # `__sizeof__`

# - So let us look at the two ways of getting the size of a particular object in Python. These are `getsizeof()` method and `__sizeof()` method. 
# - The `getsizeof()` is a system-specific method and hence we have to import the sys module to use it. A sample code is as shown below for calculating the size of a list.

# In[159]:


import sys
a = [1, 2]
b = [1, 2, 3, 4]
c = [1, 2, 3, 4]
d = [2, 3, 1, 4, 66, 54, 45, 89]
print(sys.getsizeof(a))
print(sys.getsizeof(b))
print(sys.getsizeof(c))
print(sys.getsizeof(d))


# - `getsizeof()` method calls the `__sizeof__()` method o the object with an additional garbage collector overhead. 
# - Hence the size returned by the `getsize()` method will be more than that returned by the `__sizeof()__` method. 

# In[160]:


w = [1, 2]
x = [4, 5, 7, 9]
y = [2, 8, 6, 56, 45, 89, 88]
z = [54, 45, 12, 23, 24, 90, 20, 40]
print(w.__sizeof__())
print(x.__sizeof__())
print(y.__sizeof__())
print(z.__sizeof__())


# # `__subclasshook__`

# - `__subclasscheck__` is one of the methods to customize the result of `issubclass()` built-in function. 
# - It is a method to check whether a class is a subclass or not and returns True if the class is considered as a subclass(direct or indirect) of another class, otherwise, returns False. 
# - It cannot be defined as a class method in the actual/real class. It is implemented in the metaclass, as it is not for ordinary classes. 
# - **Example** consider a situation where you want to check if a certain value is present as an attribute inside a class using the `issubclass()` method.

# In[161]:


class A(type):

    # __subclasscheck__() defined
    def __subclasscheck__(cls, sub):

        # Getting the L attribute of
        # subclass
        attr = getattr(cls, 'L', [])

        # Checking if the subclass
        # is present in the L attribute
        # of subclass or not
        if sub in attr:
            return True

        return False


class B(metaclass=A):

    # L Attribute
    L = [1, 2, 3, 4, 5]


class C(metaclass=A):

    # L Attribute
    L = ["Geeks", "For"]


# In[162]:


# Driver's code
print(issubclass(1, B))
print(issubclass("Geeks", B))
print(issubclass("Geeks", C))


# # Check them all in a loop

# In[164]:


def check_in_a_loop():
    pass


# In[165]:


dir(check_in_a_loop)


# In[166]:


check_in_a_loop.__dict__


# In[167]:


for i in dir(check_in_a_loop):
    print(i)
    print(eval("check_in_a_loop."+str(i)))


# # References
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-warning">
# <font color=black>
# 
# - https://www.honeybadger.io/blog/python-instantiation-metaclass/
# - [`__closure__`](https://www.geeksforgeeks.org/__closure__-magic-function-in-python/)
# - [`__code__`](https://www.codeguage.com/courses/python/functions-code-objects)
# - [`__default__` #1](https://betterprogramming.pub/mutable-default-arguments-in-python-643ae2583e00)
# - [`__default__` #2](https://mdawar.dev/blog/mock-python-default-function-argument)
# - [`__deleteattr`](https://python-reference.readthedocs.io/en/latest/docs/dunderattr/delattr.html)
# - [`__dir__`](https://stackoverflow.com/questions/19703335/whats-the-difference-between-dir-and-dir)
# - [`__doc__`](https://blog.finxter.com/what-is-__-doc-__-in-python/)
# - [`__eq_`](https://www.pythontutorial.net/python-oop/python-__eq__/)
# - [`__format__`](https://peps.python.org/pep-3101/)
# - [`__get__`](https://python-reference.readthedocs.io/en/latest/docs/dunderdsc/get.html)
# - [`__getattribute__`]()
# - [`__globals__`](https://javier.gr/blog/2014/04/python-patching-function-globals/)
# - [`__gt__`](https://blog.finxter.com/python-__gt__-magic-method/)
# - [`__hash__` #1](https://hynek.me/articles/hashes-and-equality/)
# - [`__hash__` #2](https://stackoverflow.com/questions/2909106/whats-a-correct-and-good-way-to-implement-hash)
# - [`__init_subclass__`](https://stackoverflow.com/questions/45400284/understanding-init-subclass)
# - [`__module__`](http://www.stephaniehicks.com/learnPython/pages/modules.html)
# - [`__new__`](https://medium.com/@taohidulii/playing-with-inheritance-in-python-73ea4f3b669e)
# - [`__qualname__`](https://www.codingem.com/qualname-in-python/)
# - [`__reduce__`](https://stackoverflow.com/questions/19855156/whats-the-exact-usage-of-reduce-in-pickler)
# - [`__reduce_ex__`](https://stackoverflow.com/questions/150284/what-is-the-difference-between-reduce-and-reduce-ex)
# - [`__repr__` & `__str__`](https://www.journaldev.com/22460/python-str-repr-functions)
# - [`__setattr__`](https://blog.finxter.com/python-__setattr__-magic-method/)
# - [`__sizeof__`](https://www.geeksforgeeks.org/difference-between-__sizeof__-and-getsizeof-method-python/)
# - [`__subclasshook__`](https://www.geeksforgeeks.org/__subclasscheck__-and-__subclasshook__-in-python/)
# 
# </font>
# </div>

# In[ ]:




