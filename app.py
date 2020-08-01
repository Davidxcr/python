

celsius = int(input("Enter an integer value for degree in celsius: "))


def fahrenheit(C):
    return (float(1.8) * C + int(32))


print("The Fahrenheit equivalent of " + str(celsius) + " degree Celsius is " +str(fahrenheit(celsius)))