# 3. Write a program which accepts one number and checks whether it is perfect number or not.

# Input: 6
# Output: Perfect Number

def perfectnumber(no):    
    sum = 0
    for i in range(1,no):
        if no % i == 0:
            sum = sum + i
            
    return sum

def main():
    Number = int(input("Enter Number :"))
    ret = perfectnumber(Number)

    if ret == Number:
        print("Perfect Number")
    else:
        print("Not Perfect Number")


if __name__ == "__main__":
    main()