'''
Write a program that reads two integers aand b and displays the sum square (a + b) ** 2
and the sum of the squares a**2 + b**2 these numbers in the following format:

The square of sum <a> and <b> is equal to the <square of sum a and b>
The sum of squares <a> and <b> is equal to <sum of squares a and b>
Input format
Two integer numbers are submitted to the program, each on a separate line.

Output format
The program should output the text according to the condition.
'''
def square_of_sum(a: int,  b: int) -> str:
    square_sum_formula = (a + b) ** 2
    sum_of_squares_formula = (a ** 2) + (b ** 2)
    return f'Квадрат суммы {a} и {b} равен {square_sum_formula}\nСумма квадратов {a} и {b} равна {sum_of_squares_formula}'

print(square_of_sum(int(input()), int(input())))