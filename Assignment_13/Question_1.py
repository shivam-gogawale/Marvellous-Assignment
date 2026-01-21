# 1. Write a program which accepts length and width of rectangle and prints area.

def AreaofRectangle(Length,Width):
    return Length * Width

def main():
    Length = int(input("Enter Length :"))
    Width = int(input("Enter Width :"))
    ret = AreaofRectangle(Length,Width)

    print("Area of rectangle is",ret)

if __name__ == "__main__":
    main()