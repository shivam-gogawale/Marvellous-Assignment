# 5. Write a program which accept N numbers from user and store it into List.
#  Return addition of all prime numbers from that List.
#  Main python file accepts N numbers from user and pass each number to ChkPrime() function which is part of our user defined module named as MarvellousNum. 
#  Name of the function from main python file should be ListPrime().
# Input: Number of elements: 11
# Input Elements:13 5 45 7 4 56 10 34 2 5 8
# Output:
# 54 (13+5+7+2 + 5)

import MarvellousNum 

def ListPrime(items):
    sum = 0
    for i in range(len(items)):
        if MarvellousNum.CheckPrime(items[i]) == True:
            sum = sum + items[i]
    return sum

def main():
    no = int(input("Enter Number :"))
    items = []
    for _ in range(no):
        userNo = int(input("Enter list item :"))
        items.append(userNo)

    print("List of Items :",items)

    res = ListPrime(items)

    print("Addition of prime number is:",res)


if __name__ == "__main__":
    main()