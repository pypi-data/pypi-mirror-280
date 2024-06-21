# qolab

Collection of scripts to run experimental hardware with python.

Started in April 2021 by Eugeniy E. Mikhailov

## Build instructions

To build a python wheel package and put it in `./dist/` directory, run

~~~~~
flit build
~~~~~

## Test instructions

~~~~~
export PYTHONPATH=.
python -m pytest 
~~~~~

Note that we cannot just run `pytest` since I see no way to set the module search path.

