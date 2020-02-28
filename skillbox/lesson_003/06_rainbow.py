# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)

a_coordinates = [50, 50]
b_coordinates = [350, 450]
for colors in rainbow_colors:
    print(colors)
    a = sd.get_point(*a_coordinates)
    b = sd.get_point(*b_coordinates)
    sd.line(a, b, colors, 4)
    a_coordinates = list(map(lambda x: x+4 , a_coordinates))
    b_coordinates = list(map(lambda x: x+4, b_coordinates))

# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво
# TODO здесь ваш код

sd.pause()
