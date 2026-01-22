# 3. Write a program which accepts two numbers and prints addition, subtraction, multiplication and division


def addition(no1,no2):
    return no1 + no2

def subtraction(no1,no2):
    return no1 - no2

def multiplication(no1,no2):
    return no1 * no2

def division(no1,no2):
    return no1 / no2
 
def main():
    no1 = int(input("Enter first no :"))
    no2 = int(input("Enter second no :"))

    add = addition(no1,no2)
    sub = subtraction(no1,no2)
    mul = multiplication(no1,no2)
    div = division(no1,no2)

    print("Addition is :",add)
    print("Subtraction is :",sub)
    print("Multiplication is :",mul)
    print("Division is :",div)


if __name__ == "__main__":
    main()