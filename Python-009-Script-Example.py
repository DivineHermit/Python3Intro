"""
    Python3 Introduction
    Imports and Modules.
    Written by: Dominic Lee
    Date: 04/01/2024

    This is an example of using functions in a script.
"""

def add(val1: float, val2: float):
    """Add val1 and val2 together and return the result."""
    return val1+val2


def subtract(val1: float, val2: float):
    """Subtract val2 from val1 and return the result."""
    return val1-val2


def multiply(val1: float, val2: float):
    """Multiply val1 by val2 and return the result."""
    return val1*val2


def divide(val1: float, val2: float):
    """Divide val1 by val2 and return the result."""
    return val1/val2


def main():
    """This function acts as the main code of script."""
    while True:
        val1 = input("Enter first number: ")
        val2 = input("Enter second number: ")

        if val1 == "" or val2 == "": break  # check for a empty input and break the while loop if no input is supplied.
        val1, val2 = float(val1), float(val2)
        # We can now call our functions and print out the results in an f-string.
        print(f"{val1}+{val2} = {add(val1, val2)}")
        print(f"{val1}-{val2} = {subtract(val1, val2)}")
        print(f"{val1}*{val2} = {multiply(val1, val2)}")
        print(f"{val1}/{val2} = {divide(val1, val2)}")


if __name__ == "__main__":
    # If we run this file the below call to the 'main()' function is called and the code in that function is activated.
    # However, if we imported this file, the 'main()' function is NOT run and above functions are loaded into the importing script to be used there.
    main()
