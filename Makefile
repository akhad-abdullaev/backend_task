# ----------------------------------------
# Makefile for Django Backend Task Project
# ----------------------------------------

# Project metadata
PROJECT_NAME := backend_task
APP_DIR := apps
MANAGE := python manage.py
PIP := pip

# Virtual environment
VENV := venv
ACTIVATE := . $(VENV)/bin/activate

# Default target
.PHONY: help
help:
	@echo "Usage:"
	@echo "  make init        - create and activate virtualenv, install requirements"
	@echo "  make install     - install dependencies from requirements.txt"
	@echo "  make run         - run Django development server"
	@echo "  make migrate     - apply migrations"
	@echo "  make makemigrations - create new migrations"
	@echo "  make shell       - open Django shell"
	@echo "  make test        - run tests"
	@echo "  make lint        - run flake8 linting"
	@echo "  make clean       - cleanup __pycache__, *.pyc files, DB, logs"

# Initialize environment
.PHONY: init
init:
	include .envrc || true
	python3 -m venv $(VENV)
	$(ACTIVATE) && $(PIP) install --upgrade pip
	$(ACTIVATE) && $(PIP) install -r requirements.txt

# Install requirements
.PHONY: install
install:
	$(PIP) install -r requirements.txt

# Run development server
.PHONY: run
run:
	$(MANAGE) runserver

# Django migrations
.PHONY: migrate
migrate:
	$(MANAGE) migrate

.PHONY: makemigrations
makemigrations:
	$(MANAGE) makemigrations

# Django shell
.PHONY: shell
shell:
	$(MANAGE) shell

# Testing
.PHONY: test
test:
	$(MANAGE) test

# Linting (requires flake8 in requirements.txt)
.PHONY: lint
lint:
	flake8 .

# Cleanup
.PHONY: clean
clean:
	find . -type f -name '*.pyc' -delete
	find . -type d -name '__pycache__' -exec rm -rf {} +
	rm -f db.sqlite3
