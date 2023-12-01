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
        self.__turn: list[int] = [0, 0]
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
    def turn(self):
        return self.__turn

    @turn.setter 
    def turn(self, turn):
        if type(turn) == list and len(turn) == 2:
            self.__turn = turn
        elif type(turn) != list:
            print("Turn incorrect type! Try again!")
            self.ask_turn()
        elif len(turn) != 2:
            print('Incorrect input! Try again!')
            self.ask_turn()
        else:
            print('Error!')
            self.ask_turn()

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
    
    def ask_turn(self, boardsize :int=3):
        '''Asks the player what move he wants to make and checks if the
        move matches the size of the board
        :boardsize: size of the playing board
	    :type boardsize: int
        return: self.turn
        '''
        while True:
            error_status = False
            current_turn  = input(
                f'{self.name}, select a cell and \
enter separated by a space (x y): ').split()
            self.turn = [int(numbers) for numbers in current_turn]
            
            for num in self.turn:
                if num > boardsize:
                        print('Value is more, than boardsize. Try again!')
                        error_status = 1
                        break
                else:
                    continue
            if error_status:
                continue
            break
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