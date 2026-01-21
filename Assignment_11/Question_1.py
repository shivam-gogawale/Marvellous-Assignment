# 1. Write a program which accepts one number and checks whether it is prime or not.

# Input: 11
# Output: Prime Number

from math import sqrt

def getPrimeNumber(no):

    for i in range(2,int(sqrt(no))+1):
        if no % i == 0:
            return False
    
    return True

def main():
    no = int(input("Enter Number : "))
    res = getPrimeNumber(no)

    if res:
        print("Prime Number")
    else:
        print("Not Prime Number")
if __name__ == "__main__":
    main()