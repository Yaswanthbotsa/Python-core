# 3. Given a list:
# nums = [12, 15, 7, 18, 20, 21, 25]
# Use filter() and lambda to keep numbers that are divisible by 3 OR divisible by
# 5 but NOT divisible by both.
# Explain how the logical condition works.

nums = [12, 15, 7, 18, 20, 21, 25]
results = list(filter(lambda n: (n % 3 == 0 or n % 5 == 0) and not (n%3 == 0 and n % 5 == 0),nums))
print(results)