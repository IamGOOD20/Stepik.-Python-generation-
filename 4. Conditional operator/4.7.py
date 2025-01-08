'''
Write a program that checks the following ratio for a given four-digit number:
    the sum of the first and last digits equals the difference between the second and third digits
'''

def balance(digit: int) -> str: # 1234
    first_digit = digit // 1000
    second_digit = (digit % 1000) // 100
    third_digit = (digit % 100) // 10
    fourth_digit = digit % 10
    if first_digit + fourth_digit == second_digit - third_digit:
        return 'ДА'
    else:
        return 'НЕТ'

print(balance(int(input())))
