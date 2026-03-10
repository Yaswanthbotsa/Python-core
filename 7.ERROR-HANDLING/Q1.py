"""
• Create a class Person whose constructor takes age as an argument. Raise a
ValueError if the age is less than 0.
"""

class Person:
    def __init__(self,age):
        if age < 0:
            raise ValueError("Age should be greater than 0")
        self.age = age
    def __str__(self):
        return f" {self.age}"
try:
    s = Person(int(input("Enter Person age: ")))
    print(f"The Person with age{s.age}")
    s1 = Person(int(input("Enter Person age: ")))
    print(f"The Person{s1} with age{s1.age}")
except ValueError as ve:
    print(f"ValueError: {ve}")


