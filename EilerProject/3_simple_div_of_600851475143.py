"""
Простые делители числа 13195 - это 5, 7, 13 и 29.

Каков самый большой делитель числа 600851475143, являющийся простым числом?
"""


def simple_list():
    my_list = []
    for i in range(300):
        for j in range(2, 1 + int(i ** 0.5)):
            if not i % j:
                break
            else:
                my_list.append(i)
    print(set(my_list))

simple_list()

#def divisioner(n):
#    character_num = begin
#    while character_num < end:
#        yield chr(character_num)
#        character_num += 1
#
#for i in alphabet(97, 99):
#    print(i)
#
