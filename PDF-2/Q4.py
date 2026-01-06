'''
Q4. Build a Loan class that:
•	Has a common interest rate for all loans.
•	Each object stores borrower name and principal.
•	Calculates total payable amount.
•	Provides a function to update the interest rate.
•	Provides a static function to check loan eligibility (e.g., salary > certain threshold).
Demonstrate:
1.	Creating multiple loan accounts.
2.	Updating interest rates.
3.	Checking eligibility and total repayment for borrowers.
'''
class Loan:
    intrest = 8
    min_salary = 30000
    def __init__(self,name,principal):
        self.name = name
        self.pricipal = principal
    def total_payable_amount(self):
        return self.pricipal + (self.pricipal* Loan.intrest)
    @classmethod
    def change_intrest(cls,new_rate):
        cls.intrest = new_rate
    @staticmethod
    def loan_eligibility(salary):
        return salary > Loan.min_salary

l1 = Loan("El",25000)
print(l1.name,l1.pricipal)

print(l1.total_payable_amount())
print(Loan.loan_eligibility(25000))
Loan.change_intrest(9)
print(Loan.intrest)