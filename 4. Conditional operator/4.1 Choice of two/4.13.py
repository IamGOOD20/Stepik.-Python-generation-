'''
Write a program that reads three numbers and counts the sum of positive numbers only.
'''

def only_plus(one: int, two: int, three: int) -> int:
    result = 0
    if one > 0:
        result += one
    if two > 0:
        result += two
    if three > 0:
        result += three
    return result

print(only_plus(int(input()), int(input()), int(input())))

