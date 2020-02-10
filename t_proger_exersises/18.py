"""
Посчитайте, сколько раз символ встречается в строке.
"""
my_string = 'This is my string'
count = 0
character_for_search = 'i'
for character in my_string:
    if character == character_for_search:
        count += 1

print(count)