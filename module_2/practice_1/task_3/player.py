'''class Player:
#  У игрока может быть
#   — имя
#   — на какую клетку ходит'''

class Player:
    
    def __init__(self, name=None) -> None:
        self.name = name
        self.turn: list = [1, 1]
        self.side = None
    def ask_name(self):
        self.name = input('Enter your name: ')
        return self.name
    def ask_turn(self):
        self.turn  = input(
            f'{self.name}, select a cell and enter separated by a space (x y): '
            ).split()
        self.turn = [int(numbers) for numbers in self.turn]
        return self.turn
    def ask_side(self):
        self.side = int(
            input('Choose your side(0 for noughts 1 for crosses): '))

if __name__ == '__main__':
    # player_1 = Player()
    # if not player_1.name:
    #     player_1.ask_name()
    # player_1.ask_turn()
    # print(player_1.turn)
    pass