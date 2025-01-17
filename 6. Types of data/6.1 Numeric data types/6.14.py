'''
Let’s call the number interesting, if it is the difference between the maximum and minimum digit equals the average of the digit.
Write a program that determines whether an interesting number or not.
If the number is interesting, you should print "Interesting" (without quotation marks),
otherwise - "Uninteresting" (without quotation marks).
'''

def interesting_digit(digit: int) -> str:

    # split digit
    first_digit = digit // 100
    middle_digit = (digit % 100) // 10
    last_digit = digit % 10

    # min med max digits
    min_digit = min(first_digit, middle_digit, last_digit)
    max_digit = max(first_digit, middle_digit, last_digit)
    medium_digit = (first_digit + middle_digit + last_digit) - (min_digit + max_digit)

    if max_digit - min_digit == medium_digit:
        return 'Число интересное'
    else:
        return 'Число неинтересное'

print(interesting_digit(int(input())))
