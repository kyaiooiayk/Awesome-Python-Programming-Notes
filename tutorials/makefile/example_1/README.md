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
- Check there is tab before each instructions with: `cat -e -t -v  Makefile`. You should be able to see the following:
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
