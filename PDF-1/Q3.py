class MathOps:
    @staticmethod
    def is_even(num):
        if num % 2 == 0:
            return "Even"
        return "Odd"
# MathOps.is_even(2)
# obj = MathOps()
# obj.is_even(3)
# print(obj.is_even(3))

num1 = MathOps.is_even(4)
print(num1)