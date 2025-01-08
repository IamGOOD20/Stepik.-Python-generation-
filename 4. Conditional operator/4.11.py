'''
Write a program that defines the smallest of four numbers.
'''
# 2 5   7 10
def smallest_of_four_numbers(digit_one: int, digit_two: int, digit_three: int, digit_four: int) -> int:
    if digit_one < digit_two:
       smallest_digit_left_side = digit_one
    else:
       smallest_digit_left_side = digit_two

    if digit_three < digit_four:
        smallest_digit_right_side = digit_three
    else:
        smallest_digit_right_side = digit_four

    if smallest_digit_left_side < smallest_digit_right_side:
        return smallest_digit_left_side
    else:
        return smallest_digit_right_side

print(smallest_of_four_numbers(int(input()), int(input()), int(input()), int(input())))
