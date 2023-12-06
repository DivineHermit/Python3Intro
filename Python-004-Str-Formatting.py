"""
    Python3 Introduction
    String Formatting, Operators and Integers.
    Written by: Dominic Lee
    Date: 11/11/2023
"""
# STRING FORMATTING #
# ================= #
print("MEMORY ALLOCATION".center(50, "+"))  # Output separator
# Despite what it may look like while explore string formatting, strings are immutable, meaning they can NOT be changed.
text = "A simple string."
print("Memory address:", id(text), "upon creation.")
# We can use Python's 'id' function to get the id of the memory block our string is saved in.
# Now lets turn our text into capitol letters using the 'upper' method and see what happens:
text = text.upper()
print("Memory address:", id(text), "after using the 'upper()' method and reassignment.")
# A new string object was created in memory and our 'text' variable now points to this new capitalized string.
# You may think that by using text = text.upper() we are reassigning the original variable, so that is changing the memory address,
# but lets just try printing out the results of lowering the text:
print("Memory address:", id(text.lower()), "after using the 'lower()' method.")
# While this is somewhat advanced for so early on, you will very shortly be able to write a program to access data from files,
# databases or other sources that could easily extend into the hundreds(100s), thousands(1000s) or possibly millions(1,000,000s) of lines
# which could slow down your computer, or worse, a working server.
# This is just something to be aware of, not some dread leviathan that will eat your computer from the inside out.

# STRING ASSIGNMENT #
# ================= #
print("STRING ASSIGNMENT".center(50, "+"))  # Output separator
# Strings can be assigned using quotation marks, and while you end up with a string object, they have a few differences
single_quote = 'Single quotes can contain double quotes "" but not other single quotes, unless you escape them (see below).'
double_quote = "And double quotes can contain single quotes '' but not other double quotes, unless you escape them (see below)."
triple_single_quote = '''You can use triple single quotes, but this style isn't used very often, in my experience.'''
triple_double_quote = """Triple quotes
can span multiple lines,
and contain both '' and ""."""
# Triple quotes are used for Doc-Strings, short for documentation strings, these are placed at the start of a file, class or function
# and give a place for you to write relevant information about what the code does and what parameters are needed.
# We'll cover Doc-Strings a little more in the functions section later on.
print(single_quote, "\n")
print(double_quote, "\n")
print(triple_single_quote, "\n")
print(triple_double_quote)

# ESCAPE CHARACTERS #
# ================= #
print("ESCAPE CHARACTERS".center(50, "+"))  # Output separator
# Those of you paying attention will have notice I mentioned 'escape them' and wondered what I was babbling about, well.
# Escape characters have special meanings in strings for example '\n' will create a new line, while '\t' will appear as
# four(4) spaces otherwise known as a tab.
# But we can also escape quotation marks to make them part of the text instead of part of the code:
escaped_text = 'Cann\'t, wont\'t, we\'re'
print(escaped_text)
# By placing a backslash '\' before the single quote we tell Python we'er not ending the string just including the apostrophe character in the text.
# I prefer using double quotation marks to make strings as it lessens the use of escape characters and makes things easier to read.

# We can add the letter 'r' before the quotation marks to tell Python to make a raw text string.
# This will treat the backslash '\' as an actual character instead of the escape character.
# This can be helpful if you need to specify a Windows file/folder path, e.g. 'C:\Users\Bob' or if your using Regular Expressions.
# (Lets not fall down that rabbit hole just yet!)
raw_text = r"Cann't,\nwont't,\nwe're\\"
print(raw_text)

# SLICING #
# ======= #
print("SLICING".center(50, "+"))  # Output separator
slicing_text = "Hilary pointed out some typos in this section, so thanks to her."
# They also class as an array, meaning each character in the string has an index that can be used to identify it.
# Python indexing starts at zero(0) so the index of the first letter of a string is 0, while the second letter is 1 and so on.

# We can slice array's using a three(3) part pattern at the end of the array, it looks like this [::] or [1:5:3] with values.
# The first value is the starting index, the second is the end index and the final, optional, value are the steps.

# Let's get the first five(5) letters from our 'slicing_text' string above:
print(slicing_text[:6])  # this will print out 'Hilary'
# We didn't supply a starting index so Python will start at the beginning of the string and go to the end value.
# You may of noticed we wanted five(5) characters and stopped at index six(6)... this is because the last index is not included in the slice.

print("The letter at index 3 is:", slicing_text[3])  # here we only supply one value, so this is an index and not a slice.

# Here are three(3) slicing examples using the slicing_text string above:
print("The letters at index 14 to 18 is:", slicing_text[-14:-8])  # you can use negatives to slice from the end of a string
# but note when using a negative index the last letter index is -1 not -0
print("The letters at index -28 to -24 is:", slicing_text[57:60])
print("The letters at index 83 to 89 is:", slicing_text[:6])

# The step value can be used to skip over some of the indexes, lets print the first index and skip ahead four(4) character and repeat till the end.
print("Every forth(4) character:\n" + slicing_text[::4])

# STRING METHODS #
# ============== #
print("STRING METHODS".center(50, "+"))  # Output separator
text = """

Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse
cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non
proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

"""
[print(x) for x in dir(text) if not x.startswith("_")]  # (a list comprehension to print out all the string methods)
# Once a variable has been assigned, you have access to lots of methods for interacting with the data.
# Here is a brief description of them from the W3Schools.com (a great resource for several programming/development languages)
# Method summery from: https://www.w3schools.com/python/python_strings_methods.asp
# capitalize()  - Converts the first character to upper case
# casefold()    - Converts string into lower case
# center()      - Returns a centered string
# count()       - Returns the number of times a specified value occurs in a string
# encode()      - Returns an encoded version of the string
# endswith()    - Returns true if the string ends with the specified value
# expandtabs()  - Sets the tab size of the string
# find()        - Searches the string for a specified value and returns the position of where it was found
# format()      - Formats specified values in a string
# format_map()  - Formats specified values in a string
# index()       - Searches the string for a specified value and returns the position of where it was found
# isalnum()     - Returns True if all characters in the string are alphanumeric
# isalpha()     - Returns True if all characters in the string are in the alphabet
# isascii()     - Returns True if all characters in the string are ascii characters
# isdecimal()   - Returns True if all characters in the string are decimals
# isdigit()     - Returns True if all characters in the string are digits
# isidentifier()- Returns True if the string is an identifier
# islower()     - Returns True if all characters in the string are lower case
# isnumeric()   - Returns True if all characters in the string are numeric
# isprintable() - Returns True if all characters in the string are printable
# isspace()     - Returns True if all characters in the string are whitespaces
# istitle()     - Returns True if the string follows the rules of a title
# isupper()     - Returns True if all characters in the string are upper case
# join()        - Joins the elements of an iterable to the end of the string
# ljust()       - Returns a left justified version of the string
# lower()       - Converts a string into lower case
# lstrip()      - Returns a left trim version of the string
# maketrans()   - Returns a translation table to be used in translations
# partition()   - Returns a tuple where the string is parted into three parts
# replace()     - Returns a string where a specified value is replaced with a specified value
# rfind()       - Searches the string for a specified value and returns the last position of where it was found
# rindex()      - Searches the string for a specified value and returns the last position of where it was found
# rjust()       - Returns a right justified version of the string
# rpartition()  - Returns a tuple where the string is parted into three parts
# rsplit()      - Splits the string at the specified separator, and returns a list
# rstrip()      - Returns a right trim version of the string
# split()       - Splits the string at the specified separator, and returns a list
# splitlines()  - Splits the string at line breaks and returns a list
# startswith()  - Returns true if the string starts with the specified value
# strip()       - Returns a trimmed version of the string
# swapcase()    - Swaps cases, lower case becomes upper case and vice versa
# title()       - Converts the first character of each word to upper case
# translate()   - Returns a translated string
# upper()       - Converts a string into upper case
# zfill()       - Fills the string with a specified number of 0 values at the beginning

# STRING CONCATENATION #
# ==================== #
print("STRING CONCATENATION".center(50, "+"))  # Output separator
# Concatenation
#    noun: concatenation; plural noun: concatenations
#    a series of interconnected things.

# While you can't do math with strings you can use mathematical operators to manipulate them, for example:
str1 = "Hello"
str2 = "world!"
# The '+' operator will concatenate both strings together: 
print(str1 + str2)
# You'll have to take in to account the lack of spaces:
print(str1 + " " + str2)

# STRING FORMATTING ... AT LAST! #
# ============================== #
print("STRING FORMATTING ... AT LAST!".center(50, "+"))  # Output separator
# Up until now we have used simple strings to output messages to the console, but what if we need more
# we can use the 'format' method or 'f-strings', lets start with the format method, as that should work on all versions of Python 3.
text = "Hello {}, you are {} years old!"  # some text with placeholders '{}' to be filled later.
name = input("Enter your name: ")  # ask for the users name.
birth_year = int(input("What year were you born?: "))  # ask for the users birth year
# Now that we have a 'text' string to format, and some data to format it with, 'name' & 'birth_year' lets insert them into the 'text':
print(text.format(name, 2023-birth_year))
# For each placeholder, you need to supply something to take its place.
# above 'name' slots into the first placeholder and then the answer to 2023-birthyear is placed into the second placeholder,
# and we dont have to worry about converting the answer to a string as the format method takes care of that for us, yay.
age, year, name = 33, 1990, "Bob"
print("Hello {2}, you are {0} years old making {1} your birth year!".format(age, year, name))
# Above we use the same format method, but this time we specify which bit of data goes where using an index for more control.

# And finally, my favorite formatting method, f-strings. These were introduced in Python 3.6
# RealPython.com has a recent article on some of the new f-string features: https://realpython.com/python-f-strings/

# Lets print out a f-string similar to the one above.
# F-strings allow us to place Python code directly into our text and have it evaluated at run time and be displayed.
# To create an f-string just place an 'f' before the quotation marks, similar to how we made a raw string earlier.
print(f"Hello {name.upper()}, you are {16+16+1} years old, making your birth year {2023 - age}!")
# We use curly brackets just like the 'format' method, but we can write code inside them.

# I recommend checking out the RealPython article above as it covers the Python2 modulo text formatting method
# as well as going into more detail of what we've covered here.

# QUESTIONS:
"""
Q12) Give an example of three ways to create a string.
A12) 

Q13) What is the outcome for the following code?
     print(3 * "2")
A13) 

Q14) What is the outcome of the following code?
     print(3 + "2")
A14) 

Q15) How would you capitalize each letter in the following code?
     text = "Lorem ipsum dolor sit amet."
A15) 

Q16) How can you split a string across multiple lines?
A16) 

Q17) Code a small application to ask for a name and birth year,
     then use an 'f' string to greet the user and tell them how old they are.
     This can be done in three lines of Python code, and remember you can NOT
     do math on a string.
A17)
"""
