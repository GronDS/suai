'''O базе данных интернет-магазина PizzaTime хранятся данные o том, кто, что и 
сколько заказывал y них в определённый период. Вам нужно структурировать эту 
информацию, a также понять, сколько всего пицц купил каждый заказчик.
Ha вход в программу подаётся N заказов. Каждый заказ представляет собой строку
вида «Покупатель —  название пиццы —  количество заказанных пицц». Реализуйте 
код, который выводит список покупателей и их заказов по алфавиту. Учитывайте, 
что один человек может заказать одно и то же несколько раз.'''

orders: dict = {

}
order_number: int = int(input('Введите кол-во заказов: '))

for order in range(order_number):
    client_name, pizza_name, pizzas_quantity =\
        input(f'{order + 1} заказ: ').split()
    pizzas_quantity = int(pizzas_quantity)

    if client_name in orders.keys():
        if pizza_name in orders[client_name].keys():
            orders[client_name][pizza_name] += pizzas_quantity             
        else:
            orders[client_name].update({pizza_name: pizzas_quantity})
    else:
        orders[client_name] = {pizza_name: pizzas_quantity}

for client in orders:
    print(f'{client}:')
    for key, value in sorted(orders[client].items()):
        print(f'\t{key}: {value}')