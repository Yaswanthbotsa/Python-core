'''Q1. Create a class Student that:
•	Keeps track of the total number of students created.
•	Determines whether a student passed or failed based on a shared passing mark.
•	Provides a method to curve marks by increasing everyone’s marks by a percentage.
•	Has a utility to convert marks (0–100) into letter grades (A, B, C, etc.).
Demonstrate:
1.	Creating multiple students.
2.	Applying a grading curve.
3.	Displaying updated results with letter grades.
'''

class Student:
    total_students = 0
    passing_marks = 40
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
        Student.total_students += 1

    def is_passed(self):
        if self.marks > Student.passing_marks:
            return "Passed"
        return "Failed"
    def curve_method(self,per):
        return self.marks+(self.marks/per)
    @staticmethod
    def grades(marks):
        if marks >= 90:
            return 'A'
        elif marks>= 80:
            return 'B'
        elif marks >= 65:
            return 'c'
        else:
            return "Fail"

stu1 = Student("Bob",51)
stu2  = Student("Will",40)
print(Student.is_passed(stu1))
print(stu1.curve_method(10))
print(Student.is_passed(stu1))
print((Student.grades(stu1.marks)))



