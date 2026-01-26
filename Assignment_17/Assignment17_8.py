# 8. Write a program which accept one number and display below pattern.
# Input: 5
# 1 
# 1 2
# 1 2 3 
# 1 2 3 4
# 1 2 3 4 5



def pattern(no):
    for i in range(1,no+1):
        print()
        for j in range(1,i+1):
            print(j,end=' ')
        
def main():
    no = int(input("Enter Number:"))
    pattern(no)

if __name__ == "__main__":
    main()