from custom_modules.calculation_functions import calc_pythagoras

value_a = float(input("What is the value of a?:\n"))
value_b = float(input("What is the value of b?:\n"))

result = calc_pythagoras(value_a, value_b, rounded=False)
print(result)

