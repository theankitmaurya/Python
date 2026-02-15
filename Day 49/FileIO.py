# Python provides several ways to manipulate files.

"""
Opening a File -> Before, we can perform any operations on a file, we must open it. Python provides the open() function to open a file. It takes two arguments: the name of the file and the mode in which the file should be opened. The mode can be 'r' for reading, 'w' for writing or 'a' for appending.
"""

f = open("example.txt", 'r')
# print(f)
text = f.read()
print(text)
f.close()

"""
Modes in File -> There are various modes in which we can open files.
1. read (r): This mode can open the file for reading only and gives an error if the file does not exist. This is the default mode if no mode is passed as a parameter.
2. write (w): This mode opens the file for writing only and creates a new file if the file does not exist.
3. append (a): This mode opens the file for appending only and creates a new file if the file does not exist.
4. create (x): This mode creates a file and gives an error if the file already exists.
5. text (t): Apart from these modes we also need to specify how the file must be handled. t mode is used to handle text files. t refers to the text mode. THere is no difference between r and rt or w or wt since text mode is the default. The default mode is 'r' (open for reading text, synonym of 'rt').
6. binary (b): Used to handle binary files (images, pdfs etc).
"""

"""
Reading from a file -> Once we have a file object, we can use various methods to read from the file.
The read() method reads the entire contents of the file and returns it as a string.
"""

f = open("example.txt", 'r')
contents = f.read()
print(contents)
f.close()

"""
Writing to a file -> To write to a file, we first need to open it in write mode. We can use then write() method to write to the file.
"""

f = open("example.txt", 'w')
f.write("Hello, User!")
f.close()

"""
Append to a file -> If we want to append to a file instead of overwriting it, we can open it in append mode.
"""

f = open("example.txt", 'a')
f.write("Hello World!")
f.close()

"""
Closing a file -> It is important to close a file after we are done with it. This releases the resources used by the file and allows other programs to access it. To close a file, we can use the close() method.
"""

f = open("example.txt", 'r')
f.close()


"""
The 'with' statement -> Alternatively, we can use the with statement to automatically close the file after we are done with it.
"""

with open("example.txt", 'r') as f:
    contents = f.read()
    print(contents)
