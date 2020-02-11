#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь координат городов

sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - корень из (x1 - x2) ** 2 + (y1 - y2) ** 2

distances = {}

# TODO здесь заполнение словаря
for town in sites:
    sites_temp = sites.copy()
    sites_temp.pop(town) 
#    distence = (sites_temp[0][0] - sites_temp[1][0]) ** 2
#    + (sites_temp[1][0] - sites_temp[1][1]) ** 2
#    distances.update({1: 1})
    print(list(sites_temp.values())[0][0])

print(distances)
