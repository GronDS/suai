'''Есть две клетки шахматной доски. Напиши программу, которая определяет,
может ли ферзь попасть с первой клетки на вторую одним ходом. Программа читает
четыре числа, от 1 до 8 каждое. Они задают номер столбца и номер строки сначала
для первой клетки, потом для второй. Программа должна вывести «Да», если из
первой клетки ходом ферзя можно попасть во вторую, или «Нет», если такое 
действие не доступно.'''

start_place_x = int(input('Введите начальную позицию ферзя по X: '))
start_place_y = int(input('Введите начальную позицию ферзя по Y: '))

end_place_x = int(input('Введите конечную позицию ферзя по X: '))
end_place_y = int(input('Введите конечную позицию ферзя по Y: '))

rook_turn = (start_place_x == end_place_x) or (start_place_y == end_place_y)
bishop_turn = abs(start_place_x - end_place_x)\
    == abs(start_place_y - end_place_y)

if rook_turn or bishop_turn:
    print('Да')
else:
    print('Нет')