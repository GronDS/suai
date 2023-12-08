from quads import *

class Trapezoid(Quadrilaterals):
# Trapezoid class for turtle    
    def __init__(self, pen_color: str = 'black', fill_color: str = 'white',
                 pen_size: int = 1, bot_base_len: int | float = 100,
                 top_base_len: int | float = 50, 
                 right_side_len: int | float = 50,
                 right_bot_angle: int | float = 45) -> None:
        """
        :bot_base_len: length of the lower base of the trapezoid
        :type bot_base_len: int | float
        :top_base_len: length of the upper base of the trapezoid
        :type top_base_len: int | float
        :right_side_len: length of the right side of the trapezoid
        :type right_side_len: int | float
        :right_bot_angle: right bottom angle
        :type right_bot_angle: int | float
        """
        super().__init__(pen_color, fill_color, pen_size)
        self._bot_base_len = bot_base_len
        self._top_base_len = top_base_len
        self._right_side_len = right_side_len
        self.right_bot_angle = right_bot_angle
        
    def draw(self, x, y):
        """"Draw trapezoid.
        :x: x coord
	    :type x: int | float
	    :y: x coord
	    :type y: int | float
        """    
        self.begin_fill()
        self.go_to(x, y)
        self.forward(self._bot_base_len)
        self.left(180 - self.right_bot_angle)
        self.forward(self._right_side_len)
        self.left(self.right_bot_angle)
        self.forward(self._top_base_len)
        self.goto(x, y)
        self.setheading(0)
        self.end_fill()
        
if __name__ == '__main__':
    trapez = Trapezoid('black', 'grey', 3, 400, 200, 150, 45)
    trapez.draw(0, -200)
    done()