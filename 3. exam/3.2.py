'''
Schreiben Sie ein Programm, das ein Rechteck mit Sternen (*) auf dem Umfang zeigt.

Hinweis. Die Höhe und Breite des Rechtecks sind gleich 4 und 17 Sterne jeweils.

Sample Input:

Sample Output:

*****************
*               *
*               *
*****************

'''
def star_display() -> str:
    length_str = 17
    empty_space = length_str - 2
    sign = '*'
    space = ' '
    return f'{length_str * sign}\n' \
           f'{sign + space * empty_space + sign}\n' \
           f'{sign + space * empty_space + sign}\n' \
           f'{length_str * sign}'

print(star_display())
