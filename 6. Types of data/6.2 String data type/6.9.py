'''
Are entered 3 lines in random order.
Write a program that will find out if you can construct an arithmetic progression from the length of these lines.
'''

def arithmetic_lines(string1: str, string2: str, string3: str) -> str:
    # find min, max, medium and total strings
    total_str = len(string1) + len(string2) + len(string3)
    min_str = min(len(string1), len(string2), len(string3))
    max_str = max(len(string1), len(string2), len(string3))
    medium_str = total_str - max_str - min_str

    # comparing lenght
    if medium_str - min_str == max_str - medium_str:
        return 'YES'
    else:
        return 'NO'

print(arithmetic_lines(str(input()), str(input()), str(input()),))
