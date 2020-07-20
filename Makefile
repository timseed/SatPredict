.DEFAULT_GOAL := all

PYSRC = ham
PYTEST = ham/tests


VENV_NAME?=pe38
VENV_ACTIVATE=. ~/$(VENV_NAME)/bin/activate
PYTHON=~/${VENV_NAME}/bin/python3
PIP = pip3
PYCOV = $(PYTHON) -m coverage
Package = ham-0.0.1.tar.gz

objects := $(patsubst %.py,$(Package).tar.gz,$(wildcard *.py))

all : test build install

# Requirements are in setup.py, so whenever setup.py is changed, re-run installation of dependencies.
venv: $(VENV_NAME)/bin/activate
$(VENV_NAME)/bin/activate: setup.py
	test -d $(VENV_NAME) || virtualenv -p python3 $(VENV_NAME)
	${PYTHON} -m pip install -U pip
	${PYTHON} -m pip install -e .
	touch $(VENV_NAME)/bin/activate

.PHONY: build
build:
	$(PYTHON) setup.py sdist

check:
	$(PYTHON) -m pylint -E            $(PYSRC)
	$(PYTHON) -m black --check --diff $(PYSRC)
	#shellcheck -x scripts/*

format:
	$(PYTHON) -m black $(PYSRC)

test:
	$(PYTHON) -m pytest $(PYTST)

coverage:
	pytest --cov=$(PYSRC)

install:
	$(PIP) install dist/$(Package) --upgrade

.DEFAULT_GOAL := all 

bump-minor:
	$(PYTHON) -m bumpversion minor --tag --commit

bump-patch:
	$(PYTHON) -m bumpversion patch --tag --commit

