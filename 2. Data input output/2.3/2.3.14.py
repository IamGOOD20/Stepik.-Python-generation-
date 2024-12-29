'''
Sample Input 1:

*
Раз
Два
Три
Sample Output 1:

Раз*Два*Три
'''

def custom_separetor(sep_: str, str1: str, str2: str, str3: str) -> str:
    print(str1, str2, str3, sep=sep_)

custom_separetor(input(), input(), input(), input())


