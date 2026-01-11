class BankAccount:
    bank_name= input("HDFC Bank")
    def __init__(self,holder,balance):
        self.holder = holder
        self.balance = balance
    def deposit(self,amount):
        self.amount = amount
        if BankAccount.validate_amount(amount):
            self.balance += amount
            print(f"{amount}.{self.balance}")
        else:
            print("{amount}")
    @classmethod
    def  change_bank_name(cls,new_name):
        BankAccount.bank_name = new_name
    @staticmethod
    def validate_amount(amount):
        return amount > 0


