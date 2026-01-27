# 2: Write a Python program to implement a class named BankAccount with the following requirements:

# The class should contain two instance variables:
#     Name (Account holder name)
#     Amount (Account balance)

# The class should contain one class variable:
#     ROI (Rate of Interest), initialized to 10.5
#     Define a constructor (_init_ ) that accepts Name and initial Amount.

# Implement the following instance methods:
#     Display() displays account holder name and current balance
#     Deposit()- accepts an amount from the user and adds it to balance
#     Withdraw() accepts an amount from the user and subtracts it from balance (Ensure withdrawal is allowed only if sufficient balance exists)
#     CalculateInterest() calculates and returns interest using formula: Interest = (Amount * ROI) / 100

# Create multiple objects and demonstrate all methods.


class BankAccount():
    ROI = 10.5
    def __init__(self,AccName,AccAmount):
        self.Name = AccName
        self.Amount = AccAmount
    
    def Display(self):
        print(f"Account Holder Name is {self.Name} and Current Balance is {self.Amount}")

    def Deposit(self):
        self.Amount = self.Amount + int(input("Enter Deposit Amount :")) 
        print("Total Balance is :", self.Amount)

    def Withdraw(self):
        self.withDrawAmt =  int(input("Enter withdraw Amount :"))
        if self.withDrawAmt > self.Amount:
            self.Amount = self.Amount - self.withDrawAmt
            print("Total Balance is :", self.Amount)
        else:
            print("Insufficient balance")
            print("You Have :", self.Amount)
        
    def CalculateInterest(self):
        return (self.Amount * BankAccount.ROI) / 100
    

obj = BankAccount("Shivam Gogawale",20000)
obj.Display()
obj.Deposit()
obj.Withdraw()
Interest = obj.CalculateInterest()

print('Interest is :',Interest)