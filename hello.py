a = [7, 11, 23, 34, 56, 89, 1]
b = [23, 34]
result = []

result = [i for i in a if i in b]
print(result)