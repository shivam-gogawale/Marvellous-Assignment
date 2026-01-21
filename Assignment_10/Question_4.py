# 4. Write a program which accepts one number and prints all even numbers till that number.

# Input: 10
# Output: 2468 10


def getEvenNumber(no):
    num = list()

    for i in range(1,no + 1):
        if i % 2 == 0:
            num.append(i)

    return num

def main():
    number = int(input("Enter Number : "))

    res = getEvenNumber(number)

    print(res)

if __name__ == "__main__":
    main()