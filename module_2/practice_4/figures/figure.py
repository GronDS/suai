from abc import ABC, abstractmethod
from turtle import Turtle, done
from math import sin, cos, radians, pi


class Figure(ABC, Turtle):   
    # Geometric figure class, inheriting the turtle class
    def __init__(
        self,pen_color :str= 'black',fill_color :str='white', pen_size :int= 1
        ) -> None:
        """Initializes the main attributes geometric figure.
	:pen_color: turtle pen color
	:type pen_color: str
	:fill_color: fill color in turtle
	:type fill_color: str
 	:pen_size: value for pensize
	:type pen_size: int
	:return: None
	"""
        super().__init__()
        self._pen_color = pen_color
        self._fill_color = fill_color
        self._pen_size = pen_size
        self.set_fill_color(self._fill_color)
        self.set_pen_color(self._pen_color)
        self.set_pen_size(self._pen_size)
        
               
    def go_to(self, x :int|float=0, y :int|float=0):
        """"Go to the x,y point without drawing.
        :x: x coord
	    :type x: int | float
	    :y: x coord
	    :type y: int | float
        """
        self.penup()
        self.goto(x, y)
        self.pendown()
        
    def set_fill_color(self, fill_color :str):
        '''Change fill color'''
        self.fillcolor(fill_color)
    
    def set_pen_color(self, color :str):
        '''Change pen color'''
        self.pencolor(color)
    
    def set_pen_size(self, size :int):
        '''Change pen size'''
        self.pensize(size)       
    
        
    @abstractmethod
    def draw(self):
        pass