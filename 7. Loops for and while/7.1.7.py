'''
Write a program that reads one line of text and outputs 10 lines numbered from 0 to 9 each, with the specified text string.
'''

def repeat_after_me2(string: str) -> str:
    for _ in range(10):
        print(_, string)

repeat_after_me2(str(input()))
