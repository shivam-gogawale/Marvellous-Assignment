# 4: Design a Python application that creates three threads named Small, Capital, and Digits.
# All threads should accept a string as input.
# The Small thread should count and display the number of lowercase characters.
# The Capital thread should count and display the number of uppercase characters.
# The Digits thread should count and display the number of numeric digits.
# Each thread must also display:
# Thread ID
# Thread Name

import threading

def CheckSmall(strItem):
    print("id of small:",threading.get_ident())
    print("Name:",threading.current_thread().name)

    sum = 0
    for i in range(len(strItem)):
        if strItem[i].islower():
            sum += 1
    print("CheckSmall",sum)
            


def CheckCapital(strItem):
    print("id of Capital:",threading.get_ident())
    print("Name:",threading.current_thread().name)

    sum = 0
    for i in range(len(strItem)):
        if strItem[i].isupper():
            sum += 1
    print("CheckCapital",sum)

def CheckDigit(strItem):
    print("id of Digit:",threading.get_ident())
    print("Name:",threading.current_thread().name)

    sum = 0
    for i in range(len(strItem)):
        if strItem[i].isdigit():
            sum += 1
    print('CheckDigit',sum)


def main():

    no = input("enter string :")
    
    print("small---------")
    small = threading.Thread(target=CheckSmall,args=(no,))
    small.start()

    print("Capital---------")
    Capital = threading.Thread(target=CheckCapital,args=(no,))
    Capital.start()

    print("Digit---------")
    Digit = threading.Thread(target=CheckDigit,args=(no,))
    Digit.start()
    

   
    small.join()
    Capital.join()
    Digit.join()

    print("Exit from main")

if __name__ == "__main__":
    main()