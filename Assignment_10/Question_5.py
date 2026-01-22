# 5.Write a program which accepts one number and prints all odd numbers till that number

def getOddNumber(no):
    num = list()
    for i in range(1,no + 1):
        if i % 2 != 0 :
            num.append(i)

    return num

def main():
    no = int(input("Enter Number :"))
    odd = getOddNumber(no)

    print(odd)

if __name__ == "__main__":
    main()