from quads import *

class Trapezoid(Quadrilaterals):
    
    def __init__(self, pen_color: str = 'black', fill_color: str = 'white',
                 pen_size: int = 1, bot_base_len: int | float = 100,
                 top_base_len: int | float = 50, 
                 right_side_len: int | float = 50,
                 left_bot_angle: int | float = 45) -> None:
        super().__init__(pen_color, fill_color, pen_size)
        self._bot_base_len = bot_base_len
        self._top_base_len = top_base_len
        self._right_side_len = right_side_len
        self._left_bot_angle = left_bot_angle
        
    def draw(self, x, y):
        self.begin_fill()
        self.go_to(x, y)
        self.forward(self._bot_base_len)
        self.left(180 - self._left_bot_angle)
        self.forward(self._right_side_len)
        self.left(self._left_bot_angle)
        self.forward(self._top_base_len)
        self.goto(x, y)
        self.setheading(0)
        self.end_fill()
        
if __name__ == '__main__':
    trapez = Trapezoid('black', 'grey', 3, 400, 200, 150, 45)
    trapez.draw(0, -200)
    done()