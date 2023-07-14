# Freezing your Python code
***

## What is freezing?
- The benefit to the user is that your program will work out of the box with the intended version of Python. 
- For example, you can package your program up as a .exe for Windows or .app for macOS that includes both your program and all its code, as well as the Python runtime and relevant standard libraries required to execute it.
- It allows your program to run without the end user having to install anything else, such as Python.
- A downside is that the application will be much larger, e.g. megabytes, and required updates to the program or the included Python runtime will require an update of the entire package.
***

## Tools
- [freeze](https://wiki.python.org/moin/Freeze) Python-native tool to freeze Python scripts.
- [py2exe](https://www.py2exe.org/): py2exe is a Python Distutils extension which converts Python scripts into executable Windows programs, able to run without requiring a Python installation.Spice.
- [PyInstaller](https://pyinstaller.org/en/stable/): PyInstaller bundles a Python application and all its dependencies into a single package. The user can run the packaged app without installing a Python interpreter or any modules.
- [cx_Freeze](https://cx-freeze.readthedocs.io/en/stable/): cx_Freeze creates standalone executables from Python scripts, with the same performance, is cross-platform and should work on any platform that Python itself works on.
***


## References
- [](https://superfastpython.com/multiprocessing-freeze-support-in-python/#What_is_Freezing_Code)
***