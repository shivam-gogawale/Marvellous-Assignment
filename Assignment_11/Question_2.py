# 2.Write a program which accepts one number and prints count of digits in that number.

# Input: 7521
# Output: 4

def countDigits(no):
    count = 0
    while no > 0:
        count += 1
        no = no // 10

    return count

def main():
    no = int(input("Enter Number :")) 
    ret = countDigits(no)
    print(ret)

if __name__ == "__main__":
    main()