'''
Write a program that calculates the sum of their modules
'''
def absolute_amount(digit1: float, digit2: float, digit3: float, digit4: float, digit5: float) -> float:
    return abs(digit1) + abs(digit2) + abs(digit3) + abs(digit4) + abs(digit5)

print(absolute_amount(float(input()), float(input()), float(input()), float(input()), float(input())))
