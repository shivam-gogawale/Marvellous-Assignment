# Q1) Check File Exists in Current Directory

# Problem Statement:
# Write a program which accepts a file name from the user and checks whether that file exists in the current directory or not.

# Input:
# Demo.txt

# Expected Output:
# Display whether Demo.txt exists or not.

import os


def CheckFileExist(userFile="test.txt"):

    if os.path.exists(userFile) == True:
         print("File Exists in Current Directory")
    else:
         print("File Not Exists in Current Directory")
    
    
def main():
    fileName = input("Entre File Name:")
    CheckFileExist(fileName)


if __name__ == "__main__":
    main()
