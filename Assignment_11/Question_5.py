# 5. Write a program which accepts one number and checks whether it is palindrome or not.

# Input: 121
# Output: Palindrome


def palindrome(no):
    rev = 0
    while no > 0:
        digit = no % 10
        rev = (rev * 10) + digit
        no = no // 10 

    return rev

def main():
    no = int(input("Enter Number :")) 
    ret = palindrome(no)

    if ret == no:
        print('No is Palindrome')
    else:
        print('No is Not Palindrome')
        


if __name__ == "__main__":
    main()