'''
Write a program that reads a positive integer xx and displays the number sequence x, 2x, 3x, 4x
x,2x,3x,4x and 5x, separated by three kernels -.
Input format
The program is given a positive integer xx.

Output format
The program should output text according to the task condition.
'''

def divide_and_conquer(number: int) -> str:
    custom_number = number
    custom_number_x2 = custom_number * 2
    custom_number_x3 = custom_number * 3
    custom_number_x4 = custom_number * 4
    custom_number_x5 = custom_number * 5

    return f'{custom_number}---{custom_number_x2}---{custom_number_x3}---{custom_number_x4}---{custom_number_x5}'

print(divide_and_conquer(int(input())))
