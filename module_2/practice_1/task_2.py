'''Для одной игры необходимо реализовать механику магии, где при соединении 
вух элементов получается новый. У нас есть четыре базовых элемента: «Вода», 
«Воздух», «Огонь», «Земля». Из них как раз и получаются новые: «Шторм», «Пар»,
«Грязь», «Молния», «Пыль», «Лава».
Вот таблица преобразований:
- «Вода» + «Воздух» = «Шторм»
- «Вода» + «Огонь» = «Пар»
- «Вода» + «Земля» = «Грязь»
- «Воздух» + «Огонь» = «Молния»
- «Воздух» + «Земля» = «Пыль»
- «Огонь» + «Земля» = «Лава»
Напишите программу, которая реализует все эти элементы. Каждый элемент 
необходимо организовать как отдельный класс. Если результат не определён,
то возвращается None.'''

class Water:
    def __init__(self) -> None:
        self._spell_power: int = 1
    
    def __add__(self, other):
        if isinstance(other, Wind):
            return Storm()
        elif isinstance(other, Fire):
            return Steam()
        elif isinstance(other, Earth):
            return Mud()
        else:
            return None

class Wind:
    def __init__(self) -> None:
        self._spell_power: int = 2

    def __add__(self, other):
        if isinstance(other, Water):
            return Storm()
        elif isinstance(other, Fire):
            return Lightning()
        elif isinstance(other, Earth):
            return Dust()
        else:
            return None
        
class Fire:
    def __init__(self) -> None:
        self._spell_power: int = 4
    
    def __add__(self, other):
        if isinstance(other, Water):
            return Steam()
        elif isinstance(other, Wind):
            return Lightning()
        elif isinstance(other, Earth):
            return Lava()
        else:
            return None

class Earth:
    def __init__(self) -> None:
        self._spell_power: int = 3
    def __add__(self, other):
        if isinstance(other, Water):
            return Mud()
        elif isinstance(other, Wind):
            return Dust()
        elif isinstance(other, Fire):
            return Lava()
        else:
            return None        
class Storm:
    def __init__(self) -> None:
        self._spell_power: int = 9

class Steam:
    def __init__(self) -> None:
        self._spell_power: int = 7

class Mud:
    def __init__(self) -> None:
        self._spell_power: int = 8

class Lightning:
    def __init__(self) -> None:
        self._spell_power: int = 6

class Dust:
    def __init__(self) -> None:
        self._spell_power: int = 7

class Lava:
    def __init__(self) -> None:
        self._spell_power: int = 5

if __name__ == '__main__':
    spell_1 = Fire()
    # spell_1 += Earth()
    # print(type(spell_1))
    if spell_1:
        print(spell_1._spell_power)