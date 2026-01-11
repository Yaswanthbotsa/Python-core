class Employee:
    bonus_rate = 0.1
    def __init__(self,name,base_salary):
        if not Employee.is_valid_salary(base_salary):
            raise ValueError("Salary Must be Greater than 0")
        self.name= name
        self.base_salary= base_salary
    def final_salary(self):
        return self.base_salary + (self.base_salary * Employee.bonus_rate)
    @classmethod
    def update_bonus(cls,new_rate):
        cls.bonus_rate = new_rate
    @staticmethod
    def is_valid_salary(sal):
        if sal > 0:
            return True
        else:
            return False

emp1 = Employee("Alice", 50000)
emp2 = Employee("Bob", 60000)

print(emp1.final_salary())
print(emp2.final_salary())

Employee.update_bonus(0.5)
print(emp1.final_salary())