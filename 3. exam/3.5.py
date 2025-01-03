'''
Output format
The program should output a number n + nn + nnn.
'''
def reproduction(number: int) -> int:
    first_digit = number
    second_digit = number * 10 + number
    third_digit = number * 100 + second_digit
    formula = first_digit + second_digit + third_digit

    return formula

print(reproduction(int(input())))
