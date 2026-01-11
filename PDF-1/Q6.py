class Book:
    total_books = 0
    def __init__(self,title,author):
        if Book.is_valid_title(title)==True:
            self.tile = title
            self.author = author
            Book.total_books+=1
        else:
            return None
    @classmethod
    def from_string(cls,book_str):
        title,author=book_str.split("-")
        return cls(title,author)
    @staticmethod
    def is_valid_title(title):
        if len(title)>=3:
            return True
obj=Book("HarryPotter","JKRolling")
a=Book.from_string("HarryPotter-JKRolling")
print(a.tile,a.author)
print(Book.total_books)

# class MyClass:
#     # This is the class attribute (or class variable)
#     class_attribute = "I am shared by all instances"
#
#     def __init__(self, instance_data):
#         self.instance_data = instance_data
#
# # Accessing via the class
# print(MyClass.class_attribute)
#
# # Creating instances
# instance1 = MyClass("Data 1")
# instance2 = MyClass("Data 2")
#
# # Accessing via instances
# print(instance1.class_attribute)
# print(instance2.class_attribute)
#
# # Modifying via the class (affects all instances)
# MyClass.class_attribute = "I have been changed"
# print(instance1.class_attribute)
# print(instance2.class_attribute)
