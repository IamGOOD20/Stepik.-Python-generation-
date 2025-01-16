'''
Write a program that reads one number from the keyboard and returns it backwards.
If the number entered with the keyboard is zero, then "Inverse number does not exist" (without quotation marks) should be returned.
'''

def inverse_number(number: float) -> float or str:
    if number == 0:
        return 'Обратного числа не существует'
    else:
        formula = 1 / number
        return formula

print(inverse_number(float(input())))
