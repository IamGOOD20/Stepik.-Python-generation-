'''
Write a program that will output text:
    "Python is a great language!", said Fred. "I don't ever remember having this much fun before."
'''

def text() -> str:
    a = '"Python is a great language!"'
    b = ', said Fred. '
    c = '"I don\'t ever remember having this much fun before."'
    return a + b + c

print(text())