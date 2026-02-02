# Q4) Compare Two Files (Command Line)

# Problem Statement:
# Write a program which accepts two file names through command line arguments and compares the contents of both files.
# If both files contain the same contents, display Success
# Otherwise display Failure

# Input (Command Line):
# Demo.txt Hello.txt

# Expected Output:
# Success OR Failure

import os
import sys


def Compare(userFile1,userFile2):

    if (os.path.exists(userFile1) and os.path.exists(userFile2)) == False:
         print("File Not Exists in Current Directory")
         return
    
    f1 = open(userFile1,'r')
    f2 = open(userFile2,'r')

    f1Content = f1.read()
    f2Content = f2.read()

    if f1Content == f2Content:
        print("Success")
    else:
        print("Failure")
    
def main():
    if len(sys.argv) != 3:
        print("Enter 2 files")
        return
    Compare(sys.argv[1],sys.argv[2])


if __name__ == "__main__":
    main()
