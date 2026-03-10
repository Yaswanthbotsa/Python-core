"""
• Create a class Student with an attribute marks. Implement a method
set_marks(marks) that raises a ValueError if marks are not in the range 0 to
100.
"""

class Student:
    def __init__(self):
        self.marks = None
    def set_marks(self,marks):
        if marks < 0 or marks > 100:
            raise ValueError(f"Marks {marks} is invalid! Marks should be between 0 and 100")
        self.marks = marks
        print(f"Student Marks: {self.marks}")
    def __str__(self):
        return f"Student Marks: {self.marks}"
try:
    s = Student()
    s.set_marks(int(input("Enter marks: ")))
    print(s)
except ValueError as ve:
    print(f"ValueError:  {ve}")

