# 10. Write a program which accept number from user and return addition of digits in that number.
# Input: 5187934
# Output: 37


def pattern(no):
    count = 0
    while no > 0:
        count += no % 10
        no=no//10

    return count
        
def main():
    no = int(input("Enter Number:"))
    ret = pattern(no)
    print(ret)

if __name__ == "__main__":
    main()