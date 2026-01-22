# 9. Write a lambda function using reduce() which accepts a list of numbers and returns the product of all elements

from functools import reduce
def main():
    data = []
    for i in range(5):
        no = int(input("Enter Number :"))
        data.append(no)
    
    product = reduce(lambda x1 , x2 : x1 * x2,data)

    print(product)


if __name__ == "__main__":
    main()