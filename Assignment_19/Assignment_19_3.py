# 3. Write a program which contains filter(), map() and reduce() in it.
# Python application which contains one list of numbers. List contains the numbers which are accepted from user.
# Filter should filter out all such numbers which greater than or equal to 70 and less than or equal to 90.
# Map function will increase each number by 10. Reduce will return product of all that numbers.

# Input List = [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70] 
# List after filter = [76, 89, 86, 90, 70] 
# List after map = [86, 99, 96, 100, 80]
# Output of reduce = 6538752000

from functools import reduce

filterNumber = lambda  No: No >= 70 and No <= 90
mapNumber = lambda  No: No + 10
ReduceNumber = lambda  No1,No2:No1 * No2 


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