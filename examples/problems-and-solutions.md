# Problems and solutions

Some problems I've run into while programming/using the terminals and how I solved them.

## PIP installations

Pip will normally try to install packages into the global site-package directory,
which can be accessed by all python scripts. On my university provided laptop,
this directory is protected and thus pip installs packages into user specific
site-packages directories found at ~/.local/lib/python3.XX/site-packages

When a python script is run, it searches for packages in the directory for the current
python version (ie. /python3.12/site-packages if the current version of python is 3.12).
This means that if python updates, it will search for packages in the new version's directory
thus failing to find any.

Solution:
I added the directory manually to path so that the packages will always be found:
`export PATH = ~/.local/lib/python3.12/sire-packages:$PATH`


## Python console is very slow when running in terminal

If the python interpreter starts and closes in terminal noticeably slower than before and/or
if executing lines of code takes suspiciously long, check out the size of the ~/.python\_history
file (also ~/.sympy\_history if you do a lot of symbolic calculations in terminal)

You can see the size by typing:
`ls -la | grep .python_history`
And reading the number right before the month. It is the file size in bytes.

If the file size is very large, that might be what's causing the slowdown. It is safe to
remove the history files since they don't usually contain any critical information
since the python interpreter is mostly used for quick testing and calculations.

Solution:
Delete the python (and/or sympy) history file(s) by running:
`rm .python_history`


## Fortran functions behave unexpectedly

Since Fortran 95 if a variable is initialized inside a function, it is implicitly initialized with
the 'save'-attribute which preserves the value of the variable between function calls. This
can lead to unexpected behaviour (as it did for me). So if you don't want the 'save'-attribute
to be implicitly used you need to first declare the variable and the on a separate line assign
the initial value to the variable.

Solution:
If you do NOT want variables to save, first declare, then assign:
`integer :: i`
`i = 0`

If you DO want variables to save, initialize:
`integer :: i = 0`
or explicitly
`integer, save :: i = 0`



