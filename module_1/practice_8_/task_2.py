'''Напишите программу, которая считывает с клавиатуры два числа:
a и b, —  считает и выводит в консоль среднее арифметическое всех чисел из 
отрезка [a; b], кратных числу 3.'''

number_a = int(input('Введите число a: '))
number_b = int(input('Введите число b: '))

counter = 0
summ = 0

for number in range(number_a, number_b + 1):
    if number % 3 == 0:
        counter += 1
        summ += number

print(f'Cреднее арифметическое всех чисел из отрезка [{number_a}; {number_b}],'
      f' кратных числу 3 : {summ / counter}')