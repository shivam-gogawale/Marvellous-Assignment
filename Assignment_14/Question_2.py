# 2. Write a lambda function which accepts one number and returns cube of that number.

no = int(input("Enter a number : "))

cube = lambda x : x ** 3

print(cube(no))