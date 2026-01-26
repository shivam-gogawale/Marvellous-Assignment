# 3. Write a program which contains one function named as Add() which accepts two numbers from user and return addition of that two numbers.

# Input: 11 5
# Output: 16

def Add(no1,no2):
    return no1 + no2

def main():
    No1 = int(input("Enter First Number :"))
    No2 = int(input("Enter Second Number :"))
    ret= Add(No1,No2)
    print(ret)

if __name__ == "__main__":
    main()