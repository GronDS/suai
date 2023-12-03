from figures.parallelogram import *

class Rectangle(Parallelogram):
    #Rectangle class  
    def __init__(self, pen_color: str = 'black', fill_color: str = 'white', 
                 pen_size: int = 1, first_side: int | float = 50, 
                 second_side: int|float = 100) -> None:
        """
        :second_side:vertical  side of a rectangle
        :type second_side: int | float
        """
        super().__init__(pen_color, fill_color, pen_size, first_side)
        self._second_side = second_side
        
        
if __name__ == '__main__':
    rect_1 = Rectangle('yellow', 'black', 3, 50, 200)
    rect_1.draw()
    done()