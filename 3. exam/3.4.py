'''
As we know, integers in the language Python have no limitations that are found in other programming languages.
Write a program that reads four positive integers a, b, c, d and displays the expression
a**b + c**dAs we know, integers in the language Python have no limitations that are found in other programming languages.
Write a program that reads four positive integers a, b, c, d and displays the expression
a**b + c**d
'''

def large_digit(first_digit: int, second_digit: int, third_digit: int, fourth_digit: int) -> int:
    formula = first_digit ** second_digit + third_digit ** fourth_digit
    return formula

print(large_digit(int(input()), int(input()), int(input()), int(input())))
