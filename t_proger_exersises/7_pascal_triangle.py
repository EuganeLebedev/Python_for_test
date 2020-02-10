"""
Нужно вывести первые n строк треугольника Паскаля.
В этом треугольнике на вершине и по бокам стоят единицы,
 а каждое число внутри равно сумме двух расположенных над ним чисел.
"""
from typing import List

triangle_pascal = []
n = 10

for i in range(n+1):
    triangle_pascal.append([1] + [0]*n)

for i in range(1, n + 1 ):
    for j in range(1, i + 1):
        triangle_pascal[i][j] = triangle_pascal[i - 1][j] + triangle_pascal[i - 1][j - 1]
        if triangle_pascal[i][j] == 0:
            triangle_pascal[i][j] = ''


for i in range(n + 1 ):
    for j in range(n + 1):
        if triangle_pascal[i][j] == 0:
            triangle_pascal[i][j] = '_'


for lines in triangle_pascal:
    print(lines

