'''У неудачливого бухгалтера всё опять идёт наперекосяк: ему приносят такие 
большие счета, что числа не помещаются на бумаге. Напишите программу, которая
считала бы для него, сколько цифр во вводимом числе. Обратите внимание, что
число 0 имеет одну цифру.'''

while True:
    current_number = int(input('Введите число: '))
    
    if len(str(current_number)) % 10 == 1:
        digit_name = 'цифра'
    elif len(str(current_number)) % 10 == 0 or\
        len(str(current_number)) % 10 in range(5, 10):
            digit_name = 'цифр'
    else:
        digit_name = 'цифры'
        
    print(f'В числе {current_number} {len(str(current_number))} {digit_name}')