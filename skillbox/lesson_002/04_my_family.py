#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создайте списки:

# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
my_family = ['mom', 'dad', 'grandpa']


# список списков приблизителного роста членов вашей семьи
my_family_height = [
    ['mom', 155],
    ['dad', 178],
    ['grandpa', 169]
]

# Выведите на консоль рост отца в формате
#   Рост отца - ХХ см
print('Рост отца -', my_family_height[1][1], 'cm')
# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
#   Общий рост моей семьи - ХХ см
total_height = 0
for persons in my_family_height:
    total_height += persons[1]

print(total_height)
