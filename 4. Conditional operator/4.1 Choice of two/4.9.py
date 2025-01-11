'''
Write a program that determines whether the three given numbers are (in order) consecutive members of the arithmetic progression.
'''
def arithmetic_progression(first_digit: int, second_digit: int, third_digit: int) -> str:
    if third_digit - second_digit == second_digit - first_digit:
        return 'YES'
    else:
        return 'NO'


print(arithmetic_progression(int(input()), int(input()), int(input())))
