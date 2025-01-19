'''
The sentence is given and the number of times it should be repeated.
Write a program that repeats the sentence as many times as you want.
'''

def repeat_after_me_1(sentence: str, reply: int) -> str:
    for _ in range(reply):
        print(sentence)

repeat_after_me_1(str(input()), int(input()))
