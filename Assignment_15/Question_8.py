# 8. Write a lambda function using filter() which accepts a list of numbers and returns a list of numbers divisible by both 3 and 5.

def main():
    data = []
    for i in range(5):
        no = int(input("Enter Number :"))
        data.append(no)
    
    divisible_by = list(filter(lambda x1 : x1 % 3 == 0 and x1 % 5 == 0 , data))

    print(divisible_by)


if __name__ == "__main__":
    main()