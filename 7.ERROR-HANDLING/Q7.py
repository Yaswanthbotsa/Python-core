"""
• Create a class UserInput with a method get_integer(value). Handle ValueError
and TypeError using separate except blocks.
"""
from sys import exc_info


class UserInput:
    
    def __init__(self):
        self.value = None

    def get_integer(self,value):
        try:
            self.value = int(value)
            print(f"Valid Integer: {self.value}")
        except ValueError:
            self.value = value
            print(f"ValueError: '{value}' cannot be converted to integer."
                  f" Please enter a valid number")
        except TypeError:
            self.value = value
            print(f"TypeError: '{value}' is of type '{type(value).__name__}'."
                  f" Expected a string or number, not {type(value).__name__}")

    def __str__(self):
        return f"UserInput Value: {self.value}"

s = UserInput()
s.get_integer(123)
# s.get_integer([1,2,3])
print(s)
        