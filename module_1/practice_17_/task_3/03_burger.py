# -*- coding: utf-8 -*-

# В этом модуле создать рецепт двойного чизбургера
# с помощью фукций из my_burger и вывести на консоль.

# Создать рецепт своего бургера, по вашему вкусу.
# Если не хватает инградиентов - создать соответствующие функции в модуле my_burger

# TODO здесь ваш код

from my_burger import add_buns, add_cheese, add_mayo, add_patty, \
add_pickles, add_tomatos, add_teriyaki, add_honey, add_pineapple

def make_double_cheeseburger():
    print('Готовим двойной чизбургер!')
    add_buns(2)
    add_mayo(1)
    add_patty(2)
    add_cheese(4)
    add_pickles(2)
    add_tomatos(1)
    print('Готово!')


def make_hawaiian_burger():
    print('Готовим гавайский бургер!')
    add_buns(2)
    add_mayo('1/2')
    add_patty(1)
    add_teriyaki(2)
    add_honey(1)
    add_cheese(2)
    add_pineapple(3)
    print('Готово!')
make_double_cheeseburger()
print('')
make_hawaiian_burger()
