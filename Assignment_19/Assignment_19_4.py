# 4. Write a program which contains filter(), map() and reduce() in it. Python application which contains one list of numbers.
# List contains the numbers which are accepted from user. Filter should filter out all such numbers which are even.
# Map function will calculate its square. Reduce will return addition of all that numbers.

# Input List = [5, 2, 3, 4, 3, 4, 1, 2, 8, 10] 
# List after filter = [2, 4, 4, 2, 8, 10]
# List after map = [4, 16, 16, 4, 64, 100] 
# Output of reduce = 204

from functools import reduce

filterNumber = lambda  No: No % 2 == 0
mapNumber = lambda  No: No ** 2
ReduceNumber = lambda  No1,No2:No1 + No2 


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