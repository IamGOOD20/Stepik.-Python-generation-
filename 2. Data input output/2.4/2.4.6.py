'''
Write the program to display three consecutive numbers, each on a separate line.
The first number is entered by the user, the rest of the numbers you have to calculate yourself in the program.

Input format
The program is entered with a single integer.

Output format
The program should output three consecutive numbers, each on a separate line.
'''
def three_consecutive_numbers(number: int) -> int:
    print(number, number + 1, number + 2, sep='\n')

three_consecutive_numbers(int(input()))
