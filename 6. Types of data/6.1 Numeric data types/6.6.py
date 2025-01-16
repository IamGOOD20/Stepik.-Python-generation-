'''
The famous American writer Ray Bradbury has a novel "451 degrees Fahrenheit".
Write a program that determines which temperature on the Celsius scale corresponds to the specified value on the Fahrenheit scale.
'''

def fahrenheit_451(fahrenheit_temperature: float) -> float:
    celsius_formula = 5 / 9 * (fahrenheit_temperature - 32)
    return celsius_formula

print(fahrenheit_451(float(input())))
