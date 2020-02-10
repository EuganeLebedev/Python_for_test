"""
Напишите программу, которая принимает имя файла и выводит его расширение.
Если расширение у файла определить невозможно, выбросите исключение.
"""

import pathlib

my_file = open('12_file_to_read.txt', 'r')
print(my_file.read())

file_extension = pathlib.Path('12_file_to_read').suffix
if file_extension:
    print(file_extension)
else:
    raise Exception('No file extension found!')
