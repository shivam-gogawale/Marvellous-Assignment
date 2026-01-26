# 1. Write a program which accept N numbers from user and store it into List. Return addition of all elements from that List.
# Input: Number of elements: 6
# Input Elements:
# 13
# 5
# 45
# 7
# 4
# 56
# Output:
# 130

def addition(ItemsArr):
    count = 0
    for i in range(len(ItemsArr)):
        count += ItemsArr[i]
    return count

def main():
    no = int(input("Enter Number :"))
    items = []
    for _ in range(no):
        userNo = int(input("Enter list item :"))
        items.append(userNo)
    print("List of Items :",items)
    ret = addition(items)

    print('Addition of list items :',ret)

if __name__ == "__main__":
    main()