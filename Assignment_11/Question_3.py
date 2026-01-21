# 3. Write a program which accepts one number and prints sum of digits.

# Input: 123
# Output: 6

def sum(no):
    count = 0
    while no > 0:
        count += no % 10
        no = no // 10

    return count

def main():
    no = int(input("Enter Number :")) 
    ret = sum(no)
    print(ret)


if __name__ == "__main__":
    main()