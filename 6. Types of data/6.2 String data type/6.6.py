'''
Write a program that reads two lines - the user’s name and first name - from the keyboard and outputs a sentence
'''
def what_your_name(name: str, surname: str) -> str:
    return f'Hello {name} {surname}! You have just delved into Python'

print(what_your_name(str(input()), str(input())))
