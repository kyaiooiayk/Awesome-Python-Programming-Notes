# How to create a `requirements.txt` file
***

## Introduction
- We'd like to create a file which stores all the packages we have manually installed.
- The questions arises whether we'd like to list all the dependencies or only those packages we have manually installed.
- As always it depends, so here are listed all the options you have.
***

## Option #1
- `pip freeze -> requirements.txt`
- This will dump the current versions of **all** the installed modules on that system irrespective of there usage in the current project. That is likely to be a long list of you have not installed a single manually and you have a freshly created virtual environment. 
- Further consider that this will only list modules that have been installed via `pip`, if you have installed a packaged via `conda` this may not be there. 
***


## Option #2
- `pip3 freeze -> requirements.txt`
- Sane story as per option #2.
***

## Option #3
- Install `pipreqs` with `pip install pipreqs`
- Then try: `pipreqs /path/to/project` which will dump a `requirements.txt` in the specified directory.
- The difference here with respect to the other two is that, only those packages that are used in the specified folder will be saved.
***

## Option #4
- if you are using conda then try: `conda list -e > requirements.txt`
***

## References
- [Automatically create requirements.txt](https://stackoverflow.com/questions/31684375/automatically-create-requirements-txt)
***