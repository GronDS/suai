'''Стажер придумала алгоритм, который по координатам двух шахматных клеток
должен определять, одинаковые они по цвету или нет. Вот только её код немного
сбоит. Помоги стажеру исправить код так, чтобы после нажатия кнопки 
«Запустить» он сработал без ошибок.'''

x1 = int(input('Введите координату первой клетки по X: '))
y1 = int(input('Введите координату первой клетки по Y: '))

x2 = int(input('Введите координату второй клетки по X: '))
y2 = int(input('Введите координату второй клетки по Y: '))

if (x1 + y1 + x2 + y2) % 2 == 0:
    print ('Да')
else:
    print ('Нет')