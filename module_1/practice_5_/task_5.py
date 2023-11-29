'''Вася набрался опыта и решил поискать вакансию с большей зарплатой. Его 
привлекла вакансия со странной формулой для расчёта заработной платы:
((200 * hours) / (2 ** 3)) + hours.
Он хочет понять, сколько часов нужно отработать, чтобы хватило на погашение 
кредита и еду. Напишите программу, которая запрашивает у пользователя три числа
: количество отработанных часов, остаток по кредиту и количество денег на еду.
После этого рассчитывается зарплата по формуле. Если зарплата больше или равна 
сумме, которая требуется на кредит и еду, то выводится сообщение: «Часов 
хватает. Можно отдохнуть». В противном случае: «Часов не хватает. Придётся 
работать больше!»'''

hours = int(input('Введите количество отработанных часов: '))
loan_balance = int(input('Введите остаток по кредиту: '))
food_money = int(input('Введите количество денег на еду: '))

salary = ((200 * hours) / (2 ** 3)) + hours
# print(f'Ваша зар. плата {salary}')

if salary >= (loan_balance + food_money):
    print('Часов хватает. Можно отдохнуть')
else:
    print('Часов не хватает. Придётся работать больше!')