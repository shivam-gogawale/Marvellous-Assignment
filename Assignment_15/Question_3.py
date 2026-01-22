# 3. Write a lambda function using filter() which accepts a list of numbers and returns a list of odd numbers

def main():
    data = []
    for i in range(5):
        no = int(input("Enter Number :"))
        data.append(no)
    
    odd_number = list(filter(lambda x : x % 2 != 0,data))
    print(odd_number)


if __name__ == "__main__":
    main()