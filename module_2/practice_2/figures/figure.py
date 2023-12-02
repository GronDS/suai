from abc import ABC, abstractmethod
from turtle import Turtle, done
from math import sin, cos, radians, pi


class Figure(ABC, Turtle):   
    
    def __init__(
        self, pos_x :int|float=0, pos_y :int|float=0,pen_color :str= 'black',
        fill_color :str='white', pen_size :int= 1
        ) -> None:
        super().__init__()
        self._pos_x = pos_x
        self._pos_y = pos_y
        self._pen_color = pen_color
        self._fill_color = fill_color
        self._pen_size = pen_size
        self.set_fill_color(self._fill_color)
        self.set_pen_color(self._pen_color)
        self.set_pen_size(self._pen_size)
        
               
    def go_to(self, x :int|float=0, y :int|float=0):
        self.penup()
        self.goto(x, y)
        self.pendown()
        
    def set_fill_color(self, fill_color :str):
        self.fillcolor(fill_color)
    
    def set_pen_color(self, color :str):
        self.pencolor(color)
    
    def set_pen_size(self, size :int):
        self.pensize(size)       
    
        
    @abstractmethod
    def draw(self):
        pass