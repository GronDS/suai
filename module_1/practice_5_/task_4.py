'''Напиши программу, которая принимает от пользователя четыре целых числа и 
определяет наименьшее из них.'''

values = [
    int(input('Введите 1-ое значение: ')),
    int(input('Введите 2-ое значение: ')),
    int(input('Введите 3-ое значение: ')),
    int(input('Введите 4-ое значение: '))
    ]

print(min(values))