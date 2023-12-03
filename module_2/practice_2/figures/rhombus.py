from parallelogram import *


class Rhombus(Parallelogram):
    def __init__(self, pen_color: str = 'black', fill_color: str = 'white', 
                 pen_size: int = 1, first_side: int | float = 50, 
                 base_angle: int | float = 90) -> None:
        super().__init__(pen_color, fill_color, pen_size, first_side)
        self._base_angle = base_angle
        self._second_side = self._first_side
        
    
    def draw(self, x: int | float = 0, y: int | float = 0):
        return super().draw(x, y)

if __name__ == '__main__':
    rhomb = Rhombus(
        pen_color='blue', fill_color='black',first_side=300, base_angle=30)
    rhomb.draw()
    done()