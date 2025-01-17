'''
Write a program that reads one line,
then output "YES" (without quotation marks) if the entered line has a substring of "blue",
or "NO" (without quotation marks) otherwise.
'''

def mood_color_blue(string: str) -> str:
    return 'YES' if 'синий' in string else 'NO'

print(mood_color_blue(str(input())))
