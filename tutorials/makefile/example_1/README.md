# Instructions

- Create the following `Makefile` file.
```makefile
VENV = venv
PYTHON = $(VENV)/bin/python3
PIP = $(VENV)/bin/pip

run: $(VENV)/bin/activate
	$(PYTHON) app.py

$(VENV)/bin/activate: requirements.txt update_pip
	ECHO "Chosen name for venv:" $(VENV)
	python3 -m venv $(VENV)
	$(PIP) install -r requirements.txt

update_pip:
	ECHO "Update pip"
	$(PYTHON) -m pip install --upgrade pip

clean:
	rm -rf __pycache__
	rm -rf $(VENV)
```
- Check there is a tab before each recepie with: `cat -e -t -v  Makefile`. You should be able to see the following:
```shell
VENV = venv$
PYTHON = $(VENV)/bin/python3$
PIP = $(VENV)/bin/pip$
$
run: $(VENV)/bin/activate$
^I$(PYTHON) app.py$
$
$(VENV)/bin/activate: requirements.txt update_pip$
^IECHO "Chosen name for venv:" $(VENV)$
^Ipython3 -m venv $(VENV)$
^I$(PIP) install -r requirements.txt$
$
update_pip:$
^IECHO "Update pip"$
^I$(PYTHON) -m pip install --upgrade pip$
$
clean:$
^Irm -rf __pycache__$
^Irm -rf $(VENV)$
```
- The file above show the link btw target and pre-requirements. For instace when we type `make run` this is what is going to happen:
    - The target is read but it depends on $(VENV)/bin/activate.
    - `$(VENV)/bin/activate` is itself a target which depends on two pre-requirements: `requirements.txt` a file and `update_pip` which itself is another target.
    - When the environment is created, pip is then updated and the requirements installed.
- The advantaged of make is that when this is run the second time, make would not call the recepies which install the environment, update pip and install the requirements because these were already generated. This may save you some time.
- When you are done you can clean the working directory with: `make clean`.
