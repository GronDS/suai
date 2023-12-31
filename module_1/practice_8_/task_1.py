'''Напишите программу, которая принимает от пользователя зарплату сотрудника за
каждый из 12 месяцев и выводит на экран среднюю зарплату за год.'''

months = (
    'Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август',\
        'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь'
        )

salary = 0

for month in months:
    salary += int(input(f'Введите зарплату сотрудника за {month}: '))

print(
    f'Средняя зарплата за год равна {round((salary / 12), 2)} рублей в месяц'
      )