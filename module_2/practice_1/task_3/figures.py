from turtle import Turtle, done
class Figures(Turtle):
    
    def __init__(
        self, pos_x :int|float, pos_y :int|float) -> None:
        super().__init__()
        self._pos_x = pos_x
        self._pos_y = pos_y

class Nougts(Figures):
    
    def __init__(self, pos_x: int | float, pos_y: int | float) -> None:
        super().__init__(pos_x, pos_y)
        
    def draw_nought(self, value):
        self.penup()
        self.goto(self._pos_x, self._pos_y)
        self.forward(value / 2)
        self.pendown()
        self.circle(value / 2)
        self.penup()
        self.hideturtle()
        
class Crosses(Figures):
    
    def __init__(self, pos_x: int | float, pos_y: int | float) -> None:
        super().__init__(pos_x, pos_y)
        
    def draw_cross(self, value):
        self.penup()
        self.goto(self._pos_x, self._pos_y)
        self.pendown()
        self.goto(self._pos_x + value, self._pos_y + value)
        self.penup()
        self.goto(self._pos_x + value, self._pos_y)
        self.pendown()
        self.goto(self._pos_x, self._pos_y + value)
        self.penup()
        self.hideturtle()

if __name__ == '__main__':
    cross1 = Crosses(0, 0)
    nougt1 = Nougts(200, 100)

    cross1.draw_cross(100)
    nougt1.draw_nought(200)
    done()
    # pass