# 1. Write a lambda function using map() which accepts a list of numbers and returns a list of squares of each number.

squares = lambda x : x * 2
def main():
    data = []
    for i in range(5):
        no = int(input("Enter Number :"))
        data.append(no)
    
    squares_number = list(map(squares,data))
    print(squares_number)


if __name__ == "__main__":
    main()