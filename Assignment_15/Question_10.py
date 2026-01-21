# 10.Write a lambda function using filter() which accepts a list of numbers and returns the count of even numbers.

from functools import reduce
def main():
    data = []
    for i in range(5):
        no = int(input("Enter Number :"))
        data.append(no)
    
    even_number = list(filter(lambda x1 :x1 % 2 ==0 ,data))

    print('Count of even number is :',len(even_number))


if __name__ == "__main__":
    main()