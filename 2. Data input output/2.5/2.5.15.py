'''
n school children share
k
k tangerines equal, the unbroken remainder remains in the basket.
How many whole tangerines will be taken to each student? How many mandorlas will be left in the basket?

Input format
The program is entered with two numbers: number of schoolchildren and number of tangerines, each in a separate row.

Output format
The program should produce two numbers: the number of mandarins that will be given to each student,
and the number of mandarins that will remain in the basket, each on a separate line.
'''

def mandarins_for_students(students: int, mandarins: int) -> str:
    for_students = mandarins // students
    rest = mandarins % students
    return f"{for_students}\n{rest}"

print(mandarins_for_students(int(input()), int(input())))
