'''
Write a program that reads two integer numbers and a string with the keyboard.
If this string is one of four mathematical operations (+, -, *, /),
then print the result of applying this operation to previously entered numbers,
otherwise print "Incorrect operation" (without quotation marks).
If the user wants to divide by zero, print "Cannot divide by zero!" (without quotation marks).
'''

def calculator(digit_one: int, digit_two: int, sign: str) -> int or str:
    if sign == '+':
        return digit_one + digit_two
    elif sign == '-':
        return digit_one - digit_two
    elif sign == '/':
        if digit_two == 0:
            return 'На ноль делить нельзя!'
        else:
            return digit_one / digit_two
    elif sign == '*':
        return digit_one * digit_two
    else:
        return 'Неверная операция'
print(calculator(int(input()), int(input()), str(input())))
