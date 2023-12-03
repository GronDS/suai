from parallelogram import *


class Rhombus(Parallelogram):
    def __init__(self, pen_color: str = 'black', fill_color: str = 'white', 
                 pen_size: int = 1, first_side: int | float = 50, 
                 base_angle: int | float = 90) -> None:
        """
        :base_angle: bottom right angle of the rhombus
        :type base_angle: int | float
        """
        super().__init__(pen_color, fill_color, pen_size, first_side)
        self._base_angle = base_angle
        #Equalize the sides of parallelogram
        self._second_side = self._first_side

if __name__ == '__main__':
    rhomb = Rhombus(
        pen_color='blue', fill_color='black',first_side=300, base_angle=30)
    rhomb.draw()
    done()