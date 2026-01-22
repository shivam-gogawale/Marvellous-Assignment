# 6. Write a lambda function which accepts one number and returns True if number is odd otherwise False.

no = int(input("Enter number : "))

evenOdd = lambda x1 : x1 % 2 != 0

ret = evenOdd(no)

print(ret)