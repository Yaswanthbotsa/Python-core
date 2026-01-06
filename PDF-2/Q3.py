'''Q3. Create an Employee class that:
•	Keeps a minimum experience required for promotion (shared across all employees).
•	Stores employee name, experience, and department.
•	Has a method to check eligibility for promotion.
•	Provides a function to update promotion criteria globally.
•	Offers a general tool that checks if a given department is valid (like “HR”, “Tech”, “Admin”).
Demonstrate:
1.	Creating employees from different departments.
2.	Changing promotion criteria.
3.	Displaying eligibility results and department validation.
'''
class Employee:
    min_experience = 4
    dept_list = ["HR","Tech","Admin"]
    def __init__(self,name,experience,department):
        self.name = name
        self.experience = experience
        self.department = department
    def check(self):
        return self.experience >= Employee.min_experience
    @classmethod
    def change_prom(cls,new_exp):
        cls.min_experience = new_exp
    @staticmethod
    def department_in(dept):
        if dept in Employee.dept_list:
            return True
        return False

emp1 = Employee("Mike",6,"Tech")
print(emp1.check())
print(Employee.department_in(emp1.department))
Employee.change_prom(8)
print(Employee.min_experience)
