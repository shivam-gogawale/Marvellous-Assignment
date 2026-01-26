# 4. Write a program which accept N numbers from user and store it into List. Accept one another number from user and return frequency of that number from List.
# Input: Number of elements:11
# Input Elements:13 5 11 45 7 4 56 5 34 2 5 65
# Element to search : 5
# Output: 3

def frequency(ItemsArr,no):
    count = 0
    for i in range(len(ItemsArr)):
        if ItemsArr[i] == no:
            count +=1
    return count

def main():
    no = int(input("Enter Number :"))
    items = []
    for _ in range(no):
        userNo = int(input("Enter list item :"))
        items.append(userNo)

    print("List of Items :",items)
    anotherNo = int(input("Which number frequency u want :"))
    ret = frequency(items,anotherNo)

    print('Maximum of list items :',ret)

if __name__ == "__main__":
    main()