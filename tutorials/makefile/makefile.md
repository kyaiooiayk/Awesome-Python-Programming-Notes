# Makefile
***

## Motivation
- Even though Python is regarded as an interpreted language and the files need not be compiled separately, many developers are unaware that you can still use make to automate different parts of developing a Python project, like running tests, cleaning builds, and installing dependencies.
***

## Is Python Compiled or Interpreted?
- Now, Python is usually considered to be an interpreted language. When you run a Python code, the Python interpreter reads the file line-by-line and runs it.
- But behind-the-scenes, the source code is compiled into bytecode. These are similar to CPU instructions, but instead of being run by the actual CPU, these are executed by a software called a Virtual Machine (VM), which acts as a pseudo-microprocessor that runs the bytecodes. The advantage is that you can run Python on any platform as long as the VM is installed.
- **The reason Python is regarded to be an interpreted language is because the compilation step is implicit**. You don’t have to invoke a compiler manually.
- When you import a module into your code, Python compiles those modules into bytecode for caching purposes. These are stored in a directory named `__pycache__` in the current directory, which contains compiled `.pyc` files.
***

## How is `make` used within Python?
- Although you cannot compile these modules using make, you can still use make for automation tasks like running tests, installing dependencies, cleaning the .pyc files etc.
***

## What is `make`
- It is a tool which controls the generation of executable and other non-source files from a program’s source file.
- It can automate the process of building software by tracking its dependencies and compiling the program only when the dependencies change.
***

## Motivation
***

## References
- [Creating a Python Makefile](https://earthly.dev/blog/python-makefile/)
- [Makefiles for Python and beyond](https://medium.com/aigent/makefiles-for-python-and-beyond-5cf28349bf05)
***
