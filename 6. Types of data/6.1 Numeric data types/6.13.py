'''
Write a program that will order three numbers from the highest to the lowest.
'''

def triage_of_three(digit1: int, digit2: int, digit3: int) -> str:
    min_digit = min(digit1, digit2, digit3)
    max_digit = max(digit1, digit2, digit3)
    medium_digit = (digit1 + digit2 + digit3) - min_digit - max_digit

    return f'{max_digit}\n{medium_digit}\n{min_digit}'

print(triage_of_three(int(input()), int(input()), int(input())))
