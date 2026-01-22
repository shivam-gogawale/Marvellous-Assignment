# 7. Write a lambda function which accepts one number and returns True if divisible by 5.

no = int(input("Enter number : "))

divisible = lambda x1 : x1 % 5 == 0

ret = divisible(no)

print(no," divisible by 5 :",ret)