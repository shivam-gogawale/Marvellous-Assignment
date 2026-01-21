# 3. Write a program which accepts one number and prints square of that number.

# Input: 5
# Output: 25

def Square(no):
    return no ** 2

def main():
    no = int(input("Enter Number : "))
    Result = Square(no)

    print("The square is :",Result)


if __name__ == "__main__":
    main()