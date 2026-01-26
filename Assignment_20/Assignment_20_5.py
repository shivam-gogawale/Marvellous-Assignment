#5: Design a Python application that creates two threads named Thread1 and Thread2.
# -Thread1 should display numbers from 1 to 50.
# -Thread2 should display numbers from 50 to 1 in reverse order.
# -Ensure that:
#   Thread2 starts execution only after Thread1 has completed.
# -Use appropriate thread synchronizatio
import threading


def getNumbers(no):
    for i in range(1,no):
        print(i)
    print("-----------")

def getReverseNumbers(no):
    for i in range(no,0,-1):
        print(i)

def main():

    orderNum = threading.Thread(target=getNumbers,args=(50,))
    orderNum.start()

    reverse = threading.Thread(target=getReverseNumbers,args=(50,))
    reverse.start()

    orderNum.join
    reverse.join()

    print("Exit from main")

if __name__ == "__main__":
    main()