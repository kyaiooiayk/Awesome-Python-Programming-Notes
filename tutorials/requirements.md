# How to create a `requirements.txt` file
***

## Introduction
- We'd like to create a file which stores all the packages we have manually installed.
- The questions arises whether we'd like to list all the dependencies or only those packages we have manually installed.
- As always it depends, so here are listed all the options you have.
- Take away is it is how kind of complicated this simple task really is in Python.
***

## If you project is in a jupyter notebook
- Firstly, your project file must be a py file which is direct python file.
- Convert it to `.py` using the command line: `jupyter nbconvert --to=python`
- Convert it to `.py` using the GUI: `File -> Download as -> Python (.py)`
- Then you can use one of the folling options listed below.
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

## Option #5
- This approach seems to be more robust and more repetable, meaning that there is no chance the subpackages will become somehow incompatible.
- Here is the issue: if your project uses `pandas==1.3.2` which in turns uses `numpy==1.21.2` among other packages. But pipreqs itself does not write the sub-packages in `requirments.txt`.
- Install `pip-tools` with: `pip3 install pip-tools`
- Then use this: `pipreqs --savepath=requirements.in && pip-compile --resolver=backtracking`
- The new `requirements.txt` will have a structure similar to this:
```shell
numpy==1.24.2
    # via
    #   datasets
    #   pandas
    #   pyarrow
    #   pytorch-lightning
    #   scikit-learn
    #   scipy
    #   torchmetrics
    #   transformers
```
***

## References
- [Automatically create requirements.txt](https://stackoverflow.com/questions/31684375/automatically-create-requirements-txt)
***