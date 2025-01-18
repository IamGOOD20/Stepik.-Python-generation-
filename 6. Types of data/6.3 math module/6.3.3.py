'''
Write a program that defines the area of the circle and the length of the circle by a given radius R.
'''

from math import pi

def area_and_length(r: float) -> str:
    s = pi * pow(r, 2)
    c = 2 * pi * r
    return f'{s}\n{c}'

print(area_and_length(float(input())))
