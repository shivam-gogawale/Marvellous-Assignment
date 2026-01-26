# 6. Write a program which accept one number and display below pattern.
# Input: 5
# * * * * *
# * * * *
# * * * 
# * *
# * 


def pattern(no):
    for i in range(no,0,-1):
        row = ''
        for j in range(0,i):
            row += "* "
        print(row)
       
def main():
    no = int(input("Enter Number:"))
    pattern(no)

if __name__ == "__main__":
    main()