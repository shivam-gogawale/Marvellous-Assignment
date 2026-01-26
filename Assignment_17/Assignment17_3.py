# 3. Write a program which accept one number from user and return its factorial.
# Input: 5
# Output: 120

def factorial(no):
    fact = 1
    for i in range(1,no + 1):
        fact = fact * i
    return fact

def main():
    no = int(input("Enter Number:"))
    res = factorial(no)

    print(res)

if __name__ == "__main__":
    main()