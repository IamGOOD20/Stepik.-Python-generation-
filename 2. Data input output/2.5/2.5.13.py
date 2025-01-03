'''
Geometric progression is called the sequence of numbers b1, b2,…,bn b1
​
 ,b
2
​
 ,... ,b
n
​
 , each of which starting with
b
2
b
2
​
 , is obtained by multiplying the previous number by the same constant
q
q (the denominator of the progression).

If the first member of the progression and its denominator are known, then
n
n-the geometric progression is by the formula
b n =b1 * q 7n−1
'''

def geometric_progression(b1: int, q: int, n: int) -> int:
    formula_geometric_progression = b1 * q ** (n - 1)
    return formula_geometric_progression

print(geometric_progression(int(input()), int(input()), int(input())))
