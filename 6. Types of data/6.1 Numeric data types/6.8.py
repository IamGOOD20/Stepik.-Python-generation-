'''
The positive number is given. Take the first digit after the decimal point.
'''

def first_digit_after_dot(digit: float) -> int:
    return int(digit * 10) % 10

print(first_digit_after_dot(float(input())))
