# Production-like code
***

## General advice
- Wrap your hard decisions into a class.
- Keep the code (the class) separate from the calls (`main()`)
***

## Code smell
- Code smell are certain structures in the code that indicate a violation of fundamental design principles and negatively impact design quality” and also.
-  Code smells are an indicator of factors that contribute to technical debt.
- Code smells are not code bugs.
***

## 5 most common code smells
- **Bloaters**: code elements that shouldn’t be as big as they are now. Three code smells in this category are Long Method, Large Class, Long Parameter List, Primitive Obsession and Data Clumps.
- **Object-Orientation Abusers**:
- **Change Preventers**: a single change triggers changes in multiple places. This is a sign of coupling.
- **Dispensables**: are something that add no value to the solution: Duplicate Code, Dead Code, Comments. *Comments are probably the most controversial one here*. The strongest argument for removing comment is the fact they are not tested therefoe they can diverge from actual behaviour and cause more problems than benefits.
- **Couplers**: these are usually coupled classes for reasons that can be avoided. Two typical ones are Feature Envy and Inappropriate Intimacy. 
***

## Documentations
- Documentation should not be a chore.
- Documentation should be a lightweight, high ROI activity, and a productivity tool.
- Your code should document itself. 
- Keep in mind that documentation cannot be tested and the same goes for comments!
- You need to write readable code rather than readable documentation. 
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

## Thin slice (not thin-slicing!)
- In software developement, for a given feature, we can come up with **multiple thin-slices** which can be incrementally (sequentially) built. Thin Slice is the simplest possible functional, usable, end to end slice of functionality.
***

## Slow-changing dimensions
- A slowly changing dimension (SCD) in data management and data warehousing is a dimension which contains relatively static data which can change slowly but unpredictably, rather than according to a regular schedule.
- Some examples of typical slowly changing dimensions are entities such as names of geographical locations, customers, or products.
***

## Tutorials
- [Code refactoring](https://github.com/kyaiooiayk/Awesome-Python-Programming-Notes/blob/main/tutorials/Production-grade%20code/Code%20refactoring.ipynb)
- [Step-by-step tutorial on how to refactor your code for production](https://github.com/xLaszlo/CQ4DS-notebook-sklearn-refactoring-exercise/tree/master)
***

## Blogs
- [Deliberate Machine Learning](https://laszlo.substack.com)
***

## References
- [What is code smell?](https://laszlo.substack.com/p/what-is-a-code-smell-and-what-can)
- [Refactoring for Data Scientists: How to maintain readability in a single method?](https://laszlo.substack.com/p/refactoring-for-data-scientists-how)
- [Simple trick to optimise code and maintain readability in a compute heavy application](https://laszlo.substack.com/p/simple-trick-to-optimise-code-and)
- [Documentation vs Documentation in Data Science](https://laszlo.substack.com/p/documentation-vs-documentation-in)
- [Can you version control Jupyter notebooks?](https://laszlo.substack.com/p/can-you-version-control-jupyter-notebooks)
- [Slow-changing dimensions](https://en.wikipedia.org/wiki/Slowly_changing_dimension)
***