from cell import *
from draw_numbers import *
from figures import *


WINDOW_SIZE = 900

class Board():
#  A board class that creates instances of a cell
    def __init__(self, size :int=3) -> None:
        """Initializes the main attributes of the board.
	:size: size of the playing part of the board
	:type size: int (3<=size<=9)
	:__x: x coordinate. Default position in the bottom left edge of the board
	:type __x: int|float
    :__y: y coordinate. Default position in the bottom left edge of the board
	:type __y: int|float
	:return: None
	"""
        try:
            if 3 <= size <= 9:
                self.__size :int= size
            else:
                raise Exception("Incorrect size of board!")
        except Exception as error:
            print(error)
        self.__cells :list = []
        self.__x :int|float= -(WINDOW_SIZE / 2)
        self.__y :int|float= -(WINDOW_SIZE / 2)
        self.__cell_len :int|float= WINDOW_SIZE / (self.__size + 1)
        #:cell_len: cell border size
	    # :type cell_len: int|float
        self.__make_board()
        self.__black_corner()
        self.__numerate_x()
        self.__numerate_y()

    @property
    def cells(self):
        return self.__cells

    @cells.setter
    def cells(self, cells):
        try:
            if type(cells) == list:
                self.__cells = cells
            else:
                raise TypeError("Incorrect value of cells dict!")
        except TypeError as error:
            print(error)
            raise
            
    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        try:
            if type(x) == int or type(x) == float :
                self.__x = x
            else:
                raise ValueError("Incorrect X value")
        except ValueError as error:
            print(error)
            raise
            
            
    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        try:
            if type(y) == int or type(y) == float :
                self.__y = y
            else:
                raise ValueError("Incorrect Y value")
        except ValueError as error:
            print(error)
            raise

    def __make_board(self):
        '''Сreates a board with a frame for numbering
        :i: row number of cells
	    :type i: int (4<=i<=10)
        :j: cell number in row
	    :type i: int (4<=i<=10)
        :current_cell: current cell in the generation cycle
	    :type current_cell: Сell()
        '''
        x = self.__x
        y = self.__y
        for i in range(self.__size+1):
            for j in range(self.__size+1):
                current_cell = Cell([i, j])
                current_cell.penup()
                if i == 0 or j == 0:
                    current_cell.occupied = True
                self.cells.append(current_cell)
                current_cell.draw_cell(self.__cell_len , x, y)
                x += self.__cell_len 
            y += self.__cell_len 
            x = self.__x
        

    def __black_corner(self):
        '''Paints the bottom left cell black'''
        start_cell = Cell()
        start_cell.speed(0)
        start_cell.draw_black_cell(self.__cell_len , self.x, self.y)
        
    def __numerate_x(self):
        '''Draws numbering by X'''     
        x = self.__x +  \
            self.__cell_len  + (self.__cell_len  / 2)
        y = self.__y + \
            self.__cell_len  - (self.__cell_len  / 10)
        for cell in range(self.__size):
            drawnum((self.__cell_len  / 2.5), cell + 1, x, y)
            x+= self.__cell_len 
        
    def __numerate_y(self):
        '''Draws numbering by Y'''      
        cell_len = WINDOW_SIZE / (self.__size + 1)
        x = self.__x + (cell_len / 2)
        y = self.__y + 2 * cell_len - (cell_len / 10)
        for cell in range(self.__size):
            drawnum((cell_len / 2.5), cell + 1, x, y)
            y+= cell_len
    
    def draw_turn(self, order_x, order_y, figure):
        '''Determines the coordinates of the cell of the current move and calls
        the function for drawing the corresponding figure'''
        try:
            if order_x <= self.__size and order_y <= self.__size:
                x = self.__x + self.__cell_len  * order_x
                y = self.__y + self.__cell_len  * order_y
            else:
                raise TypeError('Incorrect order input!')
        except TypeError as error:
            print(error)
  
        try :            
            if figure == 0:
                nought = Nougts(x, y)
                nought.draw(self.__cell_len )
            elif figure == 1:
                cross = Crosses(x, y)
                cross.draw(self.__cell_len )
            else:
                if type(figure) != int:
                    raise TypeError('Incorrect input type!(Need int)')
                elif figure != 0 and figure !=1:
                    raise ValueError('Incorrect figuretype value(not 0/1)!')
                else:
                    raise Exception('Unkown figuretype error (°ロ°)! !!')
        except (TypeError, ValueError, Exception) as error :
            print(error)
            raise
        
        
        
if __name__ == '__main__':
    my_board = Board(5)
    for cell in my_board.cells:
        print(cell.order, cell.occupied)
    my_board.draw_turn(2, 2, 1)
    done()
    pass