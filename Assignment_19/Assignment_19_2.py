# 2. Write a program which contains one lambda function which accepts two parameters and return its multiplication.
# Input: 4 3
# Output: 12
# Input: 6 3
# Output: 18

multiplication = lambda x1,x2 : x1 * x2

def main():
    no1 = int(input("enter first number :"))
    no2 = int(input("enter second number :"))
    res = multiplication(no1,no2)
    print(res)


if __name__ == "__main__":
    main()