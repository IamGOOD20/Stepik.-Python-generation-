'''
When you register on a site, you must enter the password twice. This is done for security,
as this approach reduces the possibility of incorrect password entry.

Write a program that compares password and its confirmation.
If they match, the program will output "Password accepted" (without quotation marks),
otherwise - "Password not accepted" (without quotation marks).
'''
def password(text1: str, text2: str) -> str:
    if text1 == text2:
        return 'Пароль принят'
    else:
        return 'Пароль не принят'

print(password(str(input()), str(input())))

