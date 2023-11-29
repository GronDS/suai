'''O базе данных магазина вся необходимая информация по товарам делится на два 
словаря: первый отвечает за коды товаров, второй —  за списки количества 
разнообразных товаров на складе. 
Каждая запись второго словаря отображает, сколько и по какой цене закупалось 
товаров (цена указана за 1 шт.). Напишите программу, которая рассчитывает, на
какую сумму лежит каждого товара на складе, и выводит эту информацию на экран.
'''

goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

reverse_goods = {}

for key, value in goods.items():
    reverse_goods[value] = key

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

for product_key, product in store.items():
    product_quantity = 0
    product_price = 0
    for model in range(len(product)):
        product_quantity += product[model]['quantity']
        product_price += product[model]['quantity'] * product[model]['price'] 
    print(
        f'{reverse_goods[product_key]} - {product_quantity} шт,\
стоимость {product_price} руб')