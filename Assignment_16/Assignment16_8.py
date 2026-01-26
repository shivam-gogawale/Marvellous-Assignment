# 8. Write a program which accept number from user and print that number of "*" on screen.
# Input: 5
# Output: * * * * *

 
    
def main():
    
    No = int(input("Enter Number :"))

    for _ in range(No):
        print("*",end=" ")



if __name__ == "__main__":
    main()