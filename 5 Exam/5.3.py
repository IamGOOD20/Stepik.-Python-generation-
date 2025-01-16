'''
The football team recruits girls from 10 to 15 years inclusive. Write a program that asks for the age and gender of the candidate,
using the letters "m" (from male to male) and "f" (from female to female) to indicate whether or not the candidate is suitable for joining the team.
If the candidate fits, then print "YES" (without quotation marks), otherwise print "NO" (without quotation marks).
'''
def girls_only(age: int, gender: str) -> str:
    if 9 < age < 16 and gender == 'f':
        return 'YES'
    else:
        return 'NO'

print(girls_only(int(input()), str(input())))
