'''
Write a program that tells the user which age group they belong to by the entered age:
to 13 (inclusive) - childhood;
from 14 to 24 (inclusive) - youth;
from 25 to 59 (inclusive) - maturity;
from 60 (inclusive) - old age.
'''

def age_group(age: int) -> str:
    if age < 14:
        return 'детство'
    elif 13 < age < 25:
        return 'молодость'
    elif 24 < age < 59:
        return 'зрелость'
    else:
        return 'старость'

print(age_group(int(input())))
