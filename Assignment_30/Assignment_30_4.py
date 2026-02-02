# Q4) Copy File Contents into Another File

# Problem Statement:
# Write a program which accepts two file names from the user.
# First file is an existing file
# Second file is a new file
# Copy all contents from the first file into the second file.

# Input:
# ABC.txt Demo.txt

# Expected Output:
# Contents of ABC.txt copied into Demo.txt.


def CopyFile(FName="Demo.txt",SName="New.txt"):

    userFileObj = open(FName,'r')
    fObj = open(SName,'w')

    readTheFile = userFileObj.read()

    fObj.write(readTheFile)

    userFileObj.close()
    fObj.close()

    print("Success !")

   


def main():
    FirstFile = input("Enter Current File Name: ")
    SecondFile = input("Enter New File Name: ")
    CopyFile(FirstFile,SecondFile)


if __name__ == "__main__":
    main()