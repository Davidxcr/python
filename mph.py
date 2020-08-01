from random import randint

fuel = randint(10, 25)
miles = randint(200, 400)


calc = miles // fuel

print("The car can hold " + str(fuel) + " gallons")

print("The car can go " + str(miles) + " miles on a full tank")

print("The car can travel  " + str(calc) + " mph")