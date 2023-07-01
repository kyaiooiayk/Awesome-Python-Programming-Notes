#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Introduction" data-toc-modified-id="Introduction-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Introduction</a></span></li><li><span><a href="#What-an-abstract-class-is?" data-toc-modified-id="What-an-abstract-class-is?-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>What an abstract class is?</a></span></li><li><span><a href="#What-is-a-virtual-abstarct-class?" data-toc-modified-id="What-is-a-virtual-abstarct-class?-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>What is a virtual abstarct class?</a></span></li><li><span><a href="#Example-#1" data-toc-modified-id="Example-#1-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>Example #1</a></span></li><li><span><a href="#Example-#2" data-toc-modified-id="Example-#2-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>Example #2</a></span></li><li><span><a href="#Conclusions" data-toc-modified-id="Conclusions-6"><span class="toc-item-num">6&nbsp;&nbsp;</span>Conclusions</a></span></li><li><span><a href="#References" data-toc-modified-id="References-7"><span class="toc-item-num">7&nbsp;&nbsp;</span>References</a></span></li></ul></div>

# # Introduction
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-warning">
# <font color=black>
# 
# **What?** Abstract and virtual abstarct class
# 
# </font>
# </div>

# # What an abstract class is?
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
# 
# - A class is called an **abstract class** if it contains some abstract methods.
# - An **abstract method** is a method that is declared, but contains no implementation. 
# - Abstract classes may not be instantiated, and its abstract methods must be implemented by its subclasses.
# - **When are they used?** Abstract base classes provide a way to define **interfaces** when other techniques like `hasattr()` would be clumsy or subtly wrong
# 
# </font>
# </div>

# # What is a virtual abstarct class?
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
# 
# - It is everything that a normal abstract class is but it contains at least one virtual method. 
# 
# </font>
# </div>

# # Example #1
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
# 
# - The abc module defines ABCMeta class which is a metaclass for defining abstract base class. Following example defines Shape class as an abstract base class using ABCMeta. 
# - The shape class has `area()` method decorated by abstractmethod.
# - A Rectangle class now uses above Shape class as its parent and implementing the abstract `area()` method. Since it is a concrete class, it can be instantiated and an implemented `area()` method can be called. 
# 
# </font>
# </div>

# In[1]:


import abc


class Shape(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def area(self):
        pass


# In[2]:


class Rectangle(Shape):
    def __init__(self, x, y):
        self.l = x
        self.b = y

    def area(self):
        return self.l*self.b


# In[3]:


r = Rectangle(10,20)
print ('area: ', r.area())


# # Example #2
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
# 
# - Let us say we run a dealeship and trade car, truck and motorcycles. If we want to create a sale system how would it look like?
# - We'll create the final model in following these steps:
#     - Create separate classes.
#     - Simplify them via inheritance using an abstarct class.
# 
# </font>
# </div>

# In[4]:


class Car(object):

    def __init__(self, wheels, miles, make, model, year):
        self.wheels = wheels
        self.make = make
        self.model = model
        self.miles = miles
        self.year = year

    def sale_price():
        """
        We charge a flat rate of 5k per wheels
        """
        return 5000.0 * sel.wheels

    def purchaise_price(self):
        """
        We buy back according to the miles the car has
        """
        return 8000.0 - (.1 * self.miles)


# In[5]:


class Truck(object):

    def __init__(self, wheels, miles, make, model, year):
        self.wheels = wheels
        self.make = make
        self.model = model
        self.miles = miles
        self.year = year

    def sale_price():
        """
        We charge a flat rate of 5k per wheels
        """
        return 5000.0 * sel.wheels

    def purchaise_price(self):
        """
        We buy back according to the miles the car has
        """
        return 10000.0 - (.1 * self.miles)


# <div class="alert alert-info">
# <font color=black>
# 
# - We create two class, but we ended up repeating a lot of code?
# - **How can we improve it?** First of all we can look for abstraction material! This means to look for something that is in common and try ti abstarct this away.
# -  This can be done by noticing that cars and trucks can be considerd as a vehicles. All vechicles have something in common and this can be used to create a more abstract class.
# 
# </font>
# </div>

# In[6]:


class Vehicle(object):

    base_sale_price = 0.0

    def __init__(self, wheels, miles, make, model, year):
        self.wheels = wheels
        self.make = make
        self.model = model
        self.miles = miles
        self.year = year

    def sale_price():
        """
        We charge a flat rate of 5k per wheels
        """
        return 5000.0 * sel.wheels

    def purchaise_price(self):
        """
        We buy back according to the miles the car has
        """
        return self.base_sale_price - (.1 * self.miles)


# <div class="alert alert-info">
# <font color=black>
# 
# - Look how we have created a class attribute `base_sale_price` to help us distinguish a car from a truck.
# - Writing `Car(Vehicle)` mean we are creating a class that inherits from the inherited class `Vehicle`.
# 
# </font>
# </div>

# In[7]:


class Car(Vehicle):
    def __init(self, wheels, miles, make, model, year):
        self.wheels = wheels
        self.make = make
        self.model = model
        self.miles = miles
        self.year = year
        self.based_sale_price = 8000


class Car(Vehicle):
    def __init(self, wheels, miles, make, model, year):
        self.wheels = wheels
        self.make = make
        self.model = model
        self.miles = miles
        self.year = year
        self.based_sale_price = 10000


# <div class="alert alert-info">
# <font color=black>
# 
# - We've cleaned up a bit the code but there are still two things that are not as polished as we'd like them to be.
# - **Frist** There is still some repeated code.
# - **Secondly** You can still create an obkect fromfrom the `Vehicle` class. A vechicle should not have a `base_sale_price`, only Car or Truck do.
# - `Vehicle` should really be an abstarct class.
# 
# </font>
# </div>

# In[8]:


# You can still do this
v = Vehicle(4, 0, "Honda", "Accord", 2014)
# but although we get purchaise price. does it make sense?
v.purchaise_price()


# <div class="alert alert-info">
# <font color=black>
# 
# - It makes sense to disallow `Vehicle(4, 0, "Honda", "Accord", 2014)` as we only wanted to abstract away some common data and behaviour.
# - A class that contains at list one **virtual method** is called metaclass.
# - A virtual method is one that the abstract class says must exhist in child classes, but does not necessarily implement something.
# 
# </font>
# </div>

# In[11]:


import abc


class Vehicle(metaclass=abc.ABCMeta):

    # These are two class attribute that depends on the type of object
    base_sale_price = 0.0
    wheels = 0

    def __init__(self, wheels, miles, make, model, year):
        self.wheels = wheels
        self.make = make
        self.model = model
        self.miles = miles
        self.year = year

    def sale_price():
        """
        We charge a flat rate of 5k per wheels
        """
        return 5000.0 * sel.wheels

    def purchaise_price(self):
        """
        We buy back according to the miles the car has
        """
        return self.base_sale_price - (.1 * self.miles)

    @abc.abstractmethod
    def vehicle_type():
        """
        Returns a string representing the type of vehicle this is.
        This will be defined in the derived class
        """
        pass


# In[12]:


# Now you can see how this will throw an error. This ie exactely what we wanted
v = Vehicle(4, 0, "Honda", "Accord", 2014)


# In[13]:


class Car(Vehicle):
    def __init__(self):
        wheels = 4
        based_sale_price = 8000

    def vehicle_type():
        """
        Returns a string representing the type of vehicle this is.
        """
        return "car"


class Truck(Vehicle):
    def __init__(self, wheels, miles, make, model, year):
        wheels = 6
        based_sale_price = 10000

    def vehicle_type():
        """
        Returns a string representing the type of vehicle this is.
        """
        return "truck"


class Motorcycle(Vehicle):
    def __init__(self, wheels, miles, make, model, year):
        wheels = 2
        based_sale_price = 4000

    def vehicle_type():
        """
        Returns a string representing the type of vehicle this is.
        """
        return "motorcycle"


# # Conclusions
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-danger">
# <font color=black>
# 
# - Remember that getting rid of duplicates is a side effect of inheritance.
# - When using inheritance, what we are really doing is providing the proper level of **abstraction**. 
# - Abstract class is **different** from virtual abstract class.
# 
# </font>
# </div>

# # References
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-warning">
# <font color=black>
# 
# - https://www.tutorialspoint.com/abstract-base-classes-in-python-abc
# - Jeff Knupp, Everything I know about Python. No longer available online.
# 
# </font>
# </div>

# In[ ]:




