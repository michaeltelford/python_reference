# Python 3 Reference Project

A go-to example Python 3 project referencing the main points of the language, all in one place for convenience.

This reference project is a personal one, whilst I've tried to ensure that the practices within are standard language practices, I am not a Python expert, hence the need for this project in the first place.

Please view both the details below and the actual source code itself as needed. Enjoy!

## Prerequisites

This reference assumes a working installation of:

- `python3`
- `pip3`

## Technical

### Code Standards

See the accepted standards at:
[https://www.python.org/dev/peps/pep-0008/](https://www.python.org/dev/peps/pep-0008/)

### Software Packages

Search for third party software packages at:
[https://pypi.python.org/pypi](https://pypi.python.org/pypi)

Then install them with pip:

`pip3 install ipython`

Or install them at the project level:

```bash
echo "ipython" >> requirements.lock
pip3 install -r requirements.lock # installs deps from PyPi.
```

### virtualenv

`virtualenv` means you can use a separate python3 executable rather than use the system installation of python (which is not the best idea in case you accidentally break it).

Run once per host OS to install virtualenv:

`pip3 install virtualenv`

Then run once per project:

```bash
cd <project_dir>
virtualenv -p python3 env # installs python3, pip3 etc.
source env/bin/activate # optional but recommended for below commands.
pip install -r requirements.lock # installs deps from PyPi.
python some_file.py # etc...
```

### Example Class

> dog.py

```python
from animal import Animal # assumes animal.py exists at the same level.


class Dog(Animal):
	“Dog animal class representation.”

	static_var = True

	def __init__(self, name=None):
		Animal._init__(self)
		self.name = name # instance var.

	def set_age(self, age=1):
		“Sets the age of of the dog.”
		super(Dog, self).set_age() # calls Animal.set_age()

	def static_method(): # doesn't contain the self param.
		return True
```

> main.py

```python
from dog import Dog


dog = Dog(“Fido”)
dog.set_age(4)
# call any inherited methods from the Animal class...
```

### Importing

The below method of updating the path is **NOT** the recommended best approach in the later versions of Python however it does work so I've included it here (tut tut!).

```python
import sys
sys.path.append("./some_folder")
from main import * # or ‘import main’ looks for main.py


# Use main.py module contents here...
```

### unittest

Use `unittest` for unit testing your code:

> lib_tests.py

```python
import unittest
from something import *


class TestGetField(unittest.TestCase):

    def setUp(self):
        self.something = Something()

    def test_something(self):
        self.assertEqual(True, self.something.some_method())


if __name__ == "__main__":
    unittest.main()
```

Execute the tests with:

`python lib_tests.py`

### behave

For BDD (Gherkin and Python) use `behave`. See [here](https://pythonhosted.org/behave/tutorial.html) for more details.

The directory structure for `behave` should roughly be as follows:

- features/*.features: Gherkin files.
- features/environment.py: trigger events e.g. pre test etc.
- features/steps/*.py: The code behind the Gherkin steps.

To run the tests:

```bash
cd features
behave # runs tests
```

### Debugging

Obviously oldschool debugging using `print(var)` can be used but if something more powerful is needed you can use `ipython` as follows:

```python
# requires 'ipython' to be installed, notice the case of IPython
from IPython import embed


if __name__ == "__main__":
  name = "Michael"
  embed() # launches an ipython shell, good for object inspection, type 'exit' to continue running the program
  do_something(name)
```

## Thanks

Thanks for looking, if you have any suggestions on improving the reference or new additions then feel free to raise an issue.  Also, if you'd like to have your own reference project then feel free to use this as a starter and fork it.
