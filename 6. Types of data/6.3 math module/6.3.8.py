'''
The right polygon is a convex polygon where all sides and all angles between adjacent sides are equal.
Area of the right polygon on the long side a and number of sides n
'''

from math import tan, pi

def regular_polygon(n: int, a: float) -> float:
    s = (n * (a ** 2)) / (4 * tan(pi / n))

    return s

print(regular_polygon(int(input()), float(input())))
