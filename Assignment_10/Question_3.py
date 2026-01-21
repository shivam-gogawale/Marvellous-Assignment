# 3. Write a program which accepts one number and prints factorial of that number.

# Input: 5
# Output: 120


def factorial(no):
    number = no
    for i in range(1,no):
        number = number * i

    return number

def main():
    no = int(input("Enter Number :"))
    res = factorial(no)

    print("factorial is :" ,res)

if __name__ == "__main__":
    main()