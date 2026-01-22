# 1. Write a program which accepts one number and prints multiplication table of that number

# Input: 4
# Output:
# 4 8 12 16 20 24 28 32 36 40


def getTable(no):
    tableList = list()
    for i in range(1,11):
        tableList.append(i * no)

    return tableList

def main():
    no = int(input("Enter Number : "))
    result = getTable(no)

    print(result)

if __name__ == "__main__":
    main()