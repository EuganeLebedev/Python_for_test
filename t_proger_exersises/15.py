"""
Напишите программу, которая принимает два списка и выводит все элементы первого, которых нет во втором.
"""
list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list_2 = [2, 4, 6, 8, 10]
result = set(list_1) - set(list_2)
print(result)
