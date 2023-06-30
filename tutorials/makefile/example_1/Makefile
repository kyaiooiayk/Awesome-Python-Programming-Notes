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
