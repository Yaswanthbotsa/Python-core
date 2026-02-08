# 5. Consider the code below:
# nums = [[1, 2], [3, 4], [5, 6]] result = list(map(lambda x: x.append(10), nums))
# print("Result:", result) print("Nums:", nums)
# Questions
# • What will be the output of result?
# • What will be the output of nums?
# • Why does map() behave this way with list.append()?
# • How can you modify the lambda so that nums is not changed?

nums = [[1,2], [3,4], [5,6]]
result = list(map(lambda x : x.append(10),nums))
print("Results: ",result)
print("Nums: ",nums)