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
    towns_between = list((sites_temp.keys()))[0] + \
                        '_' + list((sites_temp.keys()))[1]
    x1 = int(list(sites_temp.values())[0][0])
    x2 = int(list(sites_temp.values())[1][0])
    y1 = int(list(sites_temp.values())[0][1])
    y2 = int(list(sites_temp.values())[1][1])
    result = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    distances.update({towns_between: int(result)})
print(distances)

