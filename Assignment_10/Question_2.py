# 2. Write a program which accepts one number and prints sum of first N natural numbers.

# Input: 5
# Output: 15

def sum(no):
    total = 0
    for i in range(1,no+1):
        total = total + i

    return total

def main():
    no = int(input('Enter a number : '))
    result = sum(no)

    print("Sum of N numbers : ",result)

if __name__ == "__main__":
    main()