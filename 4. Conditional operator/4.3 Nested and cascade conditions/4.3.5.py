'''
Give three different integers. Write a program that finds the middle value of these numbers.
'''

def middle_number(first_number: int, second_digit: int, third_digit: int) -> int:
    if first_number > second_digit > third_digit or first_number < second_digit < third_digit:
        return second_digit

    elif third_digit > first_number > second_digit or third_digit < first_number < second_digit:
        return first_number
    else:
        return third_digit

print(middle_number(int(input()), int(input()), int(input())))

'''
def middle_number(first_digit: int, second_digit: int, third_digit: int) -> int:
    numbers_lst = sorted([first_digit, second_digit, third_digit])
    return numbers_lst[1]

print(middle_number(int(input()), int(input()), int(input())))
'''