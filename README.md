# idea-bag-solutions

These are a list of solutions to problems listed in the Idea Bag App at: [Idea Bag](https://play.google.com/store/apps/details?id=com.alansa.ideabag2)

## Instructions

### Pre-requisites

- Before running any file that has internal module (module created
specifically for program run in this project) Run:

```bash
export PYTHONPATH=/path/to/working/directory
```

## List of Completed Idea Bag Problems

- [x] city distance
- [x] fatorial
- [x] tax calculation
- [x] half string
- [x] morse code maker
- [x] palindrome checker
- [x] rss creator
- [x] word counter
- [x] FizzBuzz
- [x] Print PI to the nth decimal place using 22/7
- [ ] Print PI to the nth decimal place to get a non repeating decimal number

  - Aticles/resources:

    - [Stackoverflow1](https://stackoverflow.com/q/45113790)

## Installable packages

Listed below are reusable Python Packages that can be install from a Github
repository.

An installable package must have a pyproject.toml or setup.py file
containing all configurations. You can find instructions about package Python
projects [here](https://packaging.python.org/en/latest/tutorials/packaging-projects/)

Finally, run these commands:

- Install dependencies:

```shell
  python -m pip install --upgrade build
```

- build and create `.tar.gz` file

```shell
  python -m build
```

In any case you would like to install the packages in a project, move the `.tar.gz` file to
you local project then run:

```shell
  pip install path/to/commons_benatt-0.0.1.tar.gz
```
