# 4. Write a lambda function using reduce() which accepts a list of numbers and returns the addition of all elements

from functools import reduce
def main():
    data = []
    for i in range(5):
        no = int(input("Enter Number :"))
        data.append(no)
    
    addition = reduce(lambda x1,x2 : x1 + x2, data)
    print(addition)


if __name__ == "__main__":
    main()