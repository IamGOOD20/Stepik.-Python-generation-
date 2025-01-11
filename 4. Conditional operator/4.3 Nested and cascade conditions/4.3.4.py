'''
Write a program that classifies the triangle based on its sides length. The program should take three numbers,
each of which represents a length of one of its sides.
As a result, the program must determine whether the triangle is equilateral, equishedulred or multifaceted.
'''
def triangle_view(side_a: int, side_b: int, side_c: int) -> str:
    if side_a == side_b == side_c:
        return 'Равносторонний'
    elif side_a != side_b != side_c != side_a:
        return 'Разносторонний'
    else:
        return 'Равнобедренный'

print(triangle_view(int(input()), int(input()), int(input())))
