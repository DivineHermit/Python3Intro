"""
    Python3 Introduction
    File handling.
    Written by: Dominic Lee
    Date: 07/02/2024
"""

print("FILE HANDLING".center(50, "+"))  # Output separator
# There are hundreds of different types of files, you might think of text, images, video and audio but these are just categories.
# Some examples:
# Text  : .txt, .doc
# Images: .jpg, .bmp
# Video : .mp4, .avi
# Audio : .mp3, .wav

# We'll focus on text files as Python can handle them without having to import extra modules.
# First we create a file object so we can interact with the contents:
file = open("Python3 Intro\Lorum.txt")
# If we print out te contents of our 'file' variable we'll see it doesn't contain the contents of the text document
print(file, "\n") # it contains an TextIOWrapper and the name, mode and encoding of the text file.
# The name is the filename, and possibly filepath.
# The mode is how we are interacting with the file,
#  'r' means we are reading data from the file
#  'w' means we are writing data to the file
#  'a' means we are appending to the file, this is different to writing and we'll cover the differences a little later.
# TODO: Encoding

# Now we can get all the contents out of the file using the 'read' method
text = file.read()
print(text, "\n")
# All the text in the file gets loaded into memory, so this can be an issue with large files,
# though they would have to be VERY large to cause issue on todays computers.

print("FILE METHODS".center(50, "+"))  # Output separator
[print(x) for x in dir(file) if not x.startswith("_")]  # (a list comprehension to print out all the file methods)
# TODO: File methods.

# If you've ever tried to access/move/delete a file and got a message that it is still being used
# one reason could be that it wasn't closed correctly, this used to happen a lot when an application crashed
# and the computer still thinks the file is being used.
# Since we have the data we can close the file.
file.close()

print("FILE HANDLERS".center(50, "+"))  # Output separator
# Having to open, process and close a file can be a bit long winded (But it's a good idea to know the process)
# so lets take a look at File Handlers #TODO: Terminology

# By using the keyword with we create a file handler that will automatically close the file when we are done with it.
with open("Python3 Intro\Lorum.txt") as f:
    # The file is opened and we access it by using the alias we gave it using 'as f'
    # now we can do what we want with the contents
    for line in f.readlines():
        print(line)
# When the code in the file handler is done the file is closed:
print(f"\nIs the file closed: {f.closed}")
