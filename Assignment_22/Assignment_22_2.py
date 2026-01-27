# 2: Write a Python program to implement a class named Circle with the following requirements:

# The class should contain three instance variables: Radius, Area, and Circumference.
# The class should contain one class variable named PI, initialized to 3.14.
# Define a constructor ( init ) that initializes all instance variables to 0.0.

# Implement the following instance methods:
#     -Accept() accepts the radius of the circle from the user.
#     -CalculateArea() calculates the area of the circle and stores it in the Area variable.
#     -CalculateCircumference() calculates the circumference of the circle and stores it in the Circumference variable.
#     -Display()- displays the values of Radius, Area, and Circumference.

# Create multiple objects of the Circle class and invoke all the instance methods for each object.


class Circle():
    PI = 3.14

    def __init__(self):
        self.Radius = 0.0
        self.Area = 0.0
        self.Circumference = 0.0

    
    def Accept(self):
        self.Radius = int(input("Enter Radius :"))

    def CalculateArea(self):
        self.Area = Circle.PI * (self.Radius**2)

    def CalculateCircumference(self):
        self.Circumference = 2 * (Circle.PI * self.Radius)
    def Display(self):
        print("Value of Radius :",self.Radius)
        print("Value of Area :",self.Area)
        print("Value of Circumference :",self.Circumference)



obj = Circle()
obj2 = Circle()

obj.Accept()
obj.CalculateArea()
obj.CalculateCircumference()
obj.Display()



obj2.Accept()
obj2.CalculateArea()
obj2.CalculateCircumference()
obj2.Display()