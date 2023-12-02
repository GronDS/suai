from figure import *

class Oval(Figure):
    def __init__(self, pos_x: int | float = 0, pos_y: int | float = 0, 
                 pen_color: str = 'black', fill_color: str = 'white', 
                 pen_size: int = 1, main_radius: int|float = 100, 
                 second_radius: int|float = 100) -> None:
        super().__init__(pos_x, pos_y, pen_color, fill_color, pen_size)
        self._main_radius = main_radius
        self._second_radius = second_radius
        
    def draw(self, x :int|float=0, y :int|float=0):
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
    circle = Oval(0,100,'yellow', 'black', 6, 50, 50)
    circle.draw(100, 100)
    circle.draw(-100, -100)
    done()