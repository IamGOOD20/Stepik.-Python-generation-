'''
Write a program that finds the full number of meters by the specified number of centimeters.

Input format
The program is entered with a natural number - the number of centimeters.

Output format
The program should output one number - full number of meters.
'''
def distance_in_metres(centimeters: int) -> int:
    cantimeters_in_metres = centimeters // 100
    return cantimeters_in_metres

print(distance_in_metres(int(input())))
