"""
    Python3 Introduction
    Imports and Modules.
    Written by: Dominic Lee
    Date: 12/01/2024
"""
# This line is where imports are usually listed.

# Sometimes you may want, or need, to use code from the Python standard library or third party modules.
# A module, framework or code library are names for a collection of files that can be imported and used in your projects.
# Pygame, Pyperclip, Numpy, Random, & Pandas are some example of importable modules. 
# We briefly saw use of imports when we used the random module in the Python-005-Operators.py file.

print("IMPORT THE RANDOM MODULE".center(50, "+"))  # Output separator
# To import a module you use the keyword 'import' followed by the name of the module, lets import the random module:
import random

# We can now access the function in the random module as follows:

rnd_int = random.randint(1, 11)  # The 'randint' function will return a number from 1 to 10, 11 isn't included.
print("Number picked by randint:", rnd_int)

# One of the best practices is how you order your imports:
# Standard Library
# Third Party
# Your local files

import sqlite3                      # A Python module from the standard library for single file SQL databases.
# Third party imports would be next, but if you dont have it installed the code will throw an import error, see below.
import Python_009_Library_Example as PLE  # Finally local imports, module names with hyphens require special handling so we've used underscores for ease of import
# Also we can use aliasing to shorten the name of the module to 'PLE' so we don't have to type out 'Python_009_Library_Example' to access the code.

# Handling third party imports using a try/except statement:
try:
    import pyperclip    # This is a third party module that can be installed from PyPi.org using the 'pip install pyperclip' console command.
    # if you dont have pyperclip installed then an ImportError occurs and can be handled below.
except ImportError:
    # The module, probably, isn't installed so lets print out a message.
    print("\nError importing 'Pyperclip' module.\nYou can install it using 'pip install pyperclip'")

print("IMPORTING OUR MATH FUNCTIONS".center(50, "+"))  # Output separator
# Since we handled the import error from pyperclip the script will continue to run and we can use the code from the other modules
print("1+1 =", PLE.add(1,1))
print("1066/69 =", PLE.divide(1066, 69))
print("24*20 =", PLE.multiply(24, 20))
print("90210-210 =", PLE.subtract(90210, 210), "\n")

print("GETTING FILE PATHS WITH OS.PATH".center(50, "+"))  # Output separator
# We can use the 'from' keyword to import only specific code, like this:
from os import path
# The 'os' module has many functions for interacting with the Operating System, but by using the 'from' keyword
# we import only what we need, saving memory and complexity.
# Now we can print out the file path of this script:
print("This script is located at:", path.abspath(__file__), "\n")

# A common occurrence in online tutorials is to use star '*' imports, it looks like this:
from turtle import *
from math import *
# We now have access to ALL the functions of the turtle and maths modules... but this is bad practice.
# Not only do we not know from which module a function is from the math module will override and functions with the same name in the turtle module.
# It is better to use aliasing to shorten the names of modules or the imported functions.
