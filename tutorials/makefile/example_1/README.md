# Instructions

- Create the following `Makefile` file.
```makefile
VENV = venv
PYTHON = $(VENV)/bin/python3
PIP = $(VENV)/bin/pip

.PHONY: clean run

run: $(VENV)/bin/activate
	@echo "Running the app"
	$(PYTHON) app.py

install_venv:
	@echo "Install venv"
	python3 -m venv $(VENV)

$(VENV)/bin/activate: requirements.txt install_venv update_pip
	@echo "Chosen name for venv:" $(VENV)
	$(PIP) install -r requirements.txt

update_pip:
	@echo "Update pip"
	$(PYTHON) -m pip install --upgrade pip

clean:
	@echo "Cleaning directory"
	rm -rf __pycache__
	rm -rf $(VENV)
```
- Check there is a tab before each recepie with: `cat -e -t -v  Makefile`. You should be able to see the following:
```shell
VENV = venv$
PYTHON = $(VENV)/bin/python3$
PIP = $(VENV)/bin/pip$
$
.PHONY: clean run$
$
run: $(VENV)/bin/activate$
^I@echo "Running the app"$
^I$(PYTHON) app.py$
$
install_venv:$
^I@echo "Install venv"$
^Ipython3 -m venv $(VENV)$
$
$(VENV)/bin/activate: requirements.txt install_venv update_pip$
^I@echo "Chosen name for venv:" $(VENV)^I$
^I$(PIP) install -r requirements.txt$
$
update_pip:$
^I@echo "Update pip"$
^I$(PYTHON) -m pip install --upgrade pip$
$
clean:$
^I@echo "Cleaning directory"$
^Irm -rf __pycache__$
^Irm -rf $(VENV)$
```
- The file above shows the link btw target and pre-requirements. For instace when we type `make run` this is what is going to happen:
    - The target is `run` but this depends on `$(VENV)/bin/activate`.
    - `$(VENV)/bin/activate` is itself a target which depends on two pre-requirements: `requirements.txt` (a file) and `update_pip` (another target).
    - When the environment is created, pip is then updated and the requirements installed.
- The advantaged of `make` is that when this is run the second time, make would not call the recepies which install the environment, update pip and install the requirements because these were already generated. This may save you some a considerable amount of time if the project is big.
- When you are done, you can clean the working directory with: `make clean`.
Your Makefile contains two special targets - run and clean. Special in the sense they don’t represent an actual file that exists. And since make executes the recipes of a target if that target does not exist, these two targets will always be executed. However, if later if you have a file called run or clean, then since these targets have no prerequisites, make will consider these to always be newer and so, will not execute the recipes. To overcome this, make has something called a Phony target. By declaring a target to be Phony, you tell make not to consider an existing file with the same name. To make the run and clean targets phony, add this to the top: `.PHONY: run clean`
