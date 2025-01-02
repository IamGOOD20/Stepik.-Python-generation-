'''
Arithmetic progression is called the sequence of numbers
a1, a2,..., an a1 ​, a2 ​
 ,...,a
n
​
 , each of which starting with
a
2
a
2
​
 , is obtained from the previous by adding to it the same constant number
d
d (the difference of progression). If you know the first member of the progression (
a
1
a
1
​
 ) and its difference (
d
d)
n
n-the arithmetic member of the progression is given by:

a
n
=
a
1
+
d
(
n
−
1
)
a
n
​
 =a
1
​
 +d(n 1)

Input
Three numbers are submitted to the program:
a
1
a
1
​
 ,
d
d and
n
n, each on a separate line.

Output
The program should output
n
n-the arithmetic member of the progression.
'''


def arithmetic_progression(a: int, d: int, n: int) -> int:
    formula_progression = a + d * (n - 1)
    return formula_progression

print(arithmetic_progression(int(input()), int(input()), int(input())))
