'''Дано целое число N (> 1), являющееся числом Фибоначчи: N = F(K). Найти целое
число K - порядковый номер числа Фибоначчи N.'''

num_fibonacci = int(input('Введите число Фибоначчи: '))
first_number = 1
second_number = 1
new_number = 0
number_k = 2

while new_number != num_fibonacci:
    if num_fibonacci == 1:
        print('Порядковые номера числа 1 в ряду чисел Фибоначчи: 1 и 2')
        break
    else:
        new_number = first_number + second_number
        first_number = second_number
        second_number = new_number
        number_k += 1

print(f'Порядковый номер числа {num_fibonacci} в ряду чисел Фибоначчи: '
      f'{number_k}')
