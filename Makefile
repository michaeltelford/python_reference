#!/bin/bash

.PHONY: test run

test:
  find ./test -name "*.py" -exec python $0 \;

run:
  python src/main.py
