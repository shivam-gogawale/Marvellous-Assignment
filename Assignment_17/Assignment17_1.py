# 1. Create on module named as Arithmetic which contains 4 functions as Add() for addition, Sub() for subtraction,
#  Mult() for multiplication and Div() for division. All functions accepts two parameters as number and perform the operation.
#  Write on python program which call all the functions from Arithmetic module by accepting the parameters from user

import Arithmetic 
def main():
    No1 = int(input("Enter First Number :"))
    No2 = int(input("Enter Second Number :"))

    addition = Arithmetic.Add(No1,No2)
    subtraction = Arithmetic.Sub(No1,No2)
    multiplication = Arithmetic.Mult(No1,No2)
    division = Arithmetic.Add(No1,No2)

    print("Addition is :",addition)
    print("subtraction is :",subtraction)
    print("multiplication is :",multiplication)
    print("division is :",division)

if __name__ == "__main__":
    main()