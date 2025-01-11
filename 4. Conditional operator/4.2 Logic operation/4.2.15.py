'''
There are two different squares on the chessboard.
Write a program that determines whether the rook can be hit from the first square to the second square in one move.
The program receives four numbers of input from 1 to 8 each,
which will set the column number and the row number first for the first cell, then for the second cell.
The program should output "YES" (without quotation marks), if from the first cell a rook can be moved to the second one,
 or "NO" (without quotation marks) in the other case.
'''

def move_of_rook(current_vertical: int, current_horizontally: int,
                 next_vertical: int, next_horizontally: int) -> str:

    if (next_horizontally == current_horizontally and 1 <= next_vertical <= 8) or (
            next_vertical == current_vertical and 1 <= next_horizontally <= 8):
        return 'YES'
    else:
        return 'NO'

print(move_of_rook(int(input()), int(input()), int(input()), int(input())))
