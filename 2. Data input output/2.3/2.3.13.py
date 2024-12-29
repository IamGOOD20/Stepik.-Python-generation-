'''
Write a program that welcomes the user in the following format:

Hello, <username>!
where <username> is the string that your program accepts to input via standard input (input()).

Input format
The program is entered with one line - user name.

Output format
The program should output text according to the task condition.

Note. Use the optional end parameter of the print() command.
'''

def hello(name: str) -> str:
    return print('Hello', name, sep=', ', end='!')

hello(input())
