# 5. Write a program which accept one number for user and check whether number is prime or not.
# Input: 5
# Output: It is prime number

from math import sqrt

def prime(no):
    if no <= 1:
        return 'It is not prime number'    

    for i in range(2,int(sqrt(no)) + 1):
        if no % i == 0:
            return "It is not prime number"
        
    return 'It is prime number'    

def main():
    no = int(input("Enter Number:"))
    res = prime(no)

    print(res)

if __name__ == "__main__":
    main()