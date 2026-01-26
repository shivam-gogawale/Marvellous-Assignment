# 6. Write a program which accept number from user and check whether that number is positive or negative or zero.
# Input: 11
# Output: Positive Number
# Input: -8
# Output: Negative Number
# Input: 0
# Output: Zero

def CheckNumber(No):
    if No > 0:
        return "Positive Number"
    elif No < 0:
        return 'Negative Number'
    else:
        return "Zero"

def main():
    
    No = int(input("Enter Number :"))
    ret = CheckNumber(No)

    print(ret)

if __name__ == "__main__":
    main()