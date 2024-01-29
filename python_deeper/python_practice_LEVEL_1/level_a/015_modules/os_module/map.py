def cubes(x):
    return x ** 3 

numbers = [1, 2, 3, 4, 5]
result = list(map(cubes, numbers))
print(result)


numbers = [1, 2, 3, 4, 5]
result = list(map(lambda x:x**3, numbers))
print(result)


numbers = [1, 2, 3, 4, 5]
result = list(map(lambda x:str(x), numbers))
print(result)

words = ['apple', 'banana', 'cherry', 'date']
result = list(map(lambda x: len(x), words))
print(result)