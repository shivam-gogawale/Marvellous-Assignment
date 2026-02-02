# Q5) Search a Word in File

# Problem Statement:
# Write a program which accepts a file name and a word from the user and checks whether that word is present in the file or not.

# Input:
# Demo.txt Marvellous

# Expected Output:
# Display whether the word Marvellous is found in Demo.txt or not



def searchText(FName="Demo.txt",text="new"):

    userFileObj = open(FName,'r')

    worldList = userFileObj.read().split()

    IsExist = list(filter(lambda x1: x1 == text,worldList))

    if len(IsExist) > 0:
        print(f"The {text} Found in {FName}")
    else:
        print(f"The {text} is Not Found in {FName}")



   


def main():
    FirstFile = input("Enter File Name: ")
    text = input("Enter Text which u want search: ")
    searchText(FirstFile,text)


if __name__ == "__main__":
    main()