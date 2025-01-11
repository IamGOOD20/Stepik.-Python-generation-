'''
Write a program that determines whether the number is even or odd.
'''
def even_or_odd_number(digit: int) -> str:
    if digit % 2 == 0:
        return 'Четное'
    else:
        return 'Нечетное'

print(even_or_odd_number(int(input())))
