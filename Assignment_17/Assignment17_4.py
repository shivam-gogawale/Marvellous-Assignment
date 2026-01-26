#4. Write a program which accept one number form user and return addition of its factors.
# Input: 12
# Output: 16

def factors(no):
    sum = 0
    for i in range(1,no):
        if no % i == 0:
            sum += i
    return sum            


def main():
    no = int(input("Enter Number:"))
    res = factors(no)

    print(res)

if __name__ == "__main__":
    main()