# Types of Design Patterns
***

## Design pattern vs. architectural pattern
- **Patterns** are distilled commonality that you find in programs. It allows us to deconstruct a large complex structure and build using simple parts. It provides a general solution for a class of problems. Think of them as template which by their very nature are general and then need to be made specific depending on your case.
- **Design patterns** are usually associated with code level commonalities. It provides various schemes for refining and building smaller subsystems. It is usually influenced by programming language. Some patterns pale into insignificance due to language paradigms. Design patterns are medium-scale tactics that flesh out some of the structure and behavior of entities and their relationships.
- **Architectural patterns** are seen as commonality at higher level than design patterns. Architectural patterns are high-level strategies that concerns large-scale components, the global properties and mechanisms of a system. Application's architecture is the overall 'organization' of the code. The architecture typically needs to be decided up front and often is difficult to change once the application is built.
- **The bottom line?** Architectural elements tend towards collections of classes or modules, generally represented as boxes. Diagrams about architecture represent the loftiest level looking down, whereas class diagrams are at the most atomic level.

## Desing patterns and OOP
- Design patterns require the use of OOP.
- thus, design patterns are almost irrelevant to non-OPP programming such as C.
***

## Three types of design patterns
- **Creational Design Patterns**
  - We use creational design patterns to build objects systematically.
  - The main benefit of creational patterns is their flexibility.
  - For example differnt types of objects from the same class can be created at runtime using creational patterns.
  - In creational pattern, *Polymorphism* is often in use.
- **Structural Design Patterns**
  - We use structural patterns to establish relation between software components in particular settings.
  - The goal is to satisfy functional and nonfunctional requirements.
  - Functional requirements refer to what the software does.
  - NonFunctional requiremnets refer to how well it does its job (like how fast or slow).
  - Structual patterns take advantage of *inheritance*.
- **Behavioral Design Patterns**
  - It refers to how you make your objects interact with each other.
  - The focus here is to defining protocols between these objects when working together to achieve a common goal.
  - Beahavorial patterns mostly use *methods* and their *signatures*.
***

### Creational Design Patterns
- Factory Method | [Tutorial](https://github.com/kyaiooiayk/Python-Programming/blob/main/tutorials/Design_And_Architecture_Patterns/tutorials/Design%20Patterns%20-%20Factory%20Method.ipynb)
- Abstract Factory Method | [Tutorial](https://github.com/kyaiooiayk/Python-Programming/blob/main/tutorials/Design_And_Architecture_Patterns/tutorials/Design%20Patterns%20-%20Abstarct%20Factory%20Method.ipynb)
- Builder Method | [Tutorial](https://github.com/kyaiooiayk/Awesome-Python-Programming-Notes/blob/main/tutorials/Design_And_Architecture_Patterns/tutorials/Creational%20Design%20Patterns%20-%20Builder%20Factory%20Method.ipynb)
- Prototype Method | [Tutorial](https://github.com/kyaiooiayk/Awesome-Python-Programming-Notes/blob/main/tutorials/Design_And_Architecture_Patterns/tutorials/Creational%20Design%20Patterns%20-%20Prototype%20Method.ipynb)
- Singleton Method | [Tutorial](https://github.com/kyaiooiayk/Awesome-Python-Programming-Notes/blob/main/tutorials/Design_And_Architecture_Patterns/tutorials/Creational%20Design%20Patterns%20-%20Singleton%20Method.ipynb)
***

### Structural Design Patterns
- Adapter Method | [Tutorial](https://github.com/kyaiooiayk/Awesome-Python-Programming-Notes/blob/main/tutorials/Design_And_Architecture_Patterns/tutorials/Structural%20Design%20Patterns%20-%20Adapter%20Method.ipynb)
- Bridge Method | [Tutorial](https://github.com/kyaiooiayk/Awesome-Python-Programming-Notes/blob/main/tutorials/Design_And_Architecture_Patterns/tutorials/Structural%20Design%20Patterns%20-%20Bridge%20Method.ipynb)
- Composite Method | [Tutorial](https://github.com/kyaiooiayk/Awesome-Python-Programming-Notes/blob/main/tutorials/Design_And_Architecture_Patterns/tutorials/Structural%20Design%20Patterns%20-%20Composite%20Method.ipynb)
- Decorator Method | [Tutorial](https://github.com/kyaiooiayk/Awesome-Python-Programming-Notes/blob/main/tutorials/Design_And_Architecture_Patterns/tutorials/Structural%20Design%20Patterns%20-%20Decorator%20Method.ipynb)
- Facade Method | [Tutorial](https://github.com/kyaiooiayk/Awesome-Python-Programming-Notes/blob/main/tutorials/Design_And_Architecture_Patterns/tutorials/Structural%20Design%20Patterns%20-%20Facade%20Method.ipynb)
- Proxy Method
- FlyWeight Method
***

### Behavioral Design Patterns
- Chain of Responsibility Method
- Command Method
- Iterator Method
- Mediator Method
- Memento Method
- Observer Method
- State Method
- Strategy Method
- Template Method
- Visitor Method
***

## Design patterns in Data Science
- For data scientists thinking about code quality there are two main components in any DS project are *data* and *algorithms*.
There are three most relevant design patterns (there are many more) are:
    - **Factory Pattern** is used to decouple data IO, or in other words the data sources (SQL, pandas etc ..)
    - **Strategy Pattern** is used to decouple algorithms.
    - **Adapter Pattern** is used to decouple external services.
- All the above methods tackled the main problem in data science projects:coupling. It means that you need to rewrite a large part of your code each time you want to try new options, hence your code is not generally and essentially hard-coded. This can happen both while managing data and  algorithms.
- [Factory and Strategy Patters in DS](https://github.com/kyaiooiayk/Awesome-Python-Programming-Notes/blob/main/tutorials/Design_And_Architecture_Patterns/tutorials/Factory%20and%20Strategy%20Patterns%20in%20DS.ipynb)
***

## Others
- [Dependency inversion](https://github.com/kyaiooiayk/Awesome-Python-Programming-Notes/blob/main/tutorials/Design_And_Architecture_Patterns/tutorials/Dependency%20Inversion.ipynb)
***

## References
- [Python design patterns](https://www.geeksforgeeks.org/python-design-patterns/)
- [What's the difference between design patterns and architectural patterns?](https://stackoverflow.com/questions/4243187/whats-the-difference-between-design-patterns-and-architectural-patterns)
- [Software architecture design patterns](https://stackoverflow.com/questions/4192887/software-architecture-design-patterns/46419722#46419722)
- [10 Common Software Architectural Patterns in a nutshell](https://towardsdatascience.com/10-common-software-architectural-patterns-in-a-nutshell-a0b47a1e9013)
- [Types of Software Architecture Patterns](https://www.geeksforgeeks.org/types-of-software-architecture-patterns/?ref=gcse)
- [Design patterns in python](https://refactoring.guru/design-patterns/python)
- [Notes taken after the Linkedin "Python: Design Pattern" course](https://github.com/pyGuru123/Python-design-Patterns)
- [You only need 2 design patterns to improve the quality of your code in a data science project](https://laszlo.substack.com/p/you-only-need-2-design-patterns-to)
- [Machine learning is the continuation of software enginerring by other mens: PyData 2022](file:///Users/gm_main/Downloads/2942283f-12f6-4548-80c2-071d3edb08f4.pdf.pdf)
***
