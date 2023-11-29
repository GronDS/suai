'''Вы пришли на работу в контору по разработке игр, целевая аудитория —  дети
и их родители. У прошлого программиста было задание сделать две игры в одном
приложении, чтобы пользователь мог выбирать одну из них. Однако программист, 
на место которого вы пришли, перед увольнением не успел сделать эту задачу и 
оставил только небольшой шаблон проекта. Используя этот шаблон, реализуйте
игры «Камень, ножницы, бумага» и «Угадай число».'''

import random
from time import sleep


rock: str = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
scissors: str = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
paper: str = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
signals = (rock, scissors, paper)

def ask_the_name():
    print('Привет! Как тебя зовут?')
    player_name: str = input()
    return player_name
 

def rock_paper_scissors(player_name = 'Anonym'):
    # Здесь будет игра "Камень, ножницы, бумага"
    answers: dict = {
        1: 'камень',
        2: 'ножницы',
        3: 'бумага'
    }
    
    def rps_preview():
        for signal in signals:
            print(signal)
            sleep(1)
        for second in range(3):
            print(second + 1)
            sleep(1)
    
    while True:
        computer_answer = answers[random.randint(1, 3)]
        player_answer: str = input(\
            f'{player_name}, Выбери - камень, ножницы или бумага? ').lower()
        rps_preview()
        if player_answer == computer_answer:
            print(f'Оба игрока выбрали {player_answer}. Ничья!')
            continue
        elif player_answer == answers[1]:
            if computer_answer == answers[2]:
                print('Ты выбрал камень, а я ножницы. Я победил!')
            elif computer_answer == answers[3]:
                print('Ты выбрал камень, а я бумагу. Ты победил!')
        elif player_answer == answers[2]:
            if computer_answer == answers[1]:
                print('Ты выбрал ножницы, а я камень. Я победил!')
            elif computer_answer == answers[3]:
                print('Ты выбрал ножницы, а я бумагу. Ты победил!')
        elif player_answer == answers[3]:
            if computer_answer == answers[2]:
                print('Ты выбрал бумагу, а я ножницы. Я победил!')
            elif computer_answer == answers[1]:
                print('Ты выбрал бумагу, а я камень. Ты победил!')        
        else:
            print('Некорректный ввод!')
            continue
        
        another_game: str = input('Сыграем еще раз?[Y/N]: ').lower()
        if another_game == 'y':
            rock_paper_scissors(player_name)
        else:
            break
    mainMenu()
        
        
def guess_the_number(player_name = 'Anonym'):
    # Здесь будет игра "Угадай число"
    number: int = random.randint(1, 20)
    guess: int = 0
    print(f'Хорошо, {player_name}, Я загадал число между 1 и 20.')

    for guessesTaken in range(6):
        print('Угадай.')
        guess = int(input())        
        if guess < number:
            print('Твоё число слишком маленькое.')     
        if guess > number:
            print('Твоё число слишком большое.')
        if guess == number:
            guessesTaken = guessesTaken + 1
            print(f'Хорошая работа, {player_name}! Ты отгадал моё число за \
{guessesTaken} попыток!')
            break

    if guess != number:
        print(f'Не вышло! Я загадал число {number}.' )
    
    another_game: str = input('Сыграем еще раз?[Y/N]: ').lower()
    if another_game == 'y':
        guess_the_number(player_name)
    else:
        mainMenu()
        
guess_the_number_name: tuple = (
    'угадай число', 'угадай', 'угадайка', 'guess the number', 'guess'
                                )
rock_paper_scissors_name: tuple = (
    'камень ножницы бумага', 'камень, ножницы, бумага', 'камень', 
    'rock paper scissors', 'rock, paper, scissors', 'rock'
                                    )

def mainMenu():
    # Здесь главное меню игры
    print(
'''
=====================================
============ВЫБЕРИТЕ ИГРУ============ 
=====================================
========KAMEHЬ НОЖНИЦЫ БУМАГА========
=====================================
============УГАДАЙ ЧИСЛО=============
=====================================
================ВЫХОД================
=====================================
'''
           )
    chosen_game = input('Ввод: ').lower()
    
    if chosen_game in guess_the_number_name:
        guess_the_number(ask_the_name())
    elif chosen_game in rock_paper_scissors_name:
        rock_paper_scissors(ask_the_name())
    elif chosen_game == 'выход':
        exit()
    else:
        print('Некорректный ввод!')
        mainMenu()
        
if __name__ == "__main__":
    mainMenu()