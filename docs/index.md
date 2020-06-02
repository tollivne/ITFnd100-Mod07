# Assignment 7
# Working with Binary Files & Structured Error Handling
**Dev:** *N. Tolliver*  
**Date:** *6.1.2020*

## Introduction

This assignment involves working with GitHub, demonstrating how to work with binary files using Python’s pickling module, and how to work with exception handling.    Pickling is a method of reading and writing to and from a binary file using one of Python’s built-in modules.  The syntax and the reasoning behind using pickling will be discussed.  Following that, structured error handling will be discussed.  Structured error handling provides a way for the developer to show user-friendly error messages to the user and makes the developer think of ways in which the user could “break” the program.  It can also help guide the troubleshooting process as it could provide information on where the error was encountered by treeing through various levels of structured errors with the general error being placed at the end.

## Using the Pickling Module in Python
Pickling refers to the process of converting python data into binary.  It is also known as “serialization” or “marshalling” or “flattening.”  Unpickling refers to the process of converting binary data back into a Python object.  To “pickle” or convert a Python object to binary, you call the dump() function.  To unpickle the binary data, you call the load() function.  An excellent website for explaining and providing the syntax for the pickling module is the official Python software website:  (https://docs.python.org/3/library/pickle.html, 5.30.2020, External).  This is a reliable website that can be trusted to be very accurate and updated for the most recent versions of Python.  Although it is very accurate, it can be a bit challenging for a beginner to understand.  The pickle dump and load syntax from this website is shown in Figure 1.

![Figure 1a](https://tollivne.github.io/IntroToProg-Python-Mod07/Figure 1a.png "Pickle Dump & Pickle Load Syntax")  
![Figure 1b](https://tollivne.github.io/IntroToProg-Python-Mod07/Fibure 1b.png "Pickle Dump & Pickle Load Syntax")  
*Figure 1 - Pickle Dump & Pickle Load Syntax*

The code that I wrote to save the Python object data to a binary file is shown in Figure 2.

```
def save_data_to_file(file_name, list_of_data):
    # Now we store the data with the pickle.dump method
    objFile = open(file_name, "wb") # write binary
    pickle.dump(list_of_data, objFile)
    objFile.close
```
*Figure 2 - Saving Python Object to Binary File*

The code that I wrote to read the binary data and save it to a Python object is shown in Figure 3.

```
def read_data_from_file(file_name):
    # And, we read the data back with the pickle.load method
    objFile = open("AppData.dat", "rb")  # read binary
    list_of_data = pickle.load(objFile)  # Load() only loads one row of data
    objFile.close()
    return list_of_data
```  
*Figure 3 - Unpickling - Reading Binary Data*

I am a big fan of video tutorials and the following video was great for explaining pickling in Python:
(https://pythonprogramming.net/python-pickle-module-save-objects-serialization/, 5.30.2020, External).  What I like about this video is that he explained pickling in the beginning much like the official website describes it and then says “Okay, so what does that mean?”  Then he explains it in plain English.  I was really wondering why you would want to pickle and/or unpickle data in the first place and he explains that too.  One of the biggest advantages that I gleaned from the video is that reading in data from a large database using pickle loading can be up to 50 – 100 times faster than just reading the Python data objects.  A really good example of the speed of pickled file vs. JSON file can be found on stack overflow:  (https://stackoverflow.com/questions/43056751/why-is-dumping-with-pickle-much-faster-than-json, 5.30.2020, External).  The example uses a timing command to show the time it took to dump to a json vs. a pickled file and shows the results.  Stack overflow also contains a really good write-up to help you decide if you should be using pickle (https://stackoverflow.com/questions/21752259/python-why-pickle, 5.30.2020, External).

The pickle byte file has the extension “.dat”.  Pickle is used only with Python.  A note of caution is that pickle is not secure.  It is not human readable, and the pickle file could be hacked and contain malicious code.  Care should be used if reading someone else’s pickle file or downloading pickle files from the internet.  Figure 4 shows a screenshot of the code run using a file called “ToDoFile.txt."  The program was expecting an object file by the name AppData.dat.

![Figure 4 - Reading & Writing Binary Data](https://tollivne.github.io/IntroToProg-Python-Mod07/Figure 4.png "Reading & Writing Binary Data")  
*Figure 4 - Reading & Writing Binary Data*

Notice the error message caused intentionally because I tried to read from a file that did not exist.  This takes us to the next subject, which is “structured error handling.”

## Structured Error Handling  

There are two types of errors in Python.  One type is the type of error that occurs when the developer is writing the program (syntax).  The other type occurs when the syntax is correct, but the program does not run correctly (run-time) errors.  A logic error is one type of run-time error in which the program runs correctly but produces the wrong output, or not what the programmer expected.  Another type of runtime error is one that causes the program to crash or stop running.  The official Python documentation website is the best source of information on Errors and Exceptions (https://docs.python.org/3/tutorial/errors.html?highlight=error%20handling, 5.30.2020, External) but can be very technical.  They Python website provides an extensive list of built-in exceptions which is a great reference for looking up exceptions to use in your code (https://docs.python.org/3/library/exceptions.html, 5.30.2020, External).  The official Python website is a good source to use as a reference if you already understand the basic concepts and just need to look up some syntax or get some clarification.

Error handling is a good way to alert the user to the fact that they may be using the program in a different way than you intended.  Instead of giving the user an error written in computereze, you can structure your code so that it gives them an error message that is more sensical.  For example, the code in Figure 5 can be used to explain to the user that the file must exist before running the program.

```
try:
    objFile = open(file_name, "rb")  # read binary

except FileNotFoundError as e:
    print("The program is intended to read from a file that already exists!")
    print("Please make sure the file by the name of :"+ file_name + " exists!")
```
*Figure 5 - Try-Except for FileNotFound Error*

When a call is intentionally made using the wrong file name, a more user-friendly error message is printed out as shown in Figure 6.

![Figure 6 - User Friendly Error Message - Part I](https://tollivne.github.io/IntroToProg-Python-Mod07/Figure 6.png "User Friendly Error Message")  
*Figure 6 - User Friendly Error Message*

The program does not stop running, it continues to the next line in the code which is pickle loading the object file.  Since the object file does not exist, and could not be opened, it generates another error, different than the FileNotFoundError. To prevent this, I wanted to exit the program at this point.  I imported the system file and used the sys.exit statement to end the program as shown Figure 7.

```
import sys
sys.exit()
```
*Figure 7 - Exiting the Program When File Is Not Found*  

So, even when there was a problem running the program, there are no more difficult to decipher error messages.

The final output has a much nicer appearance as shown in Figure 8.

![Figure 8 - Final Output of Code run with Structured Error Handling](https://tollivne.github.io/IntroToProg-Python-Mod07/Figure 8.png "Final Output of Code run with Structured Error Handling")  
*Figure 8 - Final Output of Code run with Structured Error Handling*

Lastly, a “General” exception error can be placed LAST to be invoked if the error is not caught by one of the earlier more specific errors as shown in Figure 9.

```
except Exception as e:
    print("There was a non-specific error!")
    print("Built-In Python error info: ")
    print(e, e.__doc__, type(e), sep='\n')
```
*Figure 9 - General Exception Block*

Printing the general error and type is added information that can help the developer with troubleshooting.  I also added the printing of the error, document string, and type for the FileNotFound error.  Just for contrast, shown in Figure 10 is a screenshot of the program running correctly with no errors in the CMD window.  

![Figure 10 - Program Run in CMD Window](https://tollivne.github.io/IntroToProg-Python-Mod07/Figure 10.png "Program Run in CMD Window")  
*Figure 10 - Program Run in CMD Windowg*

## Summary
In this assignment, I used Python’s pickling module with the pickle.dump and the pickle.load to write data to a binary file and then read the data and print it out.  I also used structured error handling to try to foresee the type of errors a user may get and then print out a message that is more user-friendly than the built-in Python error messages.  The assignment involved researching various sources to find more information on pickling and on error handling.  I learned that pickling was faster than reading and writing to a JSON file, I learned that Git was created by the same person who created Linux and that it is not a new tool but instead has been around since 2005.  I learned a lot about the markdown language in this assignment and was able to post the assignment to the web.  I look forward to the next assignment.

[GitHub Index File](https://tollivne.github.io/IntroToProg-Python-Mod07/)
[Link to Complete Paper in MSWord](https://github.com/tollivne/IntroToProg-Python-Mod07/blob/master/docs/Assignment07.docx)  
[Link to Python Code](https://github.com/tollivne/IntroToProg-Python-Mod07/blob/master/docs/Assignment07.py)  
[Google Homepage](https://www.google.com)  
[GitHub Webpage Code CheatSheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Sheatsheet)
