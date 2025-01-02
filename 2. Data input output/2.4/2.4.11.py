'''
Write a program that reads an integer and displays the following and previous integers in the following format:

Next to the <current number> number: <next number>
For the number <current number> previous number: <previous number>
Input format
The program is entered with a single integer.

Output format
The program should output text according to the task condition.
'''

def next_previous_number(number: int) -> str:
    custom_number = number
    previous_number = number - 1
    next_number = number + 1
    return f'Следующее за числом {custom_number} число: {next_number}\n' \
           f'Для числа {custom_number} предыдущее число: {previous_number}'

print(next_previous_number(int(input())))
