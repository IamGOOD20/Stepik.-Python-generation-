'''
Write a program that determines whether the year ends with this number at two zeroes.
If the year ends, type "YES" (without quotation marks), or "NO" (without quotation marks).
'''

def beginning_of_the_century(year: int) -> str:
    last_from_end_digit = year % 10
    second_from_end_digit = (year % 100) // 10
    if last_from_end_digit == 0 and second_from_end_digit == 0:
        return 'YES'
    else:
        return 'NO'

print(beginning_of_the_century(int(input())))
