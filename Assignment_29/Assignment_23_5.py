# Q5) Frequency of a String in File

# Problem Statement:
# Write a program which accepts a file name and one string from the user and returns the frequency (count of occurrences) of that string in the file.

# Input:
# Demo.txt Marvellous

# Expected Output:
# Count how many times "Marvellous" appears in Demo.txt

import os
import sys


def CountOccurrence(userFile,text):

    if os.path.exists(userFile) == False:
         print("File Not Exists in Current Directory")
         return
    
    fObj = open(userFile,'r')
    f1Content = fObj.read()
    fObj.close()
    

    print("count :",f1Content.count(text))

    
    
def main():
    if len(sys.argv) != 3:
        print("Enter 2 files name in command line")
        return
    CountOccurrence(sys.argv[1],sys.argv[2])


if __name__ == "__main__":
    main()
