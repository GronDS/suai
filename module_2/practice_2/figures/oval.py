from figure import *

class Oval(Figure):
        # Main class for oval in turtle
    def __init__(self, pen_color: str = 'black', fill_color: str = 'white', 
                 pen_size: int = 1, main_radius: int|float = 100, 
                 second_radius: int|float = 100) -> None:
        '''
        :main_radius: horizontal radius of the oval
        :type main_radius: int | float
        :second_radius: vertical radius of the oval
        :type second_radius: int | float
        '''
        super().__init__(pen_color, fill_color, pen_size)
        self._main_radius = main_radius
        self._second_radius = second_radius
        
    def draw(self, x :int|float=0, y :int|float=0):
        """"Draw base oval.
        :x: x coord
	    :type x: int | float
	    :y: x coord
	    :type y: int | float
        """
        self.go_to(x,y)
        dx = self.xcor()
        dy = self.ycor()
        self.color(self._pen_color, self._fill_color)
        self.begin_fill()
        for deg in range(361):
            rad = radians(deg)
            move_x = self._main_radius * sin(rad) + dx
            move_y = -self._second_radius * cos(rad)\
                + self._second_radius + dy
            self.goto(move_x, move_y)
        self.end_fill()


if __name__ == '__main__':
    circle = Oval('yellow', 'black', 6, 50, 100)
    circle.draw(100, 100)
    circle.draw(-100, -100)
    done()