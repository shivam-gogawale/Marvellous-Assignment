# 1. Write a program which contains one lambda function which accepts one parameter and return power of two.
# Input: 4
# Output: 16

# Input: 6
# Output: 36

power = lambda x : x ** 2

def main():
    no = int(input("enter a number :"))
    res = power(no)
    print(res)


if __name__ == "__main__":
    main()