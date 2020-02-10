"""
Напишите программу, которая принимает текст и выводит два слова:
наиболее часто встречающееся и самое длинное.
"""

my_input_text = """This is my input text. I want to find in this text 
                   two most frequency words. It should be find and this"""
unique_dict = {}

for words in my_input_text.split():
    if words in unique_dict:
        unique_dict[words.lower()] += 1
    else:
        unique_dict[words.lower()] = 1

result = (sorted(unique_dict.items(), key = lambda item: item[1], reverse = True )[:2])
for word in result:
    print('Слово', word[0], 'встречается', word[1], 'раз') 
