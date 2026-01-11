class Employee:
    company_name = "TechCorp"
    def __init__(self,name):
        self.name= name
    @classmethod
    def change_company(cls,new_name):
        cls.company_name = new_name
obj = Employee("yash")
obj1 = Employee("Rohith")
obj2 = Employee("Nithin")
print(f"{obj.name} : {Employee.company_name}")
print(f"{obj1.name} : {Employee.company_name}")
print(f"{obj2.name} : {Employee.company_name}")
Employee.change_company("Hcl")
print(Employee.company_name)
print(obj.company_name)
print(f"after changing the company name of {obj1.name} is : {Employee.company_name}")
