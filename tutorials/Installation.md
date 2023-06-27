# Installation & packages management

## Unistalling Anaconda via command line
- Following this [Ref](https://docs.anaconda.com/anaconda/install/uninstall/)
- Install the Anaconda-Clean package from Anaconda Prompt (terminal on Linux or macOS): `conda install anaconda-clean`
- Remove all Anaconda-related files and directories without being prompted to delete each one: `anaconda-clean --yes`

## How to create a virtual environment with conda
- See which conda you are using (meaning it shows the path of the executable being called): `which conda`
- Create a virtual environment using conda specific command: `conda create –-name my_env_name python=3.7` (check for the last stable Python realease [here](https://www.python.org/downloads/macos/))
- Activate the virtual environment: `conda activate my_env_name`
- How to visualise all the env available: `conda env list`
- Install any package you like via these two options: `conda install package_name` or `pip package_name`
- How to delete a virtual env: `conda env remove --name=my_env_name`

## How to downgrade to an older version of python
- If using conda: `conda create -n you_virtual_env_name python=3.8 anaconda`

## How to manage python packages
- Update a to a specific module version: `scikit-learn==0.24.1 –upgrade`
- How to revert to an older version: first `pip uninstall scikit-learn` then `pip install scikit-learn==0.18.2`

## Machine learning specific packages
- ** XGBoost on a mac**. If your mac does not reconignis the `port` command then install [this](https://guide.macports.org/chunked/installing.macports.html). Following this [link](https://machinelearningmastery.com/install-xgboost-python-macos/)
- **PyTorch**: Follow this [refenrence](https://pytorch.org/): `coda install pytorch -c pytorch`
- **Tensorflow & keras**: first `pip install tensorflow` then `pip install keras` as keras runs on top of tensorflow and not viceversa.
