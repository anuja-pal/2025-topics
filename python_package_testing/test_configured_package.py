## Import functions directly from the package
from calculator_package import add_two_numbers, add_multiple_numbers
from calculator_package import multiply_two_numbers, multiply_multiple_numbers
from calculator_package import __version__, __author__

## Display package version, author
print(f"Using calculator_package version: v{__version__}")
print(f"This package was authored by: {__author__}")

## Test addition function
result1 = add_multiple_numbers(4,5,6)
print(f"4+5+6={result1}")

## Test multiplication function
result2 = multiply_multiple_numbers(4,5,6)
print(f"4*5*6={result2}")