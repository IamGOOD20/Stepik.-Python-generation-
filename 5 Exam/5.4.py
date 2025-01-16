'''
Write a program that reads an integer and returns the corresponding Roman number. If the number is out of range [1;10],
then the program should output "error" (without quotation marks).
'''

def roman_numerals(digit: int) -> str:
    if digit < 5 and digit > 0:
        if digit == 4:
            return 'IV'
        else:
            return digit * 'I'
    elif digit > 4 and digit < 9:
        amount_of_I = digit - 5
        return f'V{"I" * amount_of_I}'
    elif digit > 8 and digit < 11:
        amount_of_I = 10 - digit
        return f'{"I" * amount_of_I}X'
    else:
        return 'ошибка'
print(roman_numerals(int(input())))


