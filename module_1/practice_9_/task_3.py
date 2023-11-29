'''Пользователь вводит N чисел. Среди натуральных чисел, которые он указал, 
найдите наибольшее по сумме цифр. Выведите на экран это число и сумму его цифр.
'''
number_n = int(input('Сколько чисел Вы введете?: '))
max_summ = 0
max_value = 0

for i in range(number_n):
    final_summ = 0
    new_value = str(int(input('Введите число: ')))
    for digit in new_value:
        final_summ += int(digit)
    if final_summ > max_summ:
        max_summ = final_summ
        max_value = new_value

print(f'Наибольшое число по сумме цифр - {max_value}. Она равна {max_summ}.')