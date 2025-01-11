'''
Write a program that accepts three positive numbers and determines whether a nondegenerate triangle with such sides exists.
'''

def triangle_inequality(side_a: int, side_b: int, side_c: int) -> str:
    option_1 = (side_a + side_b) > side_c
    option_2 = (side_a + side_c) > side_b
    option_3 = (side_b + side_c) > side_a

    if option_1 and option_2 and option_3:
        return 'YES'
    else:
        return 'NO'

print(triangle_inequality(int(input()), int(input()), int(input())))
