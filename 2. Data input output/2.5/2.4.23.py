'''
Write a program to find the four-digit number.

Input format
The program input is a positive four-digit integer.

Output format
The program should output text according to the task condition.
'''

def four_digit_number(number: int) -> str:
    first_digit = number // 1000
    second_digit = (number % 1000) // 100
    third_digit = (number % 100) // 10
    fourth_digit = number % 10
    return f"Цифра в позиции тысяч равна {first_digit}\n" \
           f"Цифра в позиции сотен равна {second_digit}\n" \
           f"Цифра в позиции десятков равна {third_digit}\n" \
           f"Цифра в позиции единиц равна {fourth_digit}"

print(four_digit_number(int(input())))