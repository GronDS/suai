from turtle import Turtle
from abc import ABC, abstractmethod
class Figures(ABC, Turtle):
    
    def __init__(
        self, pos_x :int|float, pos_y :int|float) -> None:
        super().__init__()
        self._pos_x = pos_x
        self._pos_y = pos_y
        self.hideturtle()
        
    @abstractmethod
    def draw():
        pass

class Nougts(Figures):
            
    def draw(self, value):
        self.penup()
        self.goto(self._pos_x, self._pos_y)
        self.forward(value / 2)
        self.pendown()
        self.circle(value / 2)
        self.penup()
        
class Crosses(Figures):
        
    def draw(self, value):
        self.penup()
        self.goto(self._pos_x, self._pos_y)
        self.pendown()
        self.goto(self._pos_x + value, self._pos_y + value)
        self.penup()
        self.goto(self._pos_x + value, self._pos_y)
        self.pendown()
        self.goto(self._pos_x, self._pos_y + value)
        self.penup()

if __name__ == '__main__':
    cross1 = Crosses(0, 0)
    nougt1 = Nougts(200, 100)

    cross1.draw(100)
    nougt1.draw(200)
    # pass