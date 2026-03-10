"""
• Write a function named find_length(obj) that uses a loop to calculate the
length of the given object without using the built-in len() function. The
function should return the calculated length if the object is iterable. If a
non-iterable object such as an integer is passed, the function should raise and
handle a TypeError, and print an appropriate error message explaining what
happens when an integer is sent as input.
"""

def find_length(obj):
    try:
        c = 0
        for i in obj:
            c += 1
        return c
    except TypeError:
        print(f"TypeError: '{type(obj).__name__}' object is not iterable")

print(find_length("Hello"))
print(find_length([1,2,3,4,7,3,2,5,6]))
print(find_length((527,528,529)))
print(find_length({1,3,5,7,9}))
find_length(5)
find_length(3.14)