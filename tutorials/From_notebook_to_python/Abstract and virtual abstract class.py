#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Introduction" data-toc-modified-id="Introduction-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Introduction</a></span></li><li><span><a href="#What-an-abstract-class-is?" data-toc-modified-id="What-an-abstract-class-is?-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>What an abstract class is?</a></span></li><li><span><a href="#What-is-a-virtual-abstarct-class?" data-toc-modified-id="What-is-a-virtual-abstarct-class?-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>What is a virtual abstarct class?</a></span></li><li><span><a href="#Example-#1" data-toc-modified-id="Example-#1-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>Example #1</a></span></li><li><span><a href="#Example-#2" data-toc-modified-id="Example-#2-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>Example #2</a></span></li><li><span><a href="#pass-or-raise" data-toc-modified-id="pass-or-raise-6"><span class="toc-item-num">6&nbsp;&nbsp;</span><code>pass</code> or <code>raise</code></a></span></li><li><span><a href="#Conclusions" data-toc-modified-id="Conclusions-7"><span class="toc-item-num">7&nbsp;&nbsp;</span>Conclusions</a></span></li><li><span><a href="#References" data-toc-modified-id="References-8"><span class="toc-item-num">8&nbsp;&nbsp;</span>References</a></span></li><li><span><a href="#Requirements" data-toc-modified-id="Requirements-9"><span class="toc-item-num">9&nbsp;&nbsp;</span>Requirements</a></span></li></ul></div>

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
# - An abstract class does not require an `__init__` method, you don't need to add any constructor to it.
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


# <div class="alert alert-info">
# <font color=black>
# 
# - Using this decorator requires that the class’s metaclass is ABCMeta or is derived from it. 
# - A class that has a metaclass derived from ABCMeta cannot be instantiated unless all of its abstract methods and properties are overridden.
# - The following example shows this error with a concrete example.
# 
# </font>
# </div>

# In[4]:


class Rectangle_error(Shape):
    def __init__(self, x, y):
        self.l = x
        self.b = y        


# In[5]:


r = Rectangle_error(10,20)
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

# In[6]:


class Car():

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


# In[7]:


class Truck():

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

# In[8]:


class Vehicle():

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

# In[9]:


class Car(Vehicle):
    def __init(self, wheels, miles, make, model, year):
        self.wheels = wheels
        self.make = make
        self.model = model
        self.miles = miles
        self.year = year
        self.based_sale_price = 8000


class Truck(Vehicle):
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
# - **Secondly** You can still create an object from the `Vehicle` class. A vehicle should not have a `base_sale_price`, only Car or Truck do.
# - `Vehicle` should really be an abstract class.
# 
# </font>
# </div>

# In[10]:


# You can still do this
v = Vehicle(4, 0, "Honda", "Accord", 2014)
# but although we get purchaise price. does it make sense?
v.purchaise_price()


# <div class="alert alert-info">
# <font color=black>
# 
# - It makes sense to disallow `Vehicle(4, 0, "Honda", "Accord", 2014)` as we only wanted to abstract away some common data and behaviour, as we never meant for vehicles to be used directly. 
#     
# - A class that contains at list one **virtual method** is called metaclass.
# - A virtual method is one that the abstract class says **must exhist** in child classes, but does not necessarily implement something.
# 
# </font>
# </div>

# In[11]:


import abc


class Vehicle(metaclass=abc.ABCMeta):

    # These are two class attribute that depends on the type of object
    base_sale_price = 0.0
    wheels = 0

    def __init__(self, miles, make, model, year):        
        self.make = make
        self.model = model
        self.miles = miles
        self.year = year

    def sale_price(self):
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
    def vehicle_type(self):
        """
        Returns a string representing the type of vehicle this is.
        This will be defined in the derived class
        """
        pass


# In[12]:


# Now you can see how this will throw an error. This ie exactely what we wanted
v = Vehicle(0, "Honda", "Accord", 2014)


# In[13]:


class Car(Vehicle):

    wheels = 4
    based_sale_price = 8000

    def vehicle_type(self):
        """
        Returns a string representing the type of vehicle this is.
        """
        return "car"


class Truck(Vehicle):
    wheels = 6
    based_sale_price = 10000

    def vehicle_type(self):
        """
        Returns a string representing the type of vehicle this is.
        """
        return "truck"


class Motorcycle(Vehicle):
    wheels = 2
    based_sale_price = 4000

    def vehicle_type(self):
        """
        Returns a string representing the type of vehicle this is.
        """
        return "motorcycle"


# <div class="alert alert-info">
# <font color=black>
#     
# - This fits perfectly with our intuition.
# - The only two differences between a car and truck is the base sale price and the no of wheels.
# - All the other attributes are common hence they can be abstracted way and this is what we did with the abstract class `Vehicle`.
#     
# </font>
# </div>

# In[14]:


v = Car(1000, "Honda", "Accord", 2014)


# In[15]:


v.wheels


# In[16]:


v.based_sale_price


# In[17]:


v.make


# In[18]:


v.model


# In[19]:


v.vehicle_type()


# In[20]:


v.miles


# In[21]:


v.purchaise_price()


# # `pass` or `raise`
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
#     
# - If we use the decorator, do we need to use raise?
# - Let's create two abstract classes to find it out. If the error is the same, it means that the decorators is the first "guard" if our code, and thus raising there will never be used.'
# - A `NotImplementedError` will only throw an exception if actually called, if that is allowed.
# 
# </font>
# </div>

# In[49]:


import abc

class Strategy_pass(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def generate_signals(self):        
        pass
        
class Strategy_raise(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def generate_signals(self):        
        raise NotImplementedError("Should implement generate_signals()!")        


# In[50]:


class Derived(Strategy_pass):
    def generate_signals_(self):
        print("implemented")


# In[51]:


der = Derived()


# In[52]:


class Derived(Strategy_raise):
    def generate_signals_(self):
        print("implemented")


# In[53]:


der = Derived()


# <div class="alert alert-info">
# <font color=black>
#     
# - There is an alternative. Let's assume the code is big and just want to instantiate a class, run everything else but a nice warning/reminder in the method.
# - One could also do a raise `NotImplementedError()` inside the child method of an @abstractmethod-decorated base class method.
# 
# </font>
# </div>

# In[54]:


import abc

class Strategy_pass(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def generate_signals(self):        
        pass
    
    @abc.abstractmethod
    def generate_noise(self):        
        pass    


# In[57]:


class Derived(Strategy_raise):
    def generate_signals(self):
        output = 2+2
        return output
        
    def generate_noise(self):
        # raise a specific error! Used a warning to developer.
        raise NotImplementedError("Should implement generate_noise()!")


# In[58]:


dev = Derived()


# In[59]:


dev.generate_signals()


# In[60]:


dev.generate_noise()


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
# - [Jeff Knupp, Everything I know about Python](https://jeffknupp.com/blog/2017/03/27/improve-your-python-python-classes-and-object-oriented-programming/)
# - [When to use 'raise NotImplementedError'?](https://stackoverflow.com/questions/44315961/when-to-use-raise-notimplementederror)
#     
# </font>
# </div>

# # Requirements
# <hr style = "border:2px solid black" ></hr>

# In[ ]:


get_ipython().run_line_magic('load_ext', 'watermark')
get_ipython().run_line_magic('watermark', '-v -iv -m')


# In[ ]:




