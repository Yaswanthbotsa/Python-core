class Student:
    marks = 40
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def is_passed(self):
        if self.marks <= 40:
            return "Failed"
        return "Passed"
stu1 = Student("Pavani",23)
obj = Student("Yash",39)
obj.is_passed()
print(obj.is_passed())
print(stu1.is_passed())
