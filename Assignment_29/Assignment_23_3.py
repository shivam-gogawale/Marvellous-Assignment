# Q3) Copy File Contents into a New File (Command Line)

# Problem Statement:
# Write a program which accepts an existing file name through command line arguments, creates a new file named Demo.txt,
# and copies all contents from the given file into Demo.txt.

# Input (Command Line):
# ABC.txt

# Expected Output:
# Create Demo.txt and copy contents of ABC.txt into Demo.txt

import os
import sys


def CopyContent(userFile="test.txt"):

    if os.path.exists(userFile) == False:
         print("File Not Exists in Current Directory")
         return
    
    oldFile = open(userFile,'r')
    fObj = open('Demo.txt',"w")
    fObj.write(oldFile.read())
    print("File Copy Success ")
    
def main():
    fileName = sys.argv[1]
    CopyContent(fileName)


if __name__ == "__main__":
    main()
