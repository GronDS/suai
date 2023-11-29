'''Степан, как и большая часть населения планеты, для арифметический расчетов 
чисел использует калькулятор. Однако в работе ему нужно совершать не только 
обычные действия вроде сложения и вычитания, а делать что-то вручную он уже 
устал. Поэтому Степан решил немного расширить функционал своего калькулятора.
    Напишите программу, запрашивающую у пользователя число и действие, которое 
нужно с ним сделать. Каждое действие оформите в виде отдельной функции, а 
основную программу зациклите.
'''

def addition(first_number):
    second_number = float(input('Введите второе слогаемое: '))
    print(f'Результат: {first_number + second_number}')
def subtraction(first_number):
    second_number = float(input('Введите вычитаемое: '))
    print(f'Результат: {first_number - second_number}')
def multiplication(first_number):
    second_number = float(input('Введите множитель: '))
    print(f'Результат: {first_number * second_number}')
def division(first_number):
    second_number = float(input('Введите делитель: '))
    print(f'Результат: {first_number / second_number}')
def floor_division(first_number):
    second_number = float(input('Введите делитель: '))
    print(f'Результат: {first_number // second_number}')
def division_remainder(first_number):
    second_number = float(input('Введите делитель: '))
    print(f'Результат: {first_number % second_number}')
def exponentiation(first_number):
    second_number = float(input('Введите степень: '))
    print(f'Результат: {first_number ** second_number}')
def square_root(first_number):
    print(f'Результат: {first_number ** 0.5}')
def root(first_number):
    second_number = float(input('Введите степень: '))
    print(f'Результат: {first_number ** (1 / second_number)}')



helpMenu = \
    '''
=====================================
==========ДОСТУПНЫЕ=КОМАНДЫ:=========
==============СЛОЖЕНИЕ===============
==============ВЫЧИТАНИЕ==============
==============УМНОЖЕНИЕ==============
===============ДЕЛЕНИЕ===============
========ЦЕЛОЧИСЛЕННОЕ ДЕЛЕНИЕ========
=========ОСТАТОК ОТ ДЕЛЕНИЯ==========
==========КВАДРАТНЫЙ КОРЕНЬ==========
===============КОРЕНЬ================
=====================================
    '''

steps = {
    'сложение': addition,
    'вычитание': subtraction,
    'умножение': multiplication,
    'деление': division,
    'целочисленное деление': floor_division,
    'остаток от деления': division_remainder,
    'квадратный корень': square_root,
    'корень': root
    }



def mainMenu():
    def make_step():
        step_name = input('Введите операцию(help для списка команд): ').lower()
        return step_name
    while True:
        first_number = input('Введите число (либо выход): ')
        try:
            first_number = float(first_number)
        except:
            if first_number == 'exit' or first_number == 'выход':
                exit()
            else:
                print('Неверное значение!')
                continue
        step_name =  make_step()
        if step_name == 'help':
            print(helpMenu)
            continue
        elif step_name in steps.keys():
            steps[step_name](first_number)
        
if __name__ == "__main__":
    mainMenu()