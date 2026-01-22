# 5. Write a lambda function using reduce() which accepts a list of numbers and returns the maximum element.

from functools import reduce
def main():
    data = []
    for i in range(5):
        no = int(input("Enter Number :"))
        data.append(no)
    
    maximum = reduce(lambda x1,x2 : x1 if x1 > x2 else x2, data)
    print(maximum)


if __name__ == "__main__":
    main()