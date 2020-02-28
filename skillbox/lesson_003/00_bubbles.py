# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 600)

# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей
def three_circles():
    point = sd.get_point(100, 100)
    radius = 50
    for i in range(3):
        radius += 5
        sd.circle(center_position=point, radius=radius)

# Написать функцию рисования пузырька, принммающую 2 (или более) параметра: точка рисовании и шаг

def draw_bubble(*, point_x = 10, point_y = 10 , radius = 10, step_x = 0, step_y = 0):
    for i in range(3):
        point_x += step_x
        point_y += step_y
        point = sd.get_point(point_x, point_y)
        sd.circle(center_position=point, radius = radius)

# Нарисовать 10 пузырьков в ряд

# Нарисовать три ряда по 10 пузырьков
def draw_bubble_three_lines(*, point_x = 10, point_y = 10 , radius = 10, step_x = 0, step_y = 0):
    start_y = point_y
    for i in range(3):
        point_x += radius
        point_y = start_y
        for j in range(10):
            point_y += radius
            point = sd.get_point(point_x, point_y)
            sd.circle(center_position=point, radius = radius)

# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
# TODO здесь ваш код
def random_circles():
    for i in range(100):
        point = sd.random_point()
        width = 2
        radius = sd.random_number(a=width)
        sd.circle(center_position=point, radius=radius, color = sd.random_color(), width = width)


def main():
    three_circles()
    draw_bubble(point_x = 10, point_y = 10, radius =10,  step_x = 10)
    draw_bubble_three_lines(point_x = 10, point_y = 10, radius =10,  step_x = 10)
    random_circles()

main()


sd.pause()
