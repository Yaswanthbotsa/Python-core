class Student:
    passing_marks = 40

    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def result(self):
        if self.marks >= Student.passing_marks:
            print("Pass")
        else:
            print("Fail")
    @classmethod
    def update_passing_marks(cls,new_marks):
        cls.passing_marks = new_marks
    @staticmethod
    def grade_category(marks):
        if marks >= 90:
            return "A"
        elif marks >= 70:
            return "B"
        elif marks >= 40:
            return "C"
        return "F"

stu1 = Student("Test1", 40)
stu2 = Student("Test2", 39)
print(Student.grade_category(stu1.marks))
print(Student.grade_category(stu2.marks))
stu1.result()
stu2.result()
Student.update_passing_marks(50)
print(Student.passing_marks)
stu1.result()
stu2.result()
stu1.marks = 60
stu1.result()
