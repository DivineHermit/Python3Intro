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
#  'a' means we are appending to the file, this is different to writing.

# The difference between 'w' writing and 'a' appending to a file is when we write to a file we are defining exactly
# what the file will contain, while when appending the data is added to hte end of the file leaving existing data intact.
# Wether writing or appending formatting you data is important as linebreaks are not automatically included.

# Now we can get all the contents out of the file using the 'read' method
text = file.read()
print(text, "\n")
# All the text in the file gets loaded into memory, so this can be an issue with large files,
# though they would have to be VERY large to cause issue on todays computers.

print("FILE METHODS".center(50, "+"))  # Output separator
[print(x) for x in dir(file) if not x.startswith("_")]  # (a list comprehension to print out all the file methods)
# Method summery from: https://www.w3schools.com/python/python_ref_file.asp
# close()	    Closes the file
# detach()	    Returns the separated raw stream from the buffer
# fileno()	    Returns a number that represents the stream, from the operating system's perspective
# flush()	    Flushes the internal buffer
# isatty()	    Returns whether the file stream is interactive or not
# read()	    Returns the file content
# readable()	Returns whether the file stream can be read or not
# readline()	Returns one line from the file
# readlines()	Returns a list of lines from the file
# seek()	    Change the file position
# seekable()	Returns whether the file allows us to change the file position
# tell()	    Returns the current file position
# truncate()	Resizes the file to a specified size
# writable()	Returns whether the file can be written to or not
# write()	    Writes the specified string to the file
# writelines()	Writes a list of strings to the file

# If you've ever tried to access/move/delete a file and got a message that it is still being used
# one reason could be that it wasn't closed correctly, this used to happen a lot when an application crashed
# and the computer still thinks the file is being used.
# Since we have the data we can close the file.
file.close()

print("CONTEXT MANAGERS".center(50, "+"))  # Output separator
# Having to open, process and close a file can be a bit long winded (But it's a good idea to know the process)
# so lets take a look at using a context manager to handle the file for us.

# By using the keyword with we create a context manger that will automatically close the file when we are done with it.
with open("Python3 Intro\Lorum.txt") as f:
    # The file is opened and we access it by using the alias we gave it using 'as f'
    # now we can do what we want with the contents
    for line in f.readlines():
        print(line)
# When the code in the context manger is done the file is closed:
print(f"\nIs the file closed: {f.closed}")
