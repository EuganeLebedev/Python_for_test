"""
Напишите программу для слияния нескольких словарей в один.
"""
dict_1 = {1: 'One', 2: 'Two'}
dict_2 = {3: 'Three', 4: 'Four'}

dict_1.update(dict_2)
print(dict_1)

dict_1 = {1: 'One', 2: 'Two'}
dict_2 = {3: 'Three', 4: 'Four'}

result = {}
for i in (dict_1, dict_2):
    result.update(i)

print(result)


