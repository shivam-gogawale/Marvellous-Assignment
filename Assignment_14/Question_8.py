# 8. Write a lambda function which accepts two numbers and returns addition.

no1 = int(input("Enter first number : "))
no2 = int(input("Enter second number : "))

sum = lambda x1 , x2 : x1 + x2

ret = sum(no1,no2)

print("addition is :",ret)