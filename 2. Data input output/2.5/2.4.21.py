'''
Write a program that calculates the sum and the product of positive three-digit numbers and output text in the following format:

Sum of figures = <sum of figures>
Number production = <number production>
Input format
The program is entered with a positive three-digit number.

Output format
The program should output text according to the task condition.
'''

def three_digit_number(number: int) -> str:
    first_digit = number // 100
    second_digit = (number % 100) // 10
    third_digit = number % 10
    amount_numbers = first_digit + second_digit + third_digit
    multiplication_numbers = first_digit * second_digit * third_digit
    return f'Сумма цифр = {amount_numbers}\nПроизведение цифр = {multiplication_numbers}'

print(three_digit_number(int(input())))
