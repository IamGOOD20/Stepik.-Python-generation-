'''
The program should output 4 number (each on a separate line) - the mean arithmetic, geometric, harmonic and quadratic.
'''

from math import sqrt

def average_values(a: float, b: float) -> str:
    arithmetic_average = (a + b) / 2
    geometric_average = sqrt(a * b)
    harmonic_average = (2 * a * b) / (a + b)
    quadratic_average = sqrt(((a ** 2) + (b ** 2)) / 2)

    return f'{arithmetic_average}\n{geometric_average}\n{harmonic_average}\n{quadratic_average}'

print(average_values(float(input()), float(input())))
