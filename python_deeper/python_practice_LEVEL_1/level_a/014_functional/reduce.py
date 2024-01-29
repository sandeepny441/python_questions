from functools import reduce

numbers = [1, 2, 3, 4, 5]
result = reduce(lambda x, y : x + y, numbers)
print(f"Sum of the list: {result}")  # Output: Sum of the list: 15


x_list = map(lambda x: x**3, [1, 2, 4])
print(list(x_list)) # [1, 8, 64]
b = list(x_list)
print(b) # []

y = reduce(lambda x,y: x +y, list(x_list))
print(y)