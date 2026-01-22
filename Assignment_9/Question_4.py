# 4. Write a program which accepts one number and prints cube of that number

def getCube(no):
    return no ** 3

def main():
    no = int(input("Enter Number : "))
    result = getCube(no)

    print("The Cube Is :",result)

if __name__ == "__main__":
    main()