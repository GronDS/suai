'''В научной лаборатории выводят и тестируют новые виды клеток. Есть список из
N этих клеток, элементом которого является показатель эффективности, а индексом
—  ранг клетки. Учёные отбирают клетки по следующему принципу —  если 
эффективность клетки меньше её ранга, то она не подходит. Напишите программу,
которая выводит на экран элементы списка, значения которых меньше их индекса.
'''
wrong_cells = []
cells_number = int(input('Количество клеток: '))

for cell in range(cells_number):
    cell_value = int(input(f'Эффективность {cell + 1} клетки: '))
    if cell_value < (cell + 1):
        wrong_cells.append(cell_value)

print('Неподходящие значения:', *wrong_cells)