# setup.py
***

## What is it?
- The setup file dictates everything Python installer needs to know when installing your package.
- Two things needs to be continously updated:
    - Version
    - Install requirements
***

## Used to deploy the package in PyPI
- Go to pypi.org and create an account
- Install twine with: `pip install twine`
- Next, we’ll create an installable package. Go to the directory where the setup.py file is, and run: `python setup.py sdist bdist_wheel`. This creates `dist` and `your_package.egg-info`. The former is what we'll deploy in PyPI.
- Make sure your `.gitignore` is update otherwise this installation files will be pushed to the repo.
- Verify the distribution files you just created are okay by running: `twine check dist/*`
- Deploy first to the PyPI test domain with: `twine upload --repository-url https://test.pypi.org/legacy/ dist/*`
- Go to test.pypi.org and check your new library.
- Push it to the real PyPI: `twine upload dist/*`
- This can all be automated with the following shell script called build_deply.sh (`./build_deploy.sh` or `./build_deploy.sh --test`).
- Make the script executable with: `chmod +x build_deploy.sh`
```shell
rm -r dist ;
python setup.py sdist bdist_wheel ;
if twine check dist/* ; then
  if [ "$1" = "--test" ] ; then
    twine upload --repository-url https://test.pypi.org/legacy/ dist/*
  else
    twine upload dist/* ;
  fi
fi
```
***

## References
- [How to build your first python package](https://towardsdatascience.com/how-to-build-your-first-python-package-6a00b02635c9)
- [Publishing packages and modules](https://packaging.python.org/en/latest/guides/distributing-packages-using-setuptools/)
***
