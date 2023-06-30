VENV = venv
PYTHON = $(VENV)/bin/python3
PIP = $(VENV)/bin/pip

.PHONY: clean run all

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

all: run clean
