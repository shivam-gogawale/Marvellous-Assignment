# 5. Write a program which accepts one number and prints that many numbers in reverse order.

# Input: 5
# Output: 54321

def starting(no):
    number = list()
    for i in range(no,0,-1):
        number.append(i)

    return number

def main():
    no = int(input("Enter number :"))
    ret = starting(no)

    print(ret)

if __name__ == "__main__":
    main()