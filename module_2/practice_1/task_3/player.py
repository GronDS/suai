from typing import Literal, Annotated


class Player:
    #tic-tac-toe player class
    def __init__(self, name:str="Player", side:Literal[0, 1]=0) -> None:
        """Initializes the player's main attributes
	:__name: player name
	:type name: str|None
  	:__side: cell occupancy status
	:type __side: int|None
	:turn: player's current move
	:type turn: list[int]
	:return: None
	"""
        try:
            self.__name: str|None = name
            if type(self.__name) != str:
                    raise TypeError('Incorrect input')
        except TypeError as error:
            print(error)
            raise
            
        try:
            if type(side) != int:
                raise TypeError('Side value is non-int!')
            if side not in (0,1):
                    raise ValueError('Incorrect input(0/1)!')
        except ValueError as error:
            print(error)
            raise
        else:
            self.__side = side

        self.__turn: Annotated[list[int], 2] = [0, 0]
    
    def ask_turn(self, turn: Annotated[list[int], 2], boardsize):
        '''Asks the player what move he wants to make and checks if the
        move matches the size of the board
        :boardsize: size of the playing board
	    :type boardsize: int
        return: self.__turn
        '''
#         current_turn  = input(
#             f'{self.__name}, select a cell and \
# enter separated by a space (x y): ').split()
        
        try:    
            self.__turn = [int(numbers) for numbers in turn]
            for num in self.__turn:
                if num > boardsize:
                        raise ValueError(
                            'Value is more, than boardsize!')
        except ValueError as error:
            print(error)
            raise
        else:
            return self.__turn

        
        
if __name__ == '__main__':
#   player_1 = Player('Player', 1)
#   print(player_1.ask_turn([3,3], 5))