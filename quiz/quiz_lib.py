#! /usr/bin/env python3
import random
"""
Проверка различных типов данных на примере игры в quizz
Добавлена проверка инициатора запуска 
"""

#Актуальны ли аннотации?
def ask_answer(question: str):
    answers = ('синий','Солнце')
    
    if __name__ == '__main__':
        return answers[question]
    else:
        return input('Ответ: ')

def play_quiz():
    dict_quiz_1 = {'question': 'цвет дневного неба?\n','correct_answer': 'синий','options': {'желтый', 'красный', 'черный', 'синий'}}

    dict_quiz_2 = {'question': 'Что светит ночью?\n','correct_answer': 'Солнце','options': {'Солнце', 'Луна'}}


    #Что делать, если я хочу создать коллекцию из словарей?

    questions=(dict_quiz_1, dict_quiz_2)
    #В чем ошибка в строке?
    #for i in questions:

    for question in range(2):
        print(questions[question]['question'])
        for option in questions[question]['options']:
            print(option)
        answer = ask_answer(question)
        print('\nОтвет:', answer)
        if answer.lower() == questions[question]['correct_answer'].lower():
            print('Правильно!\n')
        else:
            print('Не угадал!\n')

if __name__ == '__main__':
    play_quiz()
