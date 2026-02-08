# 4. Given a list:
# nums = [1, 2, 3, 4]
# Use reduce() with a lambda to compute the sum, but start with an initial value
# of 10.
# Explain how the initial value affects the reduction process.
from functools import reduce
nums = [1, 2, 3, 4]
result = reduce(lambda x,y: x + y,nums,10)
print(result)
