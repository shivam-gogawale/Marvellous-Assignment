# 4: Design a Python application that creates two threads.

# -Thread 1 should compute the sum of elements from a list.
# -Thread 2 should compute the product of elements from the same list.
# -Return the results to the main thread and display them.


import threading
 

def sumOfItem(AllItem,result):
    add = 0
    for i in AllItem:
       add = i + add
    result["SumNum"] = add

def productOfItem(AllItem,result):
    product = 1
    for i in AllItem:
        product = i * product
    result["product"] = product

def main():
    result = {
        "SumNum":0,
        "product":0
    }

    no = int(input("Enter Number :"))
    ItemList = []
    for _ in range(no):
        listItem = int(input())
        ItemList.append(listItem)


    sumItem = threading.Thread(target=sumOfItem,args=(ItemList,result,))
    productItem = threading.Thread(target=productOfItem,args=(ItemList,result,))

    sumItem.start()
    productItem.start()

    sumItem.join()
    productItem.join()

    print("Sum",result["SumNum"])
    print("product",result["product"])
    
if __name__ == "__main__":
    main()