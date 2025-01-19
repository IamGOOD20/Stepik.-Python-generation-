'''
Natural number submitted to program n.
Write a program that for each of the numbers from 0 to n (inclusive) output text in the following format:
'''

def square_number(number: int) -> str:
    for _ in range(number + 1):
        print(f'Квадрат числа {_} равен {_ ** 2}')

square_number(int(input()))
