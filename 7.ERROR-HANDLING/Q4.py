"""
• Create a custom exception named InvalidAgeError. Create a class Voter with a
method check_eligibility(age) that raises this exception if age is less than 18.
"""

class InvalidAgeError(Exception):
    pass

class Voter:
    def __init__(self):
        self.age = None
    def check_eligibility(self,age):
        if age < 18 :
            raise InvalidAgeError(f"{age} is invalid! Age must be greater then 18")
        self.age = age
    def __str__(self):
        return f"The age of the person is: {self.age} - Eligible for Voting"

try:
    s = Voter()
    s.check_eligibility(int(input("Enter the age: ")))
    print(s)

except InvalidAgeError as ve:
    print(f"InvalidAgeError: {ve}")
