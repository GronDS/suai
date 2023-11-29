from cell import Cell
from draw_numbers import *
from figures import *


window_size = 900

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
        self.__size = size
        self.__cells :list = []
        self.__x :int|float= -(window_size / 2)
        self.__y :int|float= -(window_size / 2)
        
    @property
    def size(self):
        return self.__size
    
    @size.setter
    def size(self, size):
        if 3 <= size <= 9:
            self.__size = size
        else:
            print("Incorrect size of board!")

    @property
    def cells(self):
        return self.__cells

    @cells.setter
    def cells(self, cells):
        if type(cells) == list:
            self.__cells = cells
        else:
            print("Incorrect value of cells dict!")

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if type(x) == int or type(x) == float :
            self.__x = x
        else:
            print("Incorrect X value")
            
            
    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if type(y) == int or type(y) == float :
            self.__y = y
        else:
            print("Incorrect Y value")
        
    def make_board(self):
        '''Сreates a board with a frame for numbering
        :cell_len: cell border size
	    :type cell_len: int|float
        :i: row number of cells
	    :type i: int (4<=i<=10)
        :j: cell number in row
	    :type i: int (4<=i<=10)
        :current_cell: current cell in the generation cycle
	    :type cell_len: Сell()
        '''
        cell_len = window_size / (self.size + 1)
        for i in range(self.size+1):
            self.x = -(window_size / 2)
            for j in range(self.size+1):
                current_cell = Cell([i, j])
                current_cell.penup()
                if i == 0 or j == 0:
                    current_cell.occupied = True
                self.cells.append(current_cell)
                current_cell.draw_cell(cell_len, self.x, self.y)
                self.x += cell_len
            self.y += cell_len
        self.x = -(window_size / 2)
        self.y = -(window_size / 2)
        
    def numerate_board(self):
        '''Сalls frame design functions with numbering'''
        def black_corner():
            '''Paints the bottom left cell black'''
            cell_len = window_size / (self.size + 1)
            start_cell = Cell()
            start_cell.speed(0)
            start_cell.draw_black_cell(cell_len, self.x, self.y)
        
        def numerate_x():
            '''Draws numbering by X'''     
            cell_len = window_size / (self.size + 1)
            self.x = -(window_size / 2) +  cell_len + (cell_len / 2)
            self.y = -(window_size / 2) + cell_len - (cell_len / 10)
            for cell in range(self.size):
                drawnum((cell_len / 2.5), cell + 1, self.x, self.y)
                self.x+= cell_len
        
        def numerate_y():
            '''Draws numbering by Y'''      
            cell_len = window_size / (self.size + 1)
            self.x = -(window_size / 2) + (cell_len / 2)
            self.y = -(window_size / 2) + 2 * cell_len - (cell_len / 10)
            for cell in range(self.size):
                drawnum((cell_len / 2.5), cell + 1, self.x, self.y)
                self.y+= cell_len
                        
        black_corner()
        numerate_x()
        numerate_y()
    
    def draw_turn(self, order_x, order_y, figure):
        '''Determines the coordinates of the cell of the current move and calls
        the function for drawing the corresponding figure'''
        cell_len = window_size / (self.size + 1)
        x = -(window_size / 2) + cell_len * order_x
        y = -(window_size / 2) + cell_len * order_y
        if figure == 0:
            nought = Nougts(x, y)
            nought.draw_nought(cell_len)
        elif figure == 1:
            cross = Crosses(x, y)
            cross.draw_cross(cell_len)
        
        
        
if __name__ == '__main__':
    # my_board = Board(5)
    # my_board.make_board()
    # my_board.numerate_board()
    # for cell in my_board.cells:
    #     print(cell.order, cell.occupied)
        
    # my_board.draw_turn(2, 2, 1)
    pass