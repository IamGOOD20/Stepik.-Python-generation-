'''
Назовём число красивым, если оно является четырёхзначным и делится нацело на
7
7 или на
17
17. Напишите программу, определяющую, является ли введённое число красивым. Программа должна вывести «YES» (без кавычек),
если число является красивым, или «NO» (без кавычек) в противном случае.
'''

def beautiful_digit(digit: int) -> str:
    if 9999 > digit > 999:
        if digit % 7 == 0 or digit % 17 == 0:
            return 'YES'
        else:
            return 'NO'
    else:
        return 'NO' # 'The digit is not beautiful'

print(beautiful_digit(int(input())))
