from figures import *
#x and y let the user place their numbers down, d is length of sides.
class Nine(Figures):
       
    def draw(self, d):
        self.speed(0)
        self.penup()
        self.goto(self._pos_x, self._pos_y)
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
        
class Eight(Figures):
       
    def draw(self, d):
        self.speed(0)
        self.penup()
        self.goto(self._pos_x, self._pos_y)
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

class Seven(Figures):

    def draw(self, d):
        self.speed(0)
        self.penup()
        self.goto(self._pos_x, self._pos_y)
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

class Six(Figures):
        
    def draw(self, d):
        self.speed(0)
        self.penup()
        self.goto(self._pos_x, self._pos_y)
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
        
class Five(Figures):
    
    def draw(self, d):
        self.speed(0)
        self.penup()
        self.goto(self._pos_x, self._pos_y)
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
        
class Four(Figures):
    
    def draw(self, d):
        self.speed(0)
        self.penup()
        self.goto(self._pos_x, self._pos_y)
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
        
class Three(Figures):
    
    def draw(self, d):
        self.speed(0)
        self.penup()
        self.goto(self._pos_x, self._pos_y)
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

class Two(Figures):
    
    def draw(self, d):
        self.speed(0)
        self.penup()
        self.goto(self._pos_x, self._pos_y)
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
        
class One(Figures):
    
    def draw(self, d):
        self.speed(0)
        self.penup()
        self.goto(self._pos_x, self._pos_y)
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

numbers = {
    1 : One,
    2 : Two,
    3 : Three,
    4 : Four,
    5 : Five,
    6 : Six,
    7 : Seven,
    8 : Eight,
    9 : Nine
    }

def drawnum(d: int|float, n :int, x :int|float, y :int|float):
    try:
        if type(n) != int:
            raise TypeError('Wrong type of number value!')
        if n not in range(1, 10):
            raise ValueError('Number value out of board range!')
        if type(d) != int and type(d) != float:
            raise TypeError('Wrong type of sides lenght value!')
        if type(x) != int and type(x) != float:
            raise TypeError('Wrong X type!')
        if type(y) != int and type(y) != float:
            raise TypeError('Wrong Y type!')                
    except (TypeError, ValueError) as error:
        print(error)
        raise
    else:
        numbers[n](x ,y).draw(d)
        
if __name__ == '__main__':
    drawnum(100, 9, -100, -100)
    done()
    # pass