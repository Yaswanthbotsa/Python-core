class Temperature:
    def __init__(self,celsius):
        self.celsius = celsius
    @staticmethod
    def to_fahrenheit(celsius):
        f = celsius * 9/5 + 32
        return f
    def show_conversion(self):
        print(f"this show c={self.celsius}, f={Temperature.to_fahrenheit(self.celsius)}")
obj = Temperature(40)
obj.show_conversion()


