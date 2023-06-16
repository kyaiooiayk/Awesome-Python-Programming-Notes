# Production-like code
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

## Tutorials
- [Code refactoring](https://github.com/kyaiooiayk/Awesome-Python-Programming-Notes/blob/main/tutorials/Production-grade%20code/Code%20refactoring.ipynb)
***

## References
- [What is code smell?](https://laszlo.substack.com/p/what-is-a-code-smell-and-what-can)
***