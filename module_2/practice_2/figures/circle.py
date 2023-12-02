from oval import *


class Circle(Oval):
    def __init__(self, pos_x: int | float = 0, pos_y: int | float = 0, 
                 pen_color: str = 'black', fill_color: str = 'white', 
                 pen_size: int = 1, main_radius: int | float = 100) -> None:
        super().__init__(pos_x, pos_y, pen_color, fill_color, pen_size, 
                         main_radius)
        self._second_radius = self._main_radius
        

if __name__ == '__main__':
    circle_1 = Circle(0,0,'green', 'blue', 5, 200)
    circle_1.draw(-100,0)
    done()