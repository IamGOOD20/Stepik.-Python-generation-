'''
There are two different chess board squares.
Write a program that determines whether the king can hit from the first square to the second one.
The program receives four numbers of input from 1 to 8 each, which will set the column number and the row number first for the first cell,
then for the second cell.
The program must output "YES" (without quotation marks), if the first cell can be moved to the second one by a king move,
or "NO" (without quotation marks) otherwise.
'''

def kings_move(current_vertical: int, current_horizontally: int, next_vertical: int, next_horizontally: int) -> str:
    if (next_vertical == current_vertical or (next_vertical == current_vertical + 1 or next_vertical == current_vertical - 1)) and (
            next_horizontally == current_horizontally or (next_horizontally == current_horizontally + 1 or next_horizontally == current_horizontally - 1)):
        return 'YES'
    else:
        return 'NO'

print(kings_move(int(input()), int(input()), int(input()), int(input())))
