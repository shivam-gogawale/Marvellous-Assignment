# Q2) Count Words in a File

# Problem Statement:
# Write a program which accepts a file name from the user and counts the total number of words in that file.

# Input:
# Demo.txt

# Expected Output:
# Total number of words in Demo.txt


def getNoOfWorld(fName="Demo.txt"):

    fObj = open(fName,'r')

    readFile = fObj.read()

    fileString = readFile.split()

    print(f"Total number of words in {fName} is :{len(fileString)}")

    

def main():
    fileName = input("Enter File Name: ")
    getNoOfWorld(fileName)


if __name__ == "__main__":
    main()