# 3: Design a Python application where multiple threads update a shared variable.

# Use a Lock to avoid race conditions.
# Each thread should increment the shared counter multiple times.
# Display the final value of the counter after all threads complete execution

import threading

incrementCount = 0
lockObj = threading.Lock()

def Increment():
    global incrementCount
    for _ in range(200000):
        with lockObj:
            incrementCount = incrementCount + 1


def main():
    global incrementCount

    t1 = threading.Thread(target=Increment)
    t2 = threading.Thread(target=Increment)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Count",incrementCount)
    
if __name__ == "__main__":
    main()