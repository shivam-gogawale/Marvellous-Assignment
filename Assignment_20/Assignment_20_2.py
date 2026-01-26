# 2: Design a Python application that creates two threads named EvenFactor and OddFactor.

# -Both threads should accept one integer number as a parameter.
# -The EvenFactor thread should:
#   Identify all even factors of the given number.
#   Calculate and display the sum of even factors.
# -The OddFactor thread should:
#   Identify all odd factors of the given number.
#   Calculate and display the sum of odd factors.
# -After both threads complete execution, the main thread should display the message: "Exit from main"

import threading

def EvenFactor(no):
    sum = 0
    for i in range(2,no,2):
        if no % i == 0:
            sum += i
    print(sum)

def OddFactor(no):
    sum = 0
    for i in range(1,no,2):
        if no % i == 0:
            sum += i
    print(sum)

def main():

    print("Even---------")
    t1 = threading.Thread(target=EvenFactor,args=(12,))
    t1.start()
    t1.join()


    print("Odd---------")
    t2 = threading.Thread(target=OddFactor,args=(12,))
    t2.start()
    t2.join()

    print("Exit from main")

if __name__ == "__main__":
    main()