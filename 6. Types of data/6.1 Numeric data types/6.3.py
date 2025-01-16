'''
Write a program that reads the length of two wheels in a rectangular triangle and returns its area.
'''

def triangle_square(cathetus1: int, cathetus2: int) -> float:
    formula_triangle_square = float(1/2 * cathetus1 * cathetus2)
    return formula_triangle_square

print(triangle_square(float(input()), float(input())))
