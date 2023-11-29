'''Написать программу решения задачи. В программе предусмотреть ввод исходных
данных с клавиатуры. Результат округлить до трех знаков и вывести в консоль.'''

from math import pi, tan, cos, log

z = float(input('Введите z: '))
alpha = float(input('Введите alpha: '))


x = (1 + 1/(tan(pi/(4 * z)))) / (1 + cos(alpha))
y = cos(2 * alpha + (pi / 2)) ** 3 + log(pi / (3 * z))
print('x = ', round(x, 3))
print('y = ', round(y, 3))