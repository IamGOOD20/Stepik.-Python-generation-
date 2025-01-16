'''
Red, blue and yellow are called the main colors because they cannot be obtained by mixing other colors.
When you mix the two main colors, you get a secondary color:

If you mix red and blue, you get purple;
if you mix red and yellow, you get orange;
If you mix blue and yellow, you get green.
Write a program that reads the names of two main colors to mix. If the user enters something other than "red",
"blue" or "yellow", the program should output an error message.
Otherwise the program must output the name of the secondary color that results.
'''

def color_mixer(color_1: str, color_2: str) -> str:
    if color_1 not in 'красный синий желтый' or color_2 not in 'красный синий желтый':
        return 'ошибка цвета'
    elif color_1 == 'красный' or color_2 == 'красный':
        if color_1 == 'синий' or color_2 == 'синий':
            return 'фиолетовый'
        elif color_1 == 'желтый' or color_2 == 'желтый':
            return 'оранжевый'
        else:
            return 'красный'
    elif color_1 == 'желтый' or color_2 == 'желтый':
        if color_1 == 'синий' or color_2 == 'синий':
            return 'зеленый'
        else:
            return 'желтый'
    else:
        return 'синий'
print(color_mixer(str(input()), str(input())))
