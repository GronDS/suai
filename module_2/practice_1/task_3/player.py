class Player:
    #tic-tac-toe player class
    def __init__(self, name=None) -> None:
        """Initializes the player's main attributes
	:__name: player name
	:type name: str|None
	:turn: player's current move
	:type turn: list[int]
 	:__side: cell occupancy status
	:type __side: int|None
	:return: None
	"""
        self.__name: str|None = name
        self.turn: list[int] = [1, 1]
        self.__side :int|None= None
    
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if type(name) == str:
            self.__name = name
        else:
            print("Incorrect name!")    

    @property
    def side(self):
        return self.__side

    @side.setter
    def side(self, side):
        if side == 1 or side == 0:
            self.__side = side
        else:
            print("Incorrect value!")    
           
    def ask_name(self):
        '''Asks the player's name
        return: self.name'''
        self.name = input('Enter your name: ')
        return self.name
    
    def ask_turn(self):
        '''Asks the player what move he wants to make
        return: self.turn
        '''
        turn  = input(
            f'{self.name}, select a cell and \
enter separated by a space (x y): ').split()
        self.turn = [int(numbers) for numbers in turn]
        return self.turn
    
    def ask_side(self):
        ''' Ask what piece player's playing for
            :return: None'''
        self.side = int(
            input('Choose your side(0 for noughts 1 for crosses): '))

if __name__ == '__main__':
    # player_1 = Player()
    # if not player_1.name:
    #     player_1.ask_name()
    # player_1.ask_turn()
    # print(player_1.turn)
    pass