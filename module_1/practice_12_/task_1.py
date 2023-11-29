''' В одной IT-компании существует негласный закон об именовании текстовых 
документов:
1. Название файла не должно начинаться на один из специальных символов: 
@, №, $, %, ^, &, *, ().
2. Файл заканчивается расширением .txt или .docx.
    Напишите программу, которая получает на вход полное название файла и 
проверяет его по этим правилам.'''


special_symbols = ('@', '№', '$', '%', '^', '&', '*', '(', ')')
file_format = ('txt', 'docx')

file_name = input('Название файла: ')

start_name_error = \
    'Ошибка: название начинается на один из специальных символов.'
file_type_error = \
    'Ошибка: неверное расширение файла. Ожидалось .txt или .docx.'

if file_name[0] in special_symbols:
    print(start_name_error)
elif file_name.split('.')[-1] not in file_format:    
    print(file_type_error)
else:
    print('Файл назван верно.')