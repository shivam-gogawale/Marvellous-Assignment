# 3. Write a program which accept N numbers from user and store it into List. Return Minimum number from that List.
# Input: Number of elements: 4
# Input Elements: 13 5 45 7
# Output: 5

def min(ItemsArr):
    minNumber = ItemsArr[0]
    for i in range(len(ItemsArr)):
        if ItemsArr[i] < minNumber:
            minNumber = ItemsArr[i]
    return minNumber

def main():
    no = int(input("Enter Number :"))
    items = []
    for _ in range(no):
        userNo = int(input("Enter list item :"))
        items.append(userNo)

    print("List of Items :",items)
    ret = min(items)

    print('Maximum of list items :',ret)

if __name__ == "__main__":
    main()