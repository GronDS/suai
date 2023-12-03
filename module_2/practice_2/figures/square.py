from figures.rectangle import *


class Square(Rectangle):
    def __init__(self, pen_color: str = 'black', fill_color: str = 'white', 
                 pen_size: int = 1, first_side: int | float = 50) -> None:
        super().__init__(pen_color, fill_color, pen_size, first_side)
        #equalize the sides of rectangle
        self._second_side = self._first_side
        

if __name__ == '__main__':
    square_123 = Square('blue', 'pink', 3, 200)
    square_123.draw(200, 200)
    done()