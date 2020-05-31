# ------------------------------------------------------------------------ #
# Title: Assignment 07
# Description: Using the try - except for structured error handling
# ChangeLog (Who,When,What):
# N. Tolliver,5.29.2020, Created script from Assignment 06

# ------------------------------------------------------------------------ #
import sys
import pickle # This imports code from another code file!

# Data ----------------------------------------------------- #
strFileName = "ToDoFile.dat"
lstData = []

# Processing  ---------------------------------------------- #
def save_data_to_file(file_name, list_of_data):
    # Now we store the data with the pickle.dump method
    objFile = open(file_name, "wb") # write binary
    pickle.dump(list_of_data, objFile)
    objFile.close

def read_data_from_file(file_name):

    # And, we read the data back with the pickle.load method

    try:
        objFile = open(file_name, "rb")  # read binary

    except FileNotFoundError as e:
        print("The program is intended to read from a file that already exists!")
        print("Please make sure the file by the name of : "+ file_name + " exists!")
        print("To run this in the CMD window, you must navigate to the directory "
              "containing the Python program")
        print("Built-In Python error info: ")
        print(e, e.__doc__, type(e), sep='\n')
        sys.exit()

    except Exception as e:
        print("There was a non-specific error!")
        print("Built-In Python error info: ")
        print(e, e.__doc__, type(e), sep='\n')

    list_of_data = pickle.load(objFile)  # Load() ony loads one row of data
    objFile.close()
    return list_of_data

# Presentation ------------------------------------ #
# TODO: Get ID and NAME From user, then store it in a list object

strTask = str(input("Enter Task: "))
strPriority = str(input("Enter Priority: "))
lstData = [strTask, strPriority]

# TODO: store the list object into a binary file
save_data_to_file(strFileName, lstData)

# TODO: Read the data from the file into a new list object and display the contents

print(read_data_from_file(strFileName))

input()

