'''
Write a program that reads three integers and displays their sum. Each number is written in a separate line.

Input format
Three numbers are submitted to the program, each on a separate line.
'''

def sum_of_three_numbers(num1: int, num2: int, num3: int) -> int:
    amount = num1 + num2 + num3
    return amount

print(sum_of_three_numbers(int(input()), int(input()), int(input())))
