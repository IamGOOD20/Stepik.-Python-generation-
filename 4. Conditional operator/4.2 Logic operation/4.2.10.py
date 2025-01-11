'''
Write a program that accepts integer x and determines whether the number belongs to the specified intervals.

Input format
The program is entered with an integer x.

Output format
The program should output text according to the task condition.
'''
def belonging2(number: int) -> str:
    if number < -2 or number >= 7:
        return 'Принадлежит'
    else:
        return 'Не принадлежит'

print(belonging(int(input())))
