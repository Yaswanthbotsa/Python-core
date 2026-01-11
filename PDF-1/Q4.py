class Car:
    wheels = 9
    def __init__(self,mileage):
        self.mileage = mileage
    def display_specs(self):
        print(self.mileage,Car.wheels)
    @classmethod
    def change_wheels(cls,new_wheels):
        cls.wheels=new_wheels
# obj = Car(40)

# print(obj.display_specs())
# Car.change_wheels(6)
# obj.display_specs()
car1 = Car(50)
print(car1)
car1.display_specs()
car1.change_wheels(2)
print(Car.wheels)