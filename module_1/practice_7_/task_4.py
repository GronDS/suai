'''Мальчик загадывает число между 1 и 100 (включительно). Компьютер может 
спросить у мальчика: «Твоё число равно, меньше или больше, чем число N?»,
где N —  число, которое хочет проверить компьютер. Мальчик отвечает одним 
из трёх чисел: 1 —  равно, 2 —  больше, 3 —  меньше.Напишите программу, которая
с помощью цепочки таких вопросов и ответов мальчика угадывает число.
Дополнительно: сделайте так, чтобы можно было гарантированно угадать число за
семь попыток.'''

print('Загадайте целое число между 1 и 100(включительно)')

min_number = 1
max_number = 100
answer_number = (min_number + max_number) // 2
user_answer = ''

while True:
    answer_number = (min_number + max_number) // 2
    user_answer = input(
        f'Ваше число {answer_number} (равно, больше, меньше)?: '
        )
    
    if user_answer == 'равно':
        print(f'Я отгадал число {answer_number}!')
        break
    elif user_answer == 'больше':
        min_number = answer_number + 1
        continue
    elif user_answer == 'меньше':
        max_number = answer_number - 1
        continue
    else:
        print('Вы ввели неверное значение')
        continue