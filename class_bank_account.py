class Bank_Account:
    def __init__(self):
        self.balance = 0
        
    def withdraw(self):
        amount = float(input("Enter amount to be Withdrawn: "))
        
        if self.balance>=amount:
                self.balance-=amount
                print("\n You Withdrew:", amount)
        else:
                print ("\n INsufficient balance ")
                
    def deposit(self):
        amount=float(input("Enter amount to be Deposited: "))
        self.balance += amount
        print ("\n Amount Deposited:", amount)
        
    def display(self):
        print("\n Net Available Balance=", self.balance)
        
# creating an object of class
s = Bank_Account()
#Calling functions with that class object
s.deposit()
s.withdraw()
s.display()

















