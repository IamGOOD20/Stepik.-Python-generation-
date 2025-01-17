'''
Write a program that finds the smallest and largest of the five numbers and output text in the following format:

Smallest number = <smallest number>
Highest number = <highest number>
'''

def max_amd_min(digit1: int, digit2: int, digit3: int, digit4: int, digit5: int) -> str:
    min_digit = min(digit1, digit2, digit3, digit4, digit5)
    max_digit = max(digit1, digit2, digit3, digit4, digit5)

    return f'Наименьшее число = {min_digit}\nНаибольшее число = {max_digit}'

print(max_amd_min(int(input()), int(input()), int(input()), int(input()), int(input())))
