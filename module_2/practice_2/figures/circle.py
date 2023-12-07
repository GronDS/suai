from module_2.practice_2.figures.ellipse import *


class Circle(Ellipse):
    def __init__(self, pen_color: str = 'black', fill_color: str = 'white', 
                 pen_size: int = 1, main_radius: int | float = 100) -> None:
        super().__init__(pen_color, fill_color, pen_size, main_radius)
        #equalize the horizontal and vertical radii of the oval
        self._second_radius = self._main_radius
        

if __name__ == '__main__':
    circle_1 = Circle('green', 'blue', 5, 200)
    circle_1.draw(-100,0)
    done()