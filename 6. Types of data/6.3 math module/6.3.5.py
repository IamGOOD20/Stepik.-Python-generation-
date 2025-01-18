'''
Write a program to calculate the trigonometric expression by a specified number of degrees x
'''

from math import pi, sin, cos, tan, radians, pow

def trigonometric_expression(x: float) -> float:
    r = (x * pi) / 180
    expression = sin(r) + cos(r) + pow(tan(r), 2)
    return expression

print(trigonometric_expression(float(input())))
