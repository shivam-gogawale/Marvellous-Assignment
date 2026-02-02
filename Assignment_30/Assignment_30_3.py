# Q3) Display File Line by Line

# Problem Statement:
# Write a program which accepts a file name from the user and displays the contents of the file line by line on the screen.

# Input:
# Demo.txt

# Expected Output:
# Display each line of Demo.txt one by one


def readLine(fName="Demo.txt"):

    fObj = open(fName,'r')

    readFile = fObj.readlines()

    for i in readFile:
        print(i)


def main():
    fileName = input("Enter File Name: ")
    readLine(fileName)


if __name__ == "__main__":
    main()