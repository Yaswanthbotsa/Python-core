"""
• Create a class PasswordValidator with a method validate(password). Raise an
exception if the password length is less than 8 characters.
"""

class PasswordValidator:
    def __init__(self):
        self.password = None
    def validate(self, password):
        if len(password) < 8:
            raise ValueError("Password must be at least 8 characters")
        self.password = password
    def __str__(self):
        return f"Password is correct : {self.password}"
try:
    s = PasswordValidator()
    s.validate(input("Enter your password: "))
    print(s)
except ValueError as ve:
    print(f"ValueError: {ve}")
