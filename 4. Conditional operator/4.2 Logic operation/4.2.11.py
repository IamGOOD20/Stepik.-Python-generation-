'''
Write a program that accepts integer x and determines whether the number belongs to the specified intervals.

Input format
The program is entered with an integer x.

Output format
The program should output text according to the task condition.
'''

def belonging2(digit: int) -> str:
    if -30 < digit <= -2 or 7 < digit <= 25:
        return 'Принадлежит'
    else:
        return 'Не принадлежит'

print(belonging2(int(input())))
