# 2: Design a Python application that creates two threads.

# Thread 1 should calculate and display the maximum element from an list.
# Thread 2 should calculate and display the minimum element from the same list.
# The list should be accepted from the user.

import threading
from math import sqrt


def maximum(AllItem):
    maximumNumbers = AllItem[0]

    for i in AllItem:
        if i > maximumNumbers:
            maximumNumbers = i
    print("Maximum Number :",maximumNumbers)



def minimum(AllItem):
    minimumNumbers = AllItem[0]

    for i in AllItem:
        if i < minimumNumbers:
            minimumNumbers = i
    print("Minimum Number :",minimumNumbers)

    

def main():

    no = int(input("Enter Number :"))

    ItemList = []
    for _ in range(no):
        LineItem = int(input())
        ItemList.append(LineItem)


    MaxNumbList = threading.Thread(target=maximum,args=(ItemList,))    

    MinNumbList = threading.Thread(target=minimum,args=(ItemList,))    


    MaxNumbList.start()
    MinNumbList.start()

    MaxNumbList.join()
    MinNumbList.join()

if __name__ == "__main__":
    main()