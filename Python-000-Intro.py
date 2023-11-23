"""
    Python3 Introduction
    Intro, script setup and some best practices.
    Written by: Dominic Lee
    Date: 
"""
print("SHEBANG".center(50, "+"))  # Output separator
print("Example of a linux shebang:\n'#!/user/bin/python3'")
# If you are on a linux system you may see the first line of code is something like '#!/user/bin/python3'
# this is called a shebang, and is used to identify which version of Python the system should use to run the code.
# It has no effect on Windows systems, and is only needed if the script has been given executable permissions.
# If you want/need to include one it should be the first line, above the Doc-String,
# it starts with the hash/pound symbol then an exclamation mark '#!' followed by the file path to the Python interpreter to use.

print("SCRIPT LAYOUT".center(50, "+"))  # Output separator
# A Doc-String should be included at the beginning of each file to give a description of what is included and what the file does.
# Doc-Strings are basically unassigned strings using triple double quotation marks """ A Doc-String """
# There is one at the start of each of these files if you need a reference.

print("PEP-8".center(50, "+"))  # Output separator
# PEP-8 - https://peps.python.org/pep-0000/
# PEP-8 is the best practices and style guide for Python, it holds all the details and descriptions for indentation length,
# variable names and everything else.
# It can be worth looking over, but don't think you have to learn and adhere to them all.   

print("IMPORT CONTROL".center(50, "+"))  # Output separator
# You may come across the following bit of code at the bottom of someones code:
if __name__ == "__main__":
    # some code here!
    pass  # 'pass' can be used as a place holder to just move on to the next bit of code

# the above example wont actually do anything, but the if __name__ == "__main__": structure is used to control
# what happens when the file is ran verses when the file is imported into another file.
# We'll explore this in more detail later on.

# While you don't need any of these to start writing code, you should be aware of them.
# You should use a Doc-String and comments in your code at the very least.
