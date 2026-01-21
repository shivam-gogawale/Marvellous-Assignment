# 5. Write a program which accepts one number and checks whether it is divisible by 3 and 5

# Input: 15
# Output: Divisible by 3 and 5


def Divisible(no):
    if no % 3 == 0 and no % 5 == 0:
        return True
    else:
        return False

def main():
    no = int(input("Enter Number : "))

    result = Divisible(no)

    if result :
        print("Divisible by 3 and 5")
    else:
        print("Not Divisible by 3 and 5")

        


if __name__ == "__main__":
    main()