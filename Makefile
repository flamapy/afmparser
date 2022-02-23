.ONESHELL:

.PHONY: build
build:
	cd afmparser
	antlr4 -Dlanguage=Python3 UVL.g4
	sed -i "s/from AFMParser/from .AFMParser/g" AFMLexer.py
	
upload-testpypi:
	python3 -m build
	python3 -m twine upload --repository testpypi dist/*

upload-pypi:
	python3 -m build
	python3 -m twine upload --repository pypi dist/*
