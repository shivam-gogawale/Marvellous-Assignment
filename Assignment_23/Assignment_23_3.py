# 3: Write a Python program to implement a class named Numbers with the following specifications:

# The class should contain one instance variable:
# Value

# Define a constructor (init) that accepts a number from the user and initializes Value.

# Implement the following instance methods:
#   -ChkPrime() returns True if the number is prime, otherwise returns False
#   -ChkPerfect() returns True if the number is perfect, otherwise returns False
#   -Factors()- displays all factors of the number
#   -SumFactors() returns the sum of all factors
#   (You may use this method as a helper in ChkPerfect() if required)

# Create multiple objects and call all methods

from math import sqrt

class Numbers():
        def __init__(self):
          self.Value = int(input("Enter Number :"))
        
        def ChkPrime(self):
            if self.Value <= 1:
                  return False
             
            for i in range(2,int(sqrt(self.Value)) + 1):
                  if self.Value % i == 0:
                       return False
            return True

        def ChkPerfect(self):
            self.NoSum = 0
            for  i in range(1,self.Value):
                 if self.Value % i == 0:
                      self.NoSum += i

            return self.NoSum == self.Value
        
        def Factors(self):
             self.factList = []
             for i in range(1,self.Value):
                  if self.Value % i == 0:
                    self.factList.append(i)
             print("List of factor number :",self.factList)
             return self.factList

        def SumFactors(self):
             self.SumNo = 0
             for i in range(1,self.Value):
                  if self.Value % i == 0:
                    self.SumNo += i
             print("Sum of factor is",self.SumNo)

obj = Numbers()

checkPrime = obj.ChkPrime()
print("Is Prime Number :",checkPrime)

perfect = obj.ChkPerfect()
print("Is Perfect Number :",perfect)

obj.Factors()
obj.SumFactors()