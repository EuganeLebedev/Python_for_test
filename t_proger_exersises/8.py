"""
Напишите проверку на то, является ли строка палиндромом.
Палиндром — это слово или фраза, которые одинаково читаются слева направо и справа налево.
"""
my_string = 'abba'
reversed_string = ''.join(reversed(my_string))
if my_string == reversed_string:
    print('polindrom')
else:
    print("not polindrom")