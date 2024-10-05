class BankAccount:
    def __init__(self, balance=0.00):
        self.balance = float(balance)
    def deposit(self, amount):
         self.balance =+ float(amount)
         return True
    def withdraw(self, amount):
        if (self.balance>=float(amount)):
             self.balance -= float(amount)
             return True
        else : 
             return False
    def display_balance(self):
         print(f"Current Balance: ${self.balance:.2f}")

 