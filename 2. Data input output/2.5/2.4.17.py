'''
Write a program to convert the value of the time interval set in minutes into a value expressed in hours and minutes in the following format:

<the initial number of minutes> minutes is <the full number of hours> hour <the remaining number of minutes>.
Input format
The program is entered with a whole number - minutes.

Output format
The program should output text according to the task’s condition.
'''

def recalculation_of_time_interval(minutes: int) -> str:
    hours, rest_minutes = minutes // 60, minutes % 60
    return f"{minutes} мин - это {hours} час {rest_minutes} минут."

print(recalculation_of_time_interval(int(input())))
