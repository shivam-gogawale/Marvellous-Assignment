# 3. Write a lambda function which accepts two numbers and returns maximum number.

no1 = int(input("Enter a first number : "))
no2 = int(input("Enter a second number : "))

maximum = lambda x1,x2 : x1 > x2

ret = maximum(no1,no2)

if ret:
    print("Greater Number is :" ,no1)
else:
    print('Greater Number is :' ,no2)