#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Introduction" data-toc-modified-id="Introduction-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Introduction</a></span></li><li><span><a href="#Technical-aspects-of-OOP" data-toc-modified-id="Technical-aspects-of-OOP-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Technical aspects of OOP</a></span></li><li><span><a href="#What-is-inheritance?" data-toc-modified-id="What-is-inheritance?-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>What is inheritance?</a></span></li><li><span><a href="#super()-and-__mro__" data-toc-modified-id="super()-and-__mro__-4"><span class="toc-item-num">4&nbsp;&nbsp;</span><code>super()</code> and <code>__mro__</code></a></span></li><li><span><a href="#C3-class-resolution-vs.-MRO" data-toc-modified-id="C3-class-resolution-vs.-MRO-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>C3 class resolution vs. MRO</a></span></li><li><span><a href="#Example-#0" data-toc-modified-id="Example-#0-6"><span class="toc-item-num">6&nbsp;&nbsp;</span>Example #0</a></span></li><li><span><a href="#Example-#1" data-toc-modified-id="Example-#1-7"><span class="toc-item-num">7&nbsp;&nbsp;</span>Example #1</a></span></li><li><span><a href="#Example-#2" data-toc-modified-id="Example-#2-8"><span class="toc-item-num">8&nbsp;&nbsp;</span>Example #2</a></span></li><li><span><a href="#Example-#3" data-toc-modified-id="Example-#3-9"><span class="toc-item-num">9&nbsp;&nbsp;</span>Example #3</a></span></li><li><span><a href="#Example-#4" data-toc-modified-id="Example-#4-10"><span class="toc-item-num">10&nbsp;&nbsp;</span>Example #4</a></span></li><li><span><a href="#Example-#5" data-toc-modified-id="Example-#5-11"><span class="toc-item-num">11&nbsp;&nbsp;</span>Example #5</a></span></li><li><span><a href="#Example-#6" data-toc-modified-id="Example-#6-12"><span class="toc-item-num">12&nbsp;&nbsp;</span>Example #6</a></span></li><li><span><a href="#Example-#7" data-toc-modified-id="Example-#7-13"><span class="toc-item-num">13&nbsp;&nbsp;</span>Example #7</a></span></li><li><span><a href="#Example-#8" data-toc-modified-id="Example-#8-14"><span class="toc-item-num">14&nbsp;&nbsp;</span>Example #8</a></span></li><li><span><a href="#Example-#9" data-toc-modified-id="Example-#9-15"><span class="toc-item-num">15&nbsp;&nbsp;</span>Example #9</a></span></li><li><span><a href="#Example-#10" data-toc-modified-id="Example-#10-16"><span class="toc-item-num">16&nbsp;&nbsp;</span>Example #10</a></span></li><li><span><a href="#Example-#11" data-toc-modified-id="Example-#11-17"><span class="toc-item-num">17&nbsp;&nbsp;</span>Example #11</a></span></li><li><span><a href="#Inheritance-of-object-attributes" data-toc-modified-id="Inheritance-of-object-attributes-18"><span class="toc-item-num">18&nbsp;&nbsp;</span>Inheritance of object attributes</a></span></li><li><span><a href="#Instantiating-a-base-class-in-multiple-inheritance" data-toc-modified-id="Instantiating-a-base-class-in-multiple-inheritance-19"><span class="toc-item-num">19&nbsp;&nbsp;</span>Instantiating a base class in multiple inheritance</a></span></li><li><span><a href="#References" data-toc-modified-id="References-20"><span class="toc-item-num">20&nbsp;&nbsp;</span>References</a></span></li></ul></div>

# # Introduction
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-warning">
# <font color=black>
#
# **What?** Inheritance in all its flavours
#
# </font>
# </div>

# # Technical aspects of OOP
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
#
# - [ ] **Abstraction**: the use of attributes and methods allows building abstract, flexible models of objects, with a focus on what is relevant and neglecting what is not needed.
# - [ ] **Modularity** implies the possibility of breaking code down into multiple modules which are then linked to form the complete codebase.
# - [x] **Inheritance** refers to the concept that one class can inherit attributes and meth‐ ods from another class.
# - [ ] **Aggregation** refers to the case in which an object is at least partly made up of multiple other objects that might exist independently.
# - [ ] **Composition** is similar to aggregation, but here the single objects cannot exist independently of each other.
# - [ ] **Polymorphism** can take on multiple forms. Of particular importance in a Python context is what is called duck typing. This refers to the fact that standard operations can be implemented on many different classes and their instances without knowing exactly what object one is dealing with.
# - [ ] **Encapsulation** refers to the approach of making data within a class accessible only via public methods. This approach might avoid unintended effects by sim‐ ply working with and possibly changing attribute values.
#
# </font>
# </div>

# # What is inheritance?
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-info">
# <font color=black>
#
# - Inheritance was invented in 1969 for Simula.
# - Inheritance allows programmers to create classes that are built upon existing classes, and this enables a class created through inheritance to inherit the attributes and methods of the parent class. This means that inheritance supports code reusability. The methods or generally speaking the software inherited by a subclass is considered to be reused in the subclass. The relationships of objects or classes through inheritance give rise to a **directed graph**.
# - The class from which a class inherits is called the parent or **superclass**. A class which inherits from a superclass is called a **subclass** or **child class**.
#
# </font>
# </div>

# # `super()` and `__mro__`
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-info">
# <font color=black>
#
# - **First tool**: everything descent from `object`
# - **Second rule**: Python computes a method resolution order (MRO) based on your class inheritance tree.
# - The MRO satisfies 3 properties:
#     - Children of a class come before their parents
#     - Left parents come before right parents
#     - A class only appears once in the MRO
# <br><br>
# - When a method is called, the first occurrence of that method in the MRO is the one that is called.
# - Any class that doesn't implement that method is skipped. Any call to super within that method will call the next occurrence of that method in the MRO.
# - Consequently, it matters both what order you place classes in inheritance, **AND** where you put the calls to super in the methods.
# <br><br>
# - **Cons**: It can be argued that using `super` here makes the code less explicit. Making code less explicit violates The Zen of Python, which states, "Explicit is better than implicit."
# - **Pros**: There is a maintainability argument that can be made for `super` even in single inheritance. If for whatever reason your child class changes its inheritance pattern (i.e., parent class changes or there's a shift to multiple inheritance) then there's no need find and replace all the lingering references to `ParentClass.method_name()`; the use of `super` will allow all the changes to flow through with the change in the class statement.
#
# </font>
# </div>

# # C3 class resolution vs. MRO
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-info">
# <font color=black>
#
# - If we are dealing with multiple inheritance, according to the C3 class resolution algorithm, the following applies.
# - **Aassuming that child class C inherits from two parent classes A and B, "class A should be checked before class B"**.
# - Method Resolution Order (MRO) is a order in which methods should be inherited in the case of multiple iheritance. C3 linearization algorithm is how MRO works under the hood.
#
# </font>
# </div>

# In[2]:


class A:
    def foo(self):
        print("class A")


class B:
    def foo(self):
        print("class B")


class C(A, B):
    pass


# Will print what? A or B?
C().foo()


# In[3]:


class A(object):
    def foo(self):
        print("class A")


class B(A):
    pass


class C(A):
    def foo(self):
        print("class C")


class D(B, C):
    pass


# Will print what? A, B or C?
D().foo()


# # Example #0
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-info">
# <font color=black>
#
# - In its simplest form inheritance establishes a relationship btw two classes: a parent and a child.
# - A child class:
#     - keeps the attributes and methods of its parent
#     - Add new attributes or methods of its own
#     - Overrides the existig methods of its parent
#
# </font>
# </div>

# ![image.png](attachment:image.png)

# # Example #1
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-info">
# <font color=black>
#
# - Accessing parent class object attribues from child class.
#
# </font>
# </div>

# In[1]:


class Parent:
    def __init__(self):
        self.ParentObjectAttribute = 1


class Child(Parent):
    def __init__(self):
        self.ChildObjectAttribute = 2
        Parent.__init__(self)

        # here you can access myvar like below.
        print("Calling from inside __init__", self.ParentObjectAttribute)


# In[2]:


child = Child()
print(child.ChildObjectAttribute)
print(child.ParentObjectAttribute)


# In[3]:


class Parent:
    def __init__(self):
        self.ParentObjectAttribute = 1


class Child(Parent):
    def __init__(self):
        self.ChildObjectAttribute = 2
        super().__init__()

        # here you can access myvar like below.
        print("Calling from inside __init__", self.ParentObjectAttribute)


child = Child()
print(child.ChildObjectAttribute)
print(child.ParentObjectAttribute)


# # Example #2
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-info">
# <font color=black>
#
# - There is also a way to directly call each inherited class.
#
# </font>
# </div>

# In[4]:


class Parent1:
    def __init__(self):
        self.Parent1ObjectAttribute = 1


class Parent2:
    def __init__(self):
        self.Parent2ObjectAttribute = 2


class Child(Parent1, Parent2):
    def __init__(self):
        self.ChildObjectAttribute = 3
        Parent2.__init__(self)
        Parent1.__init__(self)

        print("Calling from __init__")
        print(self.ChildObjectAttribute)
        print(self.Parent1ObjectAttribute)
        print(self.Parent2ObjectAttribute)


child = Child()
print("Calling from object")
print(child.ChildObjectAttribute)
print(child.Parent1ObjectAttribute)
print(child.Parent2ObjectAttribute)


# In[5]:


Child.__mro__


# In[6]:


child.__dict__


# <div class="alert alert-info">
# <font color=black>
#
# - Super is **about** following the chain of inheritance, not getting to a specific class's method.
# - Multiple inheritance is the **ONLY** case where super() is of any use.
# - I would not recommend using it with classes using linear inheritance, where it's just **useless** overhead.
# - But this argument can be challenged and you'll find many developer not using it.s
#
# </font>
# </div>

# In[7]:


"""
Can we achieve the same with super()?
"""


class Parent1:
    def __init__(self):
        print("calling Parent1")
        super(Parent1, self).__init__()
        self.Parent1ObjectAttribute = 1


class Parent2:
    def __init__(self):
        print("calling Parent2")
        super(Parent2, self).__init__()
        self.Parent2ObjectAttribute = 2


class Child(Parent1, Parent2):
    def __init__(self):
        super(Child, self).__init__()
        self.ChildObjectAttribute = 3

        print("Calling from __init__")
        print(self.ChildObjectAttribute)
        print(self.Parent1ObjectAttribute)
        print(self.Parent2ObjectAttribute)


child = Child()
print("Calling from object")
print(child.ChildObjectAttribute)
print(child.Parent1ObjectAttribute)
print(child.Parent2ObjectAttribute)


# In[8]:


child.__dict__


# In[9]:


Child.__mro__


# # Example #3
# <hr style="border:2px solid black"> </hr>

# In[10]:


class Parent:
    def __init__(self):
        super(Parent, self).__init__()
        print("parent")


class Left(Parent):
    def __init__(self):
        super(Left, self).__init__()
        print("left")


class Right(Parent):
    def __init__(self):
        super(Right, self).__init__()
        print("right")


class Child(Left, Right):
    def __init__(self):
        super(Child, self).__init__()
        print("child")


# In[11]:


Child()


# In[12]:


"""
With super last in each method.
So it impportant where this is placed under 
__init__
"""


class Parent:
    def __init__(self):
        print("parent")
        super(Parent, self).__init__()


class Left(Parent):
    def __init__(self):
        print("left")
        super(Left, self).__init__()


class Right(Parent):
    def __init__(self):
        print("right")
        super(Right, self).__init__()


class Child(Left, Right):
    def __init__(self):
        print("child")
        super(Child, self).__init__()


# In[13]:


Child()


# In[14]:


Child.__mro__


# In[15]:


class Parent:
    def __init__(self):
        super(Parent, self).__init__()


class Left(Parent):
    def __init__(self):
        super(Left, self).__init__()


class Right(Parent):
    def __init__(self):
        super(Right, self).__init__()
        print("rigt")


class Child(Left, Right):
    def __init__(self):
        super(Child, self).__init__()


# In[16]:


Child.__mro__


# # Example #4
# <hr style="border:2px solid black"> </hr>

# In[17]:


class Person:
    """
    Base class or parent class
    """

    def __init__(self, name):
        """
        Constructor
        """
        self.name = name

    def get_name(self):
        return self.name


class Employee(Person):
    """
    Derived class or subclass
    that uses the base class constructor
    """

    def is_employee_pythonist(self):
        if any([i.lower() == "pythonista" for i in self.name.split(" ")]):
            return True
        else:
            return False


# In[18]:


"""
Let's start with object creation/instantiation
for the base clas
"""
person = Person("Pythonista")
print(person.get_name())


# In[19]:


"""
Let's create an object from the children class.
Pay attention that this particular case uses the
base class constructor
"""
employee = Employee("Employee Pythonista")
print(employee.get_name())
print(employee.is_employee_pythonist())


# # Example #5
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-info">
# <font color=black>
#
# - Inheritance is **transitive** in nature.
# - This means that if class B inherits from another class A, then all the subclasses of B would automatically inherit from class A.
#
# </font>
# </div>

# In[20]:


class A:
    def method_from_class_a(self):
        print("Hi from class A")


class B(A):
    def method_from_class_b(self):
        print("Hi from class B")


class C(B):
    def method_from_class_c(self):
        print("Hi from class C")


# In[21]:


c = C()
c.method_from_class_c()
c.method_from_class_b()
c.method_from_class_a()


# # Example #6
# <hr style="border:2px solid black"> </hr>

# In[22]:


class A:
    def speak(self):
        print("class A speaking")


class B:
    def scream(self):
        print("class B screaming")


class C(A, B):
    pass


# In[23]:


c = C()
c.speak()
c.scream()


# # Example #7
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-info">
# <font color=black>
#
# - For a class hierarchy, Python needs to determine which class to use when attempting to access an attribute by name. To do this, Python considers the ordering of base classes.
#
# </font>
# </div>

# In[24]:


class A:
    def speak(self):
        print("class A speaking")


class B:
    def speak(self):
        print("class B speaking")


class C(A, B):
    pass


c = C()
c.speak()


# In[25]:


class A:
    def speak(self):
        print("class A speaking")


class B:
    def speak(self):
        print("class B speaking")


class C(B, A):
    pass


c = C()
c.speak()


# In[26]:


class A:
    def speak(self):
        print("class A speaking")


class B:
    def speak(self):
        print("class B speaking")


class C(B, A):
    """
    Speak method of class C will override previous speak methods.
    """

    def speak(self):
        print("class C speaking")


c = C()
c.speak()


# # Example #8
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-info">
# <font color=black>
#
# - Sometimes we need to call methods of parent class to a overridden method of child class.
# - We can achieve this using super function.We can directly use methods of super class or modify them(this is very common).
#
# </font>
# </div>

# In[27]:


class A:
    def test(self):
        return "A"


class B(A):
    # override test method
    def test(self):
        # access method of parent class to overridden child class
        return "B" + super().test()


print(B().test())


# <div class="alert alert-info">
# <font color=black>
#
# - There is another **equivalent way** of achieving what we did above
# - Python 3 encourages using `super()`, instead of using `super(className, self)`, both have the same effect.
# - Python 2, only supports the super(className,self) syntax. Since, Python 2 is widely used so Python 3 also has support for this type of super calling.
#
# </font>
# </div>

# In[28]:


class B(A):
    def test(self):
        return "B" + super(B, self).test()
        # super(className,object)


# In[29]:


print(B().test())


# # Example #9
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-info">
# <font color=black>
#
# - Python supports different types of inheritance so sometimes it needs to be introspected cleanly.
# - `isinstance()` takes two arguments: an object and a class and returns `True` if the given class is anywhere in the inheritance chain of the object’s class.
#
# </font>
# </div>

# In[30]:


class A:
    def test(self):
        return "A"


class B(A):
    def test(self):
        return "B" + super(B, self).test()


print(isinstance(A(), A))
print(isinstance(B(), A))


# In[31]:


print(issubclass(A, A))
print(issubclass(B, A))
print(issubclass(A, B))
print(issubclass(B, B))


# <div class="alert alert-info">
# <font color=black>
#
# - Is there anything that can help us sout in understanding this?
# - `__bases__()` provides a tuple of immediate base classes of a class.
#
# </font>
# </div>

# In[32]:


print(A.__bases__)
print(B.__bases__)


# <div class="alert alert-info">
# <font color=black>
#
# - **By default**, every Python class is the subclass of built-in object class.
# - `__subclasses__()`returns a list of all
#     the subclasses a class.
# - As per the case where we ued `__bases__()`, `__subclasses__` only goes **one level deep** from the class we’re working on.
#
# </font>
# </div>

# In[33]:


print(A.__subclasses__())
print(B.__subclasses__())


# # Example #10
# <hr style="border:2px solid black"> </hr>

# In[34]:


class Parent:
    def __init__(self):
        self.parent_attribute = "I am a parent"

    def parent_method(self):
        print("Back in my day...")


class Child(Parent):
    """
    A child class that inherits from Parent
    """

    def __init__(self):
        Parent.__init__(self)
        self.child_attribute = "I am a child"


# Create an instance of child
child = Child()

# Show attributes and methods of child class
print(child.child_attribute)
print(child.parent_attribute)
child.parent_method()


# # Example #11
# <hr style = "border:2px solid black" ></hr>

# In[2]:


class Dog_v2:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"


# In[3]:


class JackRussellTerrier(Dog_v2):
    pass


class Dachshund(Dog_v2):
    pass


class Bulldog(Dog_v2):
    pass


# In[4]:


miles = JackRussellTerrier("Miles", 4)
buddy = Dachshund("Buddy", 9)
jack = Bulldog("Jack", 3)
jim = Bulldog("Jim", 5)


# In[5]:


jim.speak("Woof")


# <div class="alert alert-block alert-info">
# <font color=black>
#
# - To determine which class a given object belongs to, you can use the built-in `type()`
#
# </font>
# </div>

# In[6]:


type(jim)


# <div class="alert alert-block alert-info">
# <font color=black>
#
# - What if you want to determine if jim is an instance of the Dog_v2 class? You can do this with the built-in isinstance()?
# - `isinstance()` takes two arguments, an object and a class.
#
# </font>
# </div>

# In[7]:


isinstance(jim, Dog_v2)


# In[8]:


isinstance(jim, Bulldog)


# <div class="alert alert-block alert-info">
# <font color=black>
#
# - To override a method defined on the parent class, you define a method with the same name on the child class.
#
# </font>
# </div>

# In[9]:


# Before we have
jim.speak("Woof")


# In[10]:


class Bulldog(Dog_v2):
    def speak(self, sound="Arf"):
        return f"{self.name} says {sound}"


# In[11]:


# Before we have
jim = Bulldog("Jim", 5)
jim.speak()


# # Inheritance of object attributes
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
#
# - Let say we want to do multiple base class inheritance.
# - Each base class has methods and object attributes (not clas attributes). Object attributes are those related to the object, in shorts those inside the `__init__` construct.
# - We'd like to use the `.` dot notation and have access to the base classes object attributes.
# - To achieve this you need have `super.__init__()` in each base class otherwise the second base class object attributes would not be inheritated.
# - ** This is becase** calling `super().__init__()` calls `__init__` calls only the first base `__init__` method.
#
# </font>
# </div>

# In[35]:


class BASEA:
    def __init__(self, a=1):
        self.a = a
        super().__init__(self.a)

    def return_a(self, a):
        return a


# In[36]:


class BASEB:
    def __init__(self, b=1):
        self.b = b

    def return_b(self, b):
        return b


# In[37]:


class C(BASEA, BASEB):
    def __init__(self, c=1):
        self.c = c
        super().__init__(self.c)

    def return_c(self, c):
        return c


# In[38]:


# instantiate derived class C
c = C(2)


# In[39]:


# check which method are available
dir(c)


# In[40]:


c.__dict__


# <div class="alert alert-info">
# <font color=black>
#
# - If you forget to ass `super.__init__()` under the first base class `__init__` you will nto inheritate the second base class object attributes.
# - Here is an example.
#
# </font>
# </div>

# In[41]:


class BASEA:
    def __init__(self, a=1):
        self.a = a
        # super().__init__()

    def return_a(self, a):
        return a


# In[42]:


class BASEB:
    def __init__(self, b=1):
        self.b = b

    def return_b(self, b):
        return b


# In[43]:


class C(BASEA, BASEB):
    def __init__(self, c=1):
        self.c = c
        super().__init__()

    def return_c(self, c):
        return c


# In[44]:


b = BASEB(b=1)


# In[45]:


c = C(1)


# In[46]:


# As you can see object attribute b is NOT listed!
c.__dict__.keys()


# # Instantiating a base class in multiple inheritance
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
#
# - The case is similar to the case above, but an error is thrown if we try to instatiate one of the base class.
# - We'll first replicate the problem and then, we'll suggestion a solution.
#
# </font>
# </div>

# In[47]:


class BASEA:
    def __init__(self, a=1):
        self.a = a
        super(self).__init__(self.a)

    def return_a(self, a):
        return a


# In[48]:


class BASEB:
    def __init__(self, b=1):
        self.b = b

    def return_b(self, b):
        return b


# In[49]:


class C(BASEA, BASEB):
    def __init__(self, c=1):
        self.c = c
        super().__init__(self.c)

    def return_c(self, c):
        return c


# In[50]:


# Replicating the error
A = BASEA(1)


# In[51]:


class BASEA:
    def __init__(self, a=1):
        self.a = a
        # super(self).__init__(self.a)

    def return_a(self, a):
        return a


# In[52]:


class C(BASEA, BASEB):
    def __init__(self, c=1):
        self.c = c
        # super().__init__(self.c)
        BASEA.__init__(self, self.c)
        BASEB.__init__(self, self.c)

    def return_c(self, c):
        return c


# In[53]:


#  The issue is solved
A = BASEA(1)


# # References
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-warning">
# <font color=black>
#
# - https://stackoverflow.com/questions/10909032/access-parent-class-instance-attribute-from-child-class-instance
# - https://stackoverflow.com/questions/3277367/how-does-pythons-super-work-with-multiple-inheritance
# - https://www.datacamp.com/community/tutorials/super-multiple-inheritance-diamond-problem
# - https://medium.com/@taohidulii/playing-with-inheritance-in-python-73ea4f3b669e
# - https://stackoverflow.com/questions/52959041/multiple-inheritance-the-derived-class-gets-attributes-from-one-base-class-only
# - https://stackoverflow.com/questions/9575409/calling-parent-class-init-with-multiple-inheritance-whats-the-right-way
# - https://www.python-course.eu/python3_inheritance.php
# - http://python-history.blogspot.ru/2010/06/method-resolution-order.html
# - http://gistroll.com/rolls/21/horizontal_assessments/new](http://gistroll.com/rolls/21/horizontal_assessments/new
# - https://nbviewer.org/github/rasbt/python_reference/blob/master/tutorials/not_so_obvious_python_stuff.ipynb?create=1
# - https://blog.pilosus.org/posts/2019/05/02/python-mro/
#
# </font>
# </div>

# In[ ]:
