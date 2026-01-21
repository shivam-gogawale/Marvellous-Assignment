# 4. Write a program which accepts one number and prints that many numbers starting from 1.

# Input: 5
# Output: 12345

def starting(no):
    number = list()
    for i in range(1,no+1):
        number.append(i)

    return number

def main():
    no = int(input("Enter number :"))
    ret = starting(no)

    print(ret)

if __name__ == "__main__":
    main()