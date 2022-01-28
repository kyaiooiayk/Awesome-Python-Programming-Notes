- [Reference](https://realpython.com/python-testing/)

- Create folders and files like this: (Creating the __init__.py file means that the my_sum folder can be imported as a module from the parent directory)
```
project/
│
└── my_sum/
    └── __init__.py
```    
- How to run the script?
  - Option #1) python test.py 
  - Option #2) python -m unittest test
  - Option #3) python -m unittest -v test
  - Option #4) python -m unittest discover
- This will search the current directory for any files named test*.py and attempt to test them.
