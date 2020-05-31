# Assignment 7
# Working with Binary Files & Structured Error Handling
**Dev:** *N. Tolliver*  
**Date:** *5.28.2020*

## Introduction

This assignment involves working with GitHub, demonstrating how to work with binary files using Python’s pickling module, and how to work with exception handling.    Pickling is a method of reading and writing to and from a binary file using one of Python’s built-in modules.  The syntax and the reasoning behind using pickling will be discussed.  Following that, structured error handling will be discussed.  Structured error handling provides a way for the developer to show user-friendly error messages to the user and makes the developer think of ways in which the user could “break” the program.  It can also help guide the troubleshooting process as it could provide information on where the error was encountered by treeing through various levels of structured errors with the general error being placed at the end.  Lastly, using GitHub is an integral part of this assignment, so the methodology for GitHub will also be included in this document.

## Using the Pickling Module in Python
Pickling refers to the process of converting python data into binary.  It is also known as “serialization” or “marshalling” or “flattening.”  Unpickling refers to the process of converting binary data back into a Python object.  To “pickle” or convert a Python object to binary, you call the dump() function.  To unpickle the binary data, you call the load() function.  An excellent website for explaining and providing the syntax for the pickling module is the official Python software website:  (https://docs.python.org/3/library/pickle.html, 5.30.2020, External).  This is a reliable website that can be trusted to be very accurate and updated for the most recent versions of Python.  Although it is very accurate, it can be a bit challenging for a beginner to understand.  The pickle dump and load syntax from this website is shown in Figure 1.

[Figure 1a](https://github.com/tollivne/IntroToProg-Python-Mod07/blob/master/docs/Figure%201a.png)  
[Figure 1b](https://github.com/tollivne/IntroToProg-Python-Mod07/blob/master/docs/Fibure%201b.png)

The code that I wrote to save the Python object data to a binary file is shown in Figure 2.

```
def save_data_to_file(file_name, list_of_data):
    # Now we store the data with the pickle.dump method
    objFile = open(file_name, "wb") # write binary
    pickle.dump(list_of_data, objFile)
    objFile.close
```
*Figure 2 - Saving Python Object to Binary File

The code that I wrote to read the binary data and save it to a Python object is shown in Figure 3.

```
def read_data_from_file(file_name):
    # pass  # TODO: Add code here
    # And, we read the data back with the pickle.load method
    objFile = open("AppData.dat", "rb")  # read binary
    list_of_data = pickle.load(objFile)  # Load() only loads one row of data
    objFile.close()
    return list_of_data
```
I am a big fan of video tutorials and the following video was great for explaining pickling in Python:
(https://pythonprogramming.net/python-pickle-module-save-objects-serialization/, 5.30.2020, External).  What I like about this video is that he explained pickling in the beginning much like the official website describes it and then says “Okay, so what does that mean?”  Then he explains it in plain English.  I was really wondering why you would want to pickle and/or unpickle data in the first place and he explains that too.  One of the biggest advantages that I gleaned from the video is that reading in data from a large database can be up to 50 – 100 times faster than just reading the Python data objects.  A really good example of the speed of pickled file vs. JSON file can be found on stack overflow:  (https://stackoverflow.com/questions/43056751/why-is-dumping-with-pickle-much-faster-than-json, 5.30.2020, External).  The example uses a timing command to show the time it took to dump to a json vs. a pickled file and shows the results.  Stack overflow also contains a really good write-up to help you decide if you should be using pickle (https://stackoverflow.com/questions/21752259/python-why-pickle, 5.30.2020, External).

The pickle byte file has the extension “.dat”.  Pickle is used only with Python.  A note of caution is that pickle is not secure.  It is not human readable, and the pickle file could be hacked and contain malicious code.  Care should be used if reading someone else’s pickle file or downloading pickle files from the internet.  Figure 4 shows a screenshot of the code run using a file called “ToDoFile.txt.”



### Subtopic

## Topic 2

## Summary
