"""
• Create a class BankAccount with an attribute balance. Implement a method
withdraw(amount) that raises an exception if the withdrawal amount is greater
than the available balance.
"""

class BankAccount:
    def __init__(self,balance):
        self.balance = balance
    def withdraw(self,amount):
        if amount > self.balance:
            raise ValueError(f"Insufficient Balance! Available amount: {self.balance}")
        self.balance -= amount
    def __str__(self):
        return f"Available Balance= {self.balance}"

try:
    s = BankAccount(int(input("Total Balance: ")))
    s.withdraw(int(input("Amount to be withdrawn: ")))
    print(s)

except ValueError as ve:
    print(ve)