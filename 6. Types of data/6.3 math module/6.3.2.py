'''
Write a program that defines the Euclidean distance between two points whose coordinates are given.
'''

from math import pow, sqrt
def euclidean_distance(x1: float, y1: float, x2: float, y2: float) -> float:
    euclidean_formula = sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2))
    return euclidean_formula

print(euclidean_distance(float(input()), float(input()), float(input()), float(input())))