'''
Natural number submitted to programn(n ≥ 2)is a rectangular equibeastic triangle.
Write a program that will output the star triangle according to the example.
'''

def star_triangle(number: int) -> str:
    for _ in range(number):
        print(number * '*')
        number = number - 1

star_triangle(int(input()))
