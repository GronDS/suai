from quads import *


class Parallelogram(Quadrilaterals):
    # Main class for parallelogram in turtle
    
    def __init__(self, pen_color: str = 'black', fill_color: str = 'white', 
                 pen_size: int = 1, first_side: int|float = 50,
                 second_side: int|float = 100, 
                 base_angle: int|float = 90) -> None:
        '''
        :first_side: horizontal side
        :tipe first_side: int | float
        :second_side: vertical side
        :tipe second_side: int | float        
        :base_angle: left bottom angle
        :tipe base_angle: int | float
        '''
        super().__init__(pen_color, fill_color, pen_size)
        self._first_side = first_side
        self._second_side = second_side
        self._base_angle = base_angle
        
    def draw(self, x: int|float=0, y: int|float=0):
        """"Draw base parallelogram.
        :x: x coord
	    :type x: int | float
	    :y: x coord
	    :type y: int | float
        """        
        self.begin_fill()
        self.go_to(x, y)
        self.forward(self._first_side)
        self.left(180 - self._base_angle)
        self.forward(self._second_side)
        self.left(self._base_angle)
        self.forward(self._first_side)
        self.left(180 - self._base_angle)
        self.forward(self._second_side)
        self.setheading(0)
        self.end_fill()
        
        
if __name__ == '__main__':
    paral = Parallelogram('red','blue', 5, 200, 100, 85)
    paral.draw()
    done()