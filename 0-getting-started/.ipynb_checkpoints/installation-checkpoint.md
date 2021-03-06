# Installation

There are multiple ways to install Python. The easiest way to do so is through the Anaconda distribution which comes in two flavours:

## Anaconda (Recommended)

Anaconda is a very large installation and is most useful for users who are not familiar with installing modules or packages with other package managers. Choose Anaconda if you:

* Are new to `conda` or Python
* Like the convenience of having Python and over 150 scientific packages automatically installed at once
* Have the time and disk space

You can install Anaconda [here](https://www.anaconda.com/distribution/#download-section). Make sure to get the Python 3 (look for 3.x) version.

```{Note}
For students in CIS 105, I would recommend installing through Anaconda. It makes life much easier.
```

## Miniconda

Miniconda simply gives you the Python interpreter along with a command-line tool called `conda` which operates as a cross-platform package manager geared towards installing Python packages. Choose Miniconda if you:

* Do not mind installing each of the packages you want to use individually
* Do not have time or disk space to install over 150 packages at once

You can install Miniconda [here](https://docs.conda.io/en/latest/miniconda.html). Make sure to get the Python 3 version.

## pvenv

[pyenv](https://github.com/pyenv/pyenv) is a light-weight Python version management tool that lets you easily switch between multiple versions of Python. I personally prefer using pyenv for work and collaborating with others as it makes switching between Python versions rather convenient. If you are using a Mac, I suggest installing pyenv through Homebrew.

> pyenv is NOT required or needed for the purposes of CIS 105.
