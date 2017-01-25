#!/bin/bash

.PHONY: help test run

help:
	@echo ""
	@echo "Python Reference Project"
	@echo "See the README.md file for more reference details."
	@echo ""
	@echo "test   - Run all unit tests."
	@echo "run    - Run the main.py file."
	@echo ""

test:
	@find ./test -name "*.py" -exec python {} \;

run:
	@python src/main.py
