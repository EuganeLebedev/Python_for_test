# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd

#a = sd.get_point(0, 10)

def block(start_x=0, start_y=0, width=100, high=50, step = 1):
    start_x *= width * step
    start_y *= high
    a = sd.get_point(start_x, start_y)
    b = sd.get_point(start_x, start_y + high)
    c = sd.get_point(start_x + width, start_y + high)
    d = sd.get_point(start_x + width, start_y)
    sd.lines([a, b, c, d], color=sd.random_color())


for x in range(0, 10):
    for y in range(0, 50):
        if y % 2 != 0:
            block(x/2, y)
        else:
            block(x, y)
# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for

# TODO здесь ваш код
block()

sd.pause()
