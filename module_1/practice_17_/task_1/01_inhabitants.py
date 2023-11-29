# -*- coding: utf-8 -*-

# Вывести на консоль жителей комнат (модули room_1 и room_2)
# Формат: В комнате room_1 живут: ...

# TODO здесь ваш код

from rooms import room_1, room_2


rooms: dict = {
    'room_1': room_1.folks,
    'room_2': room_2.folks,
    }

def show_folks(rooms):
    for room, folks in rooms.items():
        print(f'В комнате {room} живут: ')
        for folk in folks:
            print(folk)

if __name__ == '__main__':
    show_folks(rooms)