# Notes on package file structure for proper documentation

## __init__.py files
__init__.py files must be 

# Notes on files

## index.rst
DO NOT DELETE THIS FILE! This file is used as the root file to build the entire
documentation.

## api.rst
DO NOT DELETE THIS FILE! It contains the all-important `.. autosummary::`
directive with `:recursive:` option, without which API documentation wouldn't
get extracted from docstrings by the `sphinx.ext.autosummary` engine. It is
hidden (not declared in any toctree) to remove an unnecessary intermediate
page; index.rst instead points directly to the package page.
DO NOT REMOVE THIS FILE!
