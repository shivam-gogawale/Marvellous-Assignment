# 3. Design a Python application that creates two threads named EvenList and OddList.

# Both threads should accept a list of integers as input.
# -The EvenList thread should:
#   Extract all even elements from the list.
#   Calculate and display their sum.
# -The OddList thread should:
#   Extract all odd elements from the list.
#   Calculate and display their sum.
# -Threads should run concurrently.

import threading

def EvenList(no):
    sum = 0
    for i in range(len(no)):
        if no[i] % 2 == 0:
            sum += no[i]
    print(sum)

def OddList(no):
    sum = 0
    for i in range(len(no)):
        if no[i] % 2 != 0:
            sum += no[i]
    print(sum)

def main():

    no = int(input("enter number :"))
    items = []
    for _ in range(no):
        userNo = int(input("Enter Number :"))
        items.append(userNo)


    print("Even---------")
    t1 = threading.Thread(target=EvenList,args=(items,))
    print("Odd---------")
    t2 = threading.Thread(target=OddList,args=(items,))
    
    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Exit from main")

if __name__ == "__main__":
    main()