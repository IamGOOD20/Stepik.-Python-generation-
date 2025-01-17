'''
Write a program that reads one line, then returns "YES" (without quotation marks),
if the entered line has a substring of "Saturday" or "Sunday", or "NO" (without quotation marks) otherwise.
'''
def rest_or(string: str) -> str:
    return 'YES' if 'суббота' in string or 'воскресенье' in string else 'NO'

print(rest_or(str(input())))
