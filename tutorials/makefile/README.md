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

## Makefile vs. shell script
- `make` supports (reasonably) minimal rebuilds -- i.e., you tell it what parts of your program depend on what other parts. When you update some part of the program, it only rebuilds the parts that depend on that.
- While you could do this with a shell script, it would be a lot more work (explicitly checking the last-modified dates on all the files, etc.) The only obvious alternative with a shell script is to rebuild everything every time. For tiny projects this is a perfectly reasonable approach, but for a big project a complete rebuild could easily take an hour or more
***

## Makefile syntax
- A `Makefile` file at the root of your project has a set of rules. Each rule has 3 parts: a target, a list of prerequisites, and a recipe.
- There is tab before receips, anything else will result in an error. See [this](https://stackoverflow.com/questions/23927212/makefile2-missing-separator-stop) discussion if you are having an issue with tabs. If you are working in VS use the option `Tab Size:4`. I quick way to check is by: `cat -e -t -v  Makefile`. It's show line starting by `^I` if TAB is given to that line and it end the line by `$`.
```shell
target: pre-req1 pre-req2 ...
    recepies
```
- The *target** represents a goal that you want to achieve, usually this is a file that needs to be created in your build. The **prerequisites** list tells make which files are this target dependent on. The prerequisites can be a file or another target. The **recipes** are a list of shell commands that will be executed by make as part of building the target.
***

## Makefile example
- [Yelp `data_pipeline` Makefile](https://github.com/Yelp/data_pipeline/blob/master/Makefile)
***

## References
- [Creating a Python Makefile](https://earthly.dev/blog/python-makefile/)
- [Makefiles for Python and beyond](https://medium.com/aigent/makefiles-for-python-and-beyond-5cf28349bf05)
- [Why use make over a shell script?](https://stackoverflow.com/questions/3798562/why-use-make-over-a-shell-script)
***
