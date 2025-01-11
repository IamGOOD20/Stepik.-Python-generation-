'''
Write a program that determines whether the year is leap year.
If the year is a leap year, then print "YES" (without quotation marks), otherwise print "NO" (without quotation marks).

The leap year if its number is a multiple 4 but not in multiple 100, or if it is a multiple 400.
then print "YES" (without quotation marks), otherwise print "NO" (without quotation marks).

'''
def leap_year(year: int) -> str:
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return 'YES'
    else:
        return 'NO'

print(leap_year(int(input())))
