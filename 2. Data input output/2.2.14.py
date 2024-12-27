'''
Write a program that accepts through the standard input thread (command input()) three lines,
and then outputs them in reverse sequence, each on a separate line.

Input format
Three lines are entered at the program input, each on a separate line.

Output format
The program should show the entered lines in reverse sequence, each on a separate line.

Note 1. Use input() to read the text, and print it on screen using print().

Note 2. Note that your program runs on several tests at once. Therefore,
the solution should be universal,
meaning it should output text based on the input data that comes from your program at the start.
'''

def repeat_after_me(string1: str, string2: str, string3: str) -> str:
    return print(*reversed([string1, string2, string3]), sep='\n')

repeat_after_me(input(), input(), input())