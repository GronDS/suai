from quads import *


class Parallelogram(Quadrilaterals):
    _base_angle = 90
    _second_side = 100
    
    def __init__(self, pen_color: str = 'black', fill_color: str = 'white', 
                 pen_size: int = 1, first_side: int|float = 50,) -> None:
        super().__init__(pen_color, fill_color, pen_size)
        self._first_side = first_side
        
    def draw(self, x: int|float=0, y: int|float=0):
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
    paral = Parallelogram('red','blue', 5, 100)
    paral.draw()
    done()