'''
Write a program that displays the number of days in this month. Accept that year is not special.
'''

def day_number(month: int) -> int:
    if month < 9 and month % 2 != 0 or month > 7 and month % 2 == 0:
        return 31
    elif month == 2:
        return 28
    else:
        return 30

print(day_number(int(input())))
