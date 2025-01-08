'''
Write a program that determines whether the user is allowed to access the Internet resource or not.
'''

def permit(age: int) -> str:
    if age < 18:
        return 'Доступ запрещен'
    else:
        return 'Доступ разрешен'

print(permit(int(input())))
