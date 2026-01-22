# 9. Write a lambda function which accepts two numbers and returns multiplication

no1 = int(input("Enter first number : "))
no2 = int(input("Enter second number : "))

multiplication = lambda x1 , x2 : x1 * x2

ret = multiplication(no1,no2)

print("Multiplication is :",ret)