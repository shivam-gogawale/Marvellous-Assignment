# 1: Design a Python application that creates two separate threads named Even and Odd.

# -The Even thread should display the first 10 even numbers.
# -The Odd thread should display the first 10 odd numbers.
# -Both threads should execute independently using the threading module.
# -Ensure proper thread creation and execution

import threading

def Even():
    for i in range(2,20+1,2):
        print(i)

def Odd():
    for i in range(1,20+1,2):
        print(i)

def main():

    print("Even---------")
    t1 = threading.Thread(target=Even())
    print("Odd---------")
    t2 = threading.Thread(target=Odd())
    
    t1.start()
    t2.start()

    t1.join()
    t2.join()


if __name__ == "__main__":
    main()