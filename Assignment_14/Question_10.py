# 10. Write a lambda function which accepts three numbers and returns largest number

no1 = int(input("Enter first number : "))
no2 = int(input("Enter second number : "))
no3 = int(input("Enter third number : "))

largestNumber = lambda x1 , x2 , x3 : x1 if x1 >= x2 and x2 >= x3 else (x2 if x2 >= x3 else x3)

ret = largestNumber(no1,no2,no3)

print("largest number is :",ret)