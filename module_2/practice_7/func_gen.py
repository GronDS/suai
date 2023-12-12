while True:
    try:
        number_n :int= int(input('Введите число N: '))
        if number_n > 0:
            break
        if type(number_n) != int:
            raise TypeError
        # ('Неверный ввод, число должно быть целым и больше 0!')
        if number_n < 0:
            raise ValueError('Число должно быть больше 0!')
    except (TypeError, ValueError) as error:
        print(error)
        continue

def square():
    i :int= 1
    while (i <= number_n):
        yield i
        i+= 1
        
for i in square():
    # return squares of all numbers from 1 to number_n
    answer :int= i ** 2
    print(f'===\n{i} ** 2 = {answer}')