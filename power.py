base = int(input("Enter the base: "))
exponent = int(input("Enter the exponent: "))
result = 1
for i in range(exponent):
    result = result * base

print("{0} to the power {1} is: {2}".format(base, exponent, result))