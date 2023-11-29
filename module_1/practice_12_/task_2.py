'''При написании клиент-серверного приложения часто приходится работать с 
IP-адресами. Как вы уже знаете, IP-адрес состоит из четырёх целых чисел в 
диапазоне от 0 до 255, разделённых точками.
    Пользователь вводит строку. Напишите программу, которая определяет, 
является ли заданная строка правильным IP-адресом. Обеспечьте контроль ввода, 
где предусматривается ввод целых чисел от 0 до 255, а также точки между ними.
'''
ip_address = input('Введите IP: ')

address_values = ip_address.split('.')
current_error = ''

if len(address_values) != 4:
    current_error = 'Адрес —  это четыре числа, разделённые точками.'
else:
    for value in address_values:
        if value.isdigit():
            if int(value) not in range(0, 256):
                current_error = (f'{value} превышает 255.')
        else:
            current_error = f'{value} —  это не целое число.'

print(current_error) if current_error else print('IP-адрес корректен.')