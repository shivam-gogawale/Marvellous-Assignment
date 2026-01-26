# 2. Write a program which accept one number and display below pattern.

# Input: 5
# Output:
# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *

def displayPattern(no):
    for i in range(no):
        row = ''
        for j in range(no):
            row += "* "
        print(row)


def main():
    no = int(input("Enter Number:"))
    displayPattern(no)

if __name__ == "__main__":
    main()