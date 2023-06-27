# Python wheels
***

## Wheels vs. eggs
- Python’s first mainstream packaging format was the .egg file.
- Now there’s a new format in town called the wheel (.whl). According to the Python Packaging Index’s description, a wheel *is designed to contain all the files for a PEP 376 compatible install in a way that is very close to the on-disk format.
***

## Advantages of wheels
- Faster installation for pure Python and native C extension packages.
- Avoids arbitrary code execution for installation. (Avoids setup.py)
- Installation of a C extension does not require a compiler on Linux, Windows or macOS.
- Allows better caching for testing and continuous integration.
- Creates .pyc files as part of installation to ensure they match the Python interpreter used.
- More consistent installs across platforms and machines.
- From the user’s perspective is that there’s no build stage when pip finds a compatible wheel on PyPI.
- Wheels are typically smaller in size than source distributions.
- Installing from wheels directly avoids the intermediate step of building packages off of the source distribution.
- There’s no need for a compiler to install wheels that contain compiled extension modules. The extension module comes included with the wheel targeting a specific platform and Python version.
***

## On the .whl file
- A wheel is a type of built distribution. It comes in a ready-to-install format and allows you to skip the build stage required with source distributions.
- The *.whl file is similar to an *.egg in that it’s basically a *.zip file in disguise. If you rename the extension from *.whl to *.zip, you can open it up with your zip application and see what is inside with `unzip -l <package_name>*.whl`.
- The *.whl file has a specially crafted filename that tells installers what Python versions and platforms the wheel will support.
- A wheel filename is broken down into parts separated by hyphens: `dist-version-build-python-abi-platform.whl`

***

## Source distribution  (=sdist)
- In some ways, a sdist is the opposite of a wheel.
- A source distribution contains source code. That includes not only Python code but also the source code of any extension modules (usually in C or C++) bundled with the package. With source distributions, extension modules are compiled on the user’s side rather than the developer’s.
- Source distributions also contain a bundle of metadata sitting in a directory called `<package-name>.egg-info`. This metadata helps with building and installing the package, but user’s don’t really need to do anything with it.
- A source distribution is what gets created when you run the following command: `python setup.py sdist`
***

## When to create a wheel
- They are a nice way to create a local repository of dependencies for your project(s) that you can install quickly. You could create several different wheel repositories to easily switch between different version sets for testing purposes.
- When combined with virtualenv, you have a really easy way to see how newer versions of dependencies could affect your project without needing to download them multiple times.
- What’s more important from the user’s perspective is that **there’s no build stage** when pip finds a compatible wheel on PyPI.
***

## Wheel and a source distribution
- Each python package on PPI will come with:
    - Only source distribution - the installation fetches a sdist.
    - Only a wheel - the installation fetches a prebuilt wheel
    - Both source and or even both at the same time. In this case, just if you are wondeing how, you cann force pip to install from source with: `pip install --no-cache-dir --force-reinstall --no-binary=:all: <package_name>`
- You can see the reason why a developer has chosen one of the above option by taking a look at each project’s page on PyPI and navigating to the Download files area. This section will show you what pip actually sees on the PyPI index server.
- Generally if only a source distribution (<package_name>.tar.gz) is provided this is due to the complexity of the project.
- On the other hand, if both source and wheel are provided, should the wheel be broken then pip will rever installing from source.
- If both a wheel and a source distribution, but pip **prefers** the wheel if it’s compatible with your system.
- **In conclusion** the source distribution will zip the source code, and compilation will happen on user machine when the package is installed, while a wheel will have pre-compiled binaries usable directly after installation.
***

## Different types of wheels
- A **universal wheel** contains py2.py3-none-any.whl. It supports both Python 2 and Python 3 on any OS and platform. The majority of wheels listed on the Python Wheels website are universal wheels.
- A **pure-Python wheel** contains either py3-none-any.whl or py2.none-any.whl. It supports either Python 3 or Python 2, but not both. It’s otherwise the same as a universal wheel, but it’ll be labeled with either py2 or py3 rather than the py2.py3 label.
- A **platform wheel** supports a specific Python version and platform. It contains segments indicating a specific Python version, ABI, operating system, or architecture.
***

## How to create a wheel for your package

### When you have a package but not a wheel
- **Step #1**: Let's create a clean virtual environment just for this: `conda create --name test_wheels`. Then `conda activate test_wheels` to activate the virutal environment.
- **Step #2**: Using pip is the recommended way to work with wheels. Older version of pip do not support the wheel format, hence upgrade pip with: `pip install --upgrade pip`. Let's upgrade also setuptools just in case: `pip install --upgrade setuptools`
- **Step #3**: Install the wheel package with: `pip install wheel` if not there already.
- **Step #4**: Let's assume we have a package from pip repository called `Unidecode` which takes a string of text and attempt to replace any unicode with its ASCII equivalent. This will work with any other package and we are assuming this package does not have a wheel. Will use this command: `pip wheel --wheel-dir=my_wheels Unidecode`. If you start a now python sheel and try to `import unidecode` it would not work and this is what we wanted at the moment.
- **Step #5**: We can install our wheel with the following command: `pip install --no-index --find-links=./wheel-dir/ Unidecode`
- **Step #6** To verify if we have corrrectly installed the unicode package we can start a new python sheel with `python3` and the  try to import unicode with `import unicode`. If not error is threw then th epackage was sucessfully installed the package.

### When you are building a package from scratch
- **Step #1**: Let's create a clean virtual environment just for this: `conda create --name test_wheels`. Then `conda activate test_wheels` to activate the virutal environment.
- **Step #2**: Using pip is the recommended way to work with wheels. Older version of pip do not support the wheel format, hence upgrade pip with: `pip install --upgrade pip`. Let's upgrade also setuptools just in case: `pip install --upgrade setuptools`. Additionall install python official package publisher with: `pip install twine`.
- **Step #3**: Install the wheel package with: `pip install wheel` if not there already.
- **Step #4**: Create a `setup.py` file at the root of our project:
```
from setuptools import setup, find_packages

setup(
    name="mypackage",
    version="0.0.1",
    author="kyaiooiayk",
    author_email="kyaioiayk@example.com",
    description="Dummy package",
    packages=find_packages(),
    options={"bdist_wheel": {"universal": True}},
)
```
- **Step #5**: Buil the wheel with: `python setup.py sdist bdist_wheel` which creates both a source distribution (sdist) and a wheel (bdist_wheel), placed in dist/ under the current directory. Keep in mind that that *.whl is a binary file whereas sdist distribution is not a binary file and is stored as *.tar.gz compressed file.
- **Step #6**: Check that you can use after by looking for common problems such as the package directory having an abnormal structure or the presence of duplicate files: `check-wheel-contents dist/*.whl`
- **Step #7**: Since both sdist and bdist_wheel output to dist/ by default, you can safely tell twine to upload/publish everything under dist/ using a shell wildcard (dist/*) with: `twine upload dist/*`.
- **Step #8**: Check if you can install your package with: `pip install <package_name>`
***

## References
- [Chapter 39 - Python wheels](https://python101.pythonlibrary.org/chapter39_wheels.html)
- [What Are Python Wheels and Why Should You Care?](https://realpython.com/python-wheels/)
- [Python Wheels](https://pythonwheels.com/)
- [Setuptools And Python Wheels](https://kimsereylam.com/python/2021/02/26/setuptools-and-python-wheels.html)
***
