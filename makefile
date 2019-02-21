include env
.DEFAULT_GOAL := all

mp:
	python3 mptest.py

all:
	python3 main.py

.PHONY: all