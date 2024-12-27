'''
The entry of the program is presented with a text line - the name of the football team.
Write a program that accepts this string via the standard
input (input()) and prints the sentence in the following format:

<the name of the football team> - Champion!
where <team name> is the string of text that your program entered.

Input format
The name of the football team is shown at the entrance.

Output format
The program should output text according to the task condition.

Note 1. Use input() to read the text, and print it on screen using print().

Note 2. Note that your program runs on several tests at once. Therefore,
the solution should be universal,
meaning it should output text based on the input data that comes from your program at the start.
'''

def football(club: str) -> str:
  return print(f'{club} - champion!')

football(input())
