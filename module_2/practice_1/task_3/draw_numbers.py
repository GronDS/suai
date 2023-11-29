from figures import *

#x and y let the user place their numbers down, d is length of sides.
class Nine(Figures):
    
    def __init__(self, pos_x: int | float, pos_y: int | float) -> None:
        super().__init__(pos_x, pos_y)
        
    def draw_nine(self, d, x, y):
        self.speed(0)
        self.penup()
        self.goto(x, y)
        self.pendown()
        point = self.pos()
        self.forward(d)
        self.right(90)
        self.forward(d*2)
        self.back(d)
        self.right(90)
        self.forward(d)
        self.right(90)
        self.forward(d)
        self.penup()
        self.goto(point)
        self.pendown()
        self.setheading(0)
        self.hideturtle()
        
class Eight(Figures):
    
    def __init__(self, pos_x: int | float, pos_y: int | float) -> None:
        super().__init__(pos_x, pos_y)
        
    def draw_eight(self, d, x, y):
        self.speed(0)
        self.penup()
        self.goto(x, y)
        self.pendown()
        point = self.pos()
        self.forward(d)
        self.right(90)
        self.forward(d*2)
        for i in range(3):
            self.right(90)
            self.forward(d)
        self.back(d)
        self.left(90)
        self.forward(d)
        self.penup()
        self.goto(point)
        self.pendown()
        self.setheading(0)
        self.hideturtle()

class Seven(Figures):
    
    def __init__(self, pos_x: int | float, pos_y: int | float) -> None:
        super().__init__(pos_x, pos_y)
        
    def draw_seven(self, d, x, y):
        self.speed(0)
        self.penup()
        self.goto(x, y)
        self.pendown()
        point = self.pos()
        self.forward(d)
        self.right(90)
        self.forward(d*2)
        self.back(d*2)
        self.left(90)
        self.back(d)
        self.penup()
        self.goto(point)
        self.pendown()
        self.setheading(0)
        self.hideturtle()

class Six(Figures):
    
    def __init__(self, pos_x: int | float, pos_y: int | float) -> None:
        super().__init__(pos_x, pos_y)
        
    def draw_six(self, d, x, y):
        self.speed(0)
        self.penup()
        self.goto(x, y)
        self.pendown()
        point = self.pos()
        self.forward(d)
        self.back(d)
        self.right(90)
        self.forward(d*2)
        for i in range(3):
            self.left(90)
            self.forward(d)
        self.right(90)
        self.forward(d)
        self.penup()
        self.goto(point)
        self.pendown()
        self.setheading(0)
        self.hideturtle()
        
class Five(Figures):
    
    def __init__(self, pos_x: int | float, pos_y: int | float) -> None:
        super().__init__(pos_x, pos_y)
        
    def draw_five(self, d, x, y):
        self.speed(0)
        self.penup()
        self.goto(x, y)
        self.pendown()
        point = self.pos()
        self.forward(d)
        self.back(d)
        self.right(90)
        self.forward(d)
        self.left(90)
        self.forward(d)
        for i in range(2):
            self.right(90)
            self.forward(d)
        self.penup()
        self.goto(point)
        self.pendown()
        self.setheading(0)
        self.hideturtle()
        
class Four(Figures):
    
    def __init__(self, pos_x: int | float, pos_y: int | float) -> None:
        super().__init__(pos_x, pos_y)
        
    def draw_four(self, d, x, y):
        self.speed(0)
        self.penup()
        self.goto(x, y)
        self.pendown()
        point = self.pos()
        self.right(90)
        self.forward(d)
        for i in range(2):
            self.left(90)
            self.forward(d)
        self.back(d * 2)
        self.penup()
        self.goto(point)
        self.pendown()
        self.setheading(0)
        self.hideturtle()
        
class Three(Figures):
    
    def __init__(self, pos_x: int | float, pos_y: int | float) -> None:
        super().__init__(pos_x, pos_y)
        
    def draw_three(self, d, x, y):
        self.speed(0)
        self.penup()
        self.goto(x, y)
        self.pendown()
        point = self.pos()
        for i in range(2):
            self.forward(d)
            self.right(90)
        self.forward(d)
        for i in range(2):
            self.back(d)
            self.right(90)
        self.back(d)
        self.penup()
        self.goto(point)
        self.pendown()
        self.setheading(0)
        self.hideturtle()

class Two(Figures):
    
    def __init__(self, pos_x: int | float, pos_y: int | float) -> None:
        super().__init__(pos_x, pos_y)
        
    def draw_two(self, d, x, y):
        self.speed(0)
        self.penup()
        self.goto(x, y)
        self.pendown()
        point = self.pos()
        self.forward(d)
        self.right(90)
        self.forward(d)
        self.left(90)
        for i in range(2):
            self.back(d)
            self.left(90)
        self.back(d)
        self.penup()
        self.goto(point)
        self.pendown()
        self.setheading(0)
        self.hideturtle()
        
class One(Figures):
    
    def __init__(self, pos_x: int | float, pos_y: int | float) -> None:
        super().__init__(pos_x, pos_y)
        
    def draw_one(self, d, x, y):
        self.speed(0)
        self.penup()
        self.goto(x, y)
        self.pendown()
        point = self.pos()
        self.penup()
        self.forward(d)
        self.pendown()
        self.right(90)
        self.forward(d*2)
        self.penup()
        self.goto(point)
        self.pendown()
        self.setheading(0)
        self.hideturtle()

numbers = {
    1 : One(0, 0).draw_one,
    2 : Two(0, 0).draw_two,
    3 : Three(0, 0).draw_three,
    4 : Four(0, 0).draw_four,
    5 : Five(0, 0).draw_five,
    6 : Six(0, 0).draw_six,
    7 : Seven(0, 0).draw_seven,
    8 : Eight(0, 0).draw_eight,
    9 : Nine(0, 0).draw_nine
    }

t = Turtle()

def drawnum(d, n, x, y): 
    numbers[n](d, x, y)
    t.penup()
    t.forward(1.5*d)
    t.pendown()
    
if __name__ == '__main__':
    drawnum(100, 9, -100, -100)
    done()
    #pass