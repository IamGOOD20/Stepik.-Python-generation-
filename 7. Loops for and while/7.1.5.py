'''
Write a program that prints a star rectangle in size n × 19.
'''
def star_rectangle(count: int) -> str:
    for _ in range(count):
        print('*' * 19)

star_rectangle(int(input()))

