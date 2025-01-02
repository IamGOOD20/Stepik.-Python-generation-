'''
Write a program that calculates the cube volume and area of its full surface by the entered value
of the length of the rib and output the text in the following format:

Volume = <cube volume>
Area of the full surface = <cube’s total surface area>
Input format
The input of the program is a whole number - rib length.

Output format
The program should output text according to the task’s condition.

Note 1. The volume of the cube and the area of the full surface can be calculated by the following formulas:

V = a3
S = 6a2
V=a3

S=6a2


Note 2. Note that at the current stage of learning we do not know about the operator of the degree,
so we use the definition of the degree number - the number is multiplied by itself the specified number of times. For example:

a`= a ⋅ a ⋅ a ⋅ a
'''
def cube(lenght_rib: int) -> str:
    cube_volume = lenght_rib * lenght_rib * lenght_rib
    cube_square = 6 * (lenght_rib * lenght_rib)
    return f"Объем = {cube_volume}\nПлощадь полной поверхности = {cube_square}"

print(cube(int(input())))
