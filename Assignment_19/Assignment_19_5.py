# 5. Write a program which contains filter(), map() and reduce() in it. Python application which contains one list of numbers.
# List contains the numbers which are accepted from user. Filter should filter out all prime numbers.
# Map function will multiply each number by 2. Reduce will return Maximum number from that numbers. 
# (You can also use normal functions instead of lambda functions).

# Input List = [2, 70, 11, 10, 17, 23, 31, 77]
# List after filter = [2, 11, 17, 23, 31] 
# List after map = [4, 22, 34, 46, 62] 
# Output of reduce = 62

from math import sqrt
from functools import reduce
 
def filterNumber(no):
    if no <= 1:
        return False
    for i in range(2,int(sqrt(no) + 1)):
        if no % i == 0:
            return False
    return True

mapNumber = lambda  No: No * 2
# ReduceNumber = lambda  No1,No2:No1 > No2 

def ReduceNumber(no1,no2):
    if no1 > no2:
        no2 = no1
    return no2

def main():
    no = int(input("enter number :"))
    items = []
    for _ in range(no):
        userNo = int(input("Enter Number :"))
        items.append(userNo)

    print("Input List ",items)

    FilterData = list(filter(filterNumber,items))
    mapData = list(map(mapNumber,FilterData))
    reduceData = reduce(ReduceNumber,mapData)


    print('List after filter',FilterData)
    print('List after map',mapData)
    print("Output of reduce :",reduceData)

if __name__ == "__main__":
    main()