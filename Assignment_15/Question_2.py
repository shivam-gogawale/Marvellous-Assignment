# 2. Write a lambda function using filter() which accepts a list of numbers and returns a list of even numbers

even = lambda x : x % 2 == 0
def main():
    data = []
    for i in range(5):
        no = int(input("Enter Number :"))
        data.append(no)
    
    even_number = list(filter(even,data))
    
    print(even_number)


if __name__ == "__main__":
    main()