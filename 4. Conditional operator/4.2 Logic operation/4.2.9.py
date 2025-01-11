'''
Approve a program that accepts integer x and determines whether the given number belongs to the specified range.

Input format
The program is entered with an integer x.

Output format
The program should output text according to the task condition.
'''

def belonging(number: int) -> str:
    if number > -1 and number < 17:
        return 'Принадлежит'
    else:
        return 'Не принадлежит'

print(belonging(int(input())))
