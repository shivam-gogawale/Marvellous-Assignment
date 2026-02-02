# Q1) Count Lines in a File

# Problem Statement:
# Write a program which accepts a file name from the user and counts how many lines are present in the file.

# Input:
# Demo.txt

# Expected Output:
# Total number of lines in Demo.txt.


def getNoOfLine(fName="Demo.txt"):

    fObj = open(fName,'r')

    line = sum(1 for i in fObj)

    print(f"Total number of line in {fName} is {line}")


    

def main():
    fileName = input("Enter File Name: ")
    getNoOfLine(fileName)


if __name__ == "__main__":
    main()