'''На координатной плоскости рисуются круги, у каждого круга следующие 
 параметры: координаты X и Y центра круга и значение R ―  радиус круга. По 
 умолчанию центр находится в (0, 0), а радиус равен 1.
Реализуйте класс «Круг», который инициализируется по этим параметрам. 
Круг также может:
1. Находить и возвращать свою площадь.
2. Находить и возвращать свой периметр.
3. Увеличиваться в K раз.
4. Определять, пересекается ли он с другой окружностью.'''

from turtle import Turtle, done
from math import pi, sqrt


class Circle(Turtle):
    def __init__(self, pos_x :int|float=0, pos_y :int|float=0, 
                 radius :int|float=1, color :str='black') -> None:
        super().__init__()
        self.__pos_x = pos_x
        self.__pos_y = pos_y
        self.__radius = radius
        self.__color: str = color
    
    def __str__(self) -> str:
        return f'init circle in point {self.__pos_x, self.__pos_y}, \
rad = {self.__radius}'
    
    @property
    def pos_x(self):
        return self.__pos_x
    
    @pos_x.setter
    def pos_x(self, pos_x):
        if type(pos_x) == int or type(pos_x) == float:
            self.__pos_x = pos_x
        else:
            print("Incorrect X format!")

    @property
    def pos_y(self):
        return self.__pos_y
    
    @pos_y.setter
    def pos_y(self, pos_y):
        if type(pos_y) == int or type(pos_y) == float:
            self.__pos_y = pos_y
        else:
            print("Incorrect Y format!")    

    @property
    def radius(self):
        return self.__radius
    
    @radius.setter
    def radius(self, radius):
        if type(radius) == int or type(radius) == float:
            self.__radius = radius
        else:
            print("Incorrect radius format!")

    @property
    def color(self):
        return self.__color
    
    @color.setter
    def color(self, color):
        if type(color) == str:
            self.__color = color
        else:
            print("Incorrect color format!")
  
    def show_perimeter(self):
        self.__perimeter: float = 2 * pi * self.radius
        return self.__perimeter
     
    def show_area(self):
        self.__area: float = pi * (self.radius ** 2)
        return self.__area
        
    def __mul__(self, k=2):
        self.radius *= k
        return Circle(self.pos_x, self.pos_y, self.radius, self.color)
    
        
    def check_intersect(self, other):
        range_beetween: float = sqrt(((self.pos_x - other.pos_x) ** 2) + 
            ((self.pos_y - other.pos_y) ** 2))
        rad_summ: float = self.radius + other.radius
        if range_beetween <= rad_summ:
            return 'Circles intersect'
        else:
            return 'Circles do not intersect'
            
    def draw(self):
        self.penup()
        self.pencolor(self.color)
        self.fillcolor(self.color)
        self.setpos(self.pos_x, self.pos_y - self.radius)
        self.pendown()
        self.begin_fill()
        self.circle(self.radius)
        self.end_fill()
        

if __name__ == '__main__':
    circle_1 = Circle(radius=40)
    print(circle_1)
    circle_2 = Circle(pos_x=100, radius=40, color='yellow')
    print(circle_2)
    print(circle_1.show_area())
    print(circle_1.show_perimeter())
    circle_1.draw()
    circle_2.draw()
    print(circle_1.check_intersect(circle_2))
    circle_1 = circle_1 * 2
    circle_1.draw()
    print(circle_1.check_intersect(circle_2))
    done()