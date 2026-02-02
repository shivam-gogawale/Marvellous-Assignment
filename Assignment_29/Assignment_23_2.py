# Q2) Display File Contents

# Problem Statement:
# Write a program which accepts a file name from the user, opens that file, and displays the entire contents on the console.

# Input:
# Demo.txt

# Expected Output:
# Display contents of Demo.txt on console

import os


def CheckFileExist(userFile="test.txt"):

    if os.path.exists(userFile) == False:
         print("File Not Exists in Current Directory")
         return
    
    fObj = open(userFile,"r")
    print("Content of the file is :",fObj.read())
    
def main():
    fileName = input("Entre File Name:")
    CheckFileExist(fileName)


if __name__ == "__main__":
    main()
