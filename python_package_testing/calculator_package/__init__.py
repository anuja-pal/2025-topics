## Import functions from modules
from .addition import add_two_numbers, add_multiple_numbers
from .multiplication import multiply_two_numbers, multiply_multiple_numbers

## Define package level variables
__version__ = "0.1.0"
__author__ = "AP"

## Print a message when the package is imported
print(f"calculator_package v{__version__} successfully initialised!")

## Import the advanced subpackage
from . import advanced