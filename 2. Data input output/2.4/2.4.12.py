'''
Write a program that counts the cost of three computers consisting of monitor, system unit, keyboard and mouse.

Input format
Four integer numbers (each on a separate line) are entered into the program: monitor cost, system block cost,
keyboard cost, mouse cost.

Output format
The program should output one number - purchase price (three computers).
'''

def pc_price(monitor: int, computer_case: int, keyboard: int, mouse: int) -> int:
    computer_price = monitor + computer_case + keyboard + mouse
    return computer_price * 3

print(pc_price(int(input()), int(input()), int(input()), int(input())))
