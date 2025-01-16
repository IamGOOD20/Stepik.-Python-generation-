'''
Write a program that accepts the number at the entry and, depending on the conditions,
outputs "YES" (without quotation marks) or "NO" (without quotation marks).

Terms:
if the number is odd, then "YES" should be used;
if a number is in the range of 2 to 5 (inclusive), then remove "NO";
if a number is in the range of 6 to 20 (inclusive), then exit "YES";
if the number is even and greater 20, then exit "NO".
'''

def yes_or_no(digit: int) -> str:
    if digit % 2 != 0 or 5 < digit < 21:
        return 'YES'
    else:
        return 'NO'

print(yes_or_no(int(input())))
