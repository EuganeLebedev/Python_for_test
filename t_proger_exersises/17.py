"""
Сложите цифры целого числа.
"""
number = 1234
sum_of_chars = 0

for char in str(number):
    sum_of_chars += int(char)

print(sum_of_chars)
