# 1: Design a Python application that creates two threads named Prime and NonPrime.

# -Both threads should accept a list of integers.
# -The Prime thread should display all prime numbers from the list.
# -The NonPrime thread should display all non-prime numbers from the list.

import threading
from math import sqrt


def CheckPrime(no):
    if no <= 1:
       return False
    for i in range(2,int(sqrt(no)) + 1):
        if no % i == 0:
            return False
    return True


def Prime(AllItem):
    primeItem = []
    for i in AllItem:
        if CheckPrime(i) == True:
            primeItem.append(i)
    print("List of Prime Number :",primeItem)



def NonPrime(AllItem):
     NonPrimeItem = []

     for i in AllItem:
        if CheckPrime(i) == False:
            NonPrimeItem.append(i)
     print("List of Non Prime Number :",NonPrimeItem)

    

def main():

    no = int(input("Enter Number :"))

    ItemList = []
    for _ in range(no):
        LineItem = int(input())
        ItemList.append(LineItem)


    PrimeList = threading.Thread(target=Prime,args=(ItemList,))    

    NonPrimeList = threading.Thread(target=NonPrime,args=(ItemList,))    


    PrimeList.start()
    NonPrimeList.start()

    PrimeList.join()
    NonPrimeList.join()

if __name__ == "__main__":
    main()