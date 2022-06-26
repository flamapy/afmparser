.ONESHELL:

.PHONY: build
build:
	antlr4 -Dlanguage=Python3 afmparser/AFM.g4
