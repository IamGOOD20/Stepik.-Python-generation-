'''
On the wheel rolls pockets numbered from 0 to 36. The following are the colors of the pockets:
pocket 0 is green; for pockets with 1 by 10 pockets with odd number have red color, pockets with even number - black;
for pockets with 11 to 18 pockets with odd number are black, pockets with even number are red;
for pockets with 19 on 28 pockets with odd number have red color, pockets with even number - black;
for pockets with 29 to 36 pockets with odd number are black, pockets with even number are red.
Write a program that reads the pocket number and shows whether the pocket is green, red or black.
The program should output an error message if the user enters a number that is outside of the range from 0 to 36.
'''

def colors_roulette_wheel(number: int) -> str:
    if number == 0:
        return 'зеленый'
    elif (number > 0 and number <= 10) or (number >= 19 and number <= 28):
        if number % 2 == 0:
            return 'черный'
        else:
            return 'красный'
    elif (number >= 11 and number <= 18) or (number >= 29 and number <= 36):
        if number % 2 == 0:
            return 'красный'
        else:
            return 'черный'
    else:
        return 'ошибка ввода'

print(colors_roulette_wheel(int(input())))
