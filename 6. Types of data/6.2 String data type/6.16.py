'''
We will consider the email address as correct if it has dog (@) and dot (.).
Write a program to check the correctness of the email address.
'''

def good_mail(password: str) -> str:
    if '@' in password and '.' in password:
        return 'YES'
    else:
        return 'NO'

print(good_mail(str(input())))
