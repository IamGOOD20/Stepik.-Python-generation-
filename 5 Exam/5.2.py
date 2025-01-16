def chessboard(digit1: int, digit2: int, digit3: int, digit4: int) -> str:
    if (digit1 + digit2 + digit3 + digit4) % 2 == 0:
        return 'YES'
    else:
        return 'NO'
print(chessboard(int(input()), int(input()), int(input()), int(input())))
