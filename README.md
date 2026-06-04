# BRL-CAD Python Bindings

## Prerequisites
Before setting up the Python package, ensure that you have cloned and compiled the core C++ BRL-CAD Moose library repository on your machine. Take note of the directory path containing your compiled shared object file (libbrlcad.so).

## Installation and Clean Setup Guide

Install the Necessary Build Packages:
```bash 
pip install build
```

Configure your environment path:
```bash
export LD_LIBRARY_PATH="/path/to/your/moose/build/src:$LD_LIBRARY_PATH"
```

Build Python Wheel:
```bash 
python -m build
```

Install the Package:
```bash 
pip install dist/brlcad_python_bindings-*.whl
```
## Verification and Testing 

```bash 
cd tests
# before running the test open the file and change the path of the .g file to you desired testing .g file
py test_get_title.py 

```