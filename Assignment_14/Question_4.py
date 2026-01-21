# 4. Write a lambda function which accepts two numbers and returns minimum number.

no1 = int(input("Enter a first number : "))
no2 = int(input("Enter a second number : "))

minimum = lambda x1,x2 : x1 < x2

ret = minimum(no1,no2)

if ret:
    print("minimum Number is :" ,no1)
else:
    print('minimum Number is :' ,no2)