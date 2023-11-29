# Составить отдельный модуль mastermind_engine, реализующий функциональность 
# игры.
# В этом модуле нужно реализовать функции:
#   загадать_число()
#   проверить_число(NN) - возвращает словарь {'bulls': N, 'cows': N}
# Загаданное число хранить в глобальной переменной.
# Обратите внимание, что строки - это список символов.
# При написании кода учитывайте, что движок игры никак не должен 
# взаимодействовать с пользователем. Представьте, что движок игры могут 
# использовать разные клиенты - веб, чатбот, приложение, етс - они знают как 
# спрашивать и отвечать пользователю.Движок игры реализует только саму
# функциональность игры.
# TODO здесь ваш код...

from random import choice


def create_hidden_number() -> str:
    number_list: list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    hidden_number: str = ''
    number: str = choice(number_list[1:])
    hidden_number += number
    number_list.remove(number)
    for _ in range(3):
        number: str = choice(number_list)
        hidden_number += number
        number_list.remove(number)
    return hidden_number


def check_the_guess(guess, number=create_hidden_number()):
    answer_dict = {
        'bulls': 0,
        'cows': 0
                }
    counter = 0
    for char in guess:
        if char in number:
            if char == number[counter]:
                answer_dict['bulls'] += 1
            else:
                answer_dict['cows'] += 1
        counter += 1
    if answer_dict['bulls'] == 4:
        
        return 'Победа!'
    else:
        return answer_dict