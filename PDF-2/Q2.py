'''Q2. Design a class Product that:
•	Maintains a base tax rate applicable to all products.
•	Each product has a name and base price.
•	Has a method to compute final price including tax.
•	Can change tax rate for all products using one method.
•	Includes a function to check whether a given price is valid or not (non-negative and realistic).
Demonstrate:
1.	Creating multiple products.
2.	Changing the tax rate.
3.	Showing updated prices and validity checks.
'''

class Product:
    base_tax_rate = 0.1
    def __init__(self,name,base_price):
        self.name = name
        self.base_price = base_price
    def final_price(self):
        final_pri = self.base_price + (self.base_price*Product.base_tax_rate)
        return final_pri
    @classmethod
    def change_tax(cls,new_rate):
        cls.base_tax_rate = new_rate
    @staticmethod
    def is_valid(price):
        return price > 0
    # def __repr__(self):
    #     return self.name,self.base_price

prod1 = Product("Remote-car",900)
prod2 = Product("Laptop",75000)

print(Product.final_price(prod1))
Product.change_tax(2.2)
print(Product.base_tax_rate)
print(Product.final_price(prod1))
print(Product.final_price(prod2))