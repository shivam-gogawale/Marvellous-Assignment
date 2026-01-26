
from math import sqrt

def CheckPrime(no):
    if no <= 1:
        return False

    for i in range(2,int(sqrt(no)) + 1):
        if no % i == 0:
            return False
        
    return True
