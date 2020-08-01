def factorial(fac):

    returned = 1

    for item in range(fac, 1, -1):
        returned *= item

    return returned

print(factorial(3))
print(factorial(4))
print(factorial(5))