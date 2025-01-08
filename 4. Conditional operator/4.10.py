'''
Write a program that determines the smallest of two numbers.
'''

def smallest_number(first_digit: int, second_digit: int) -> int:
    if first_digit < second_digit:
        return first_digit
    else:
        return second_digit

print(smallest_number(int(input()), int(input())))
