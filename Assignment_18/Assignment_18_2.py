# 2. Write a program which accept N numbers from user and store it into List. Return Maximum number from that List.
# Input: Number of elements: 7
# Input Elements: 13  5 45  7 4 56 34
# Output: 56

def max(ItemsArr):
    maxNumber = 0
    for i in range(len(ItemsArr)):
        if ItemsArr[i] > maxNumber:
            maxNumber = ItemsArr[i]
    return maxNumber

def main():
    no = int(input("Enter Number :"))
    items = []
    for _ in range(no):
        userNo = int(input("Enter list item :"))
        items.append(userNo)

    print("List of Items :",items)
    ret = max(items)

    print('Maximum of list items :',ret)

if __name__ == "__main__":
    main()