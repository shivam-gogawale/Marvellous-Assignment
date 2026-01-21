# 4. Write a program which accepts one number and prints reverse of that number.

# Input: 123
# Output: 321

def reverse(no):
    count = 0
    while no > 0:
        digit = no % 10
        count = (count * 10) + digit
        no = no // 10

    return count

def main():
    no = int(input("Enter Number :")) 
    ret = reverse(no)
    print(ret)


if __name__ == "__main__":
    main()