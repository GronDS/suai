from figures import Figure, done, sin, cos, radians, pi
from figures import Isosceles_Triangle
from figures import Equilateral_Triangle
from figures import Right_Triangle
from figures import Circle
from figures import Ellipse
from figures import Parallelogram
from figures import Rectangle
from figures import Rhombus
from figures import Square
from figures import Trapezoid

if __name__ == '__main__':
    isos_1 = Isosceles_Triangle('white','yellow',base_angle=30)
    isos_1.draw(0, 0)
    eq_1 = Equilateral_Triangle('red','blue',2, 200)
    eq_1.draw(100, 200)
    right_1 = Right_Triangle('green', 'pink', 5, 50, 100)
    right_1.draw(-100, -200)
    circ_1 = Circle('pink', 'grey', 3, 60)
    circ_1.draw(-100, -100)
    circ_2 = Ellipse(main_radius=30, second_radius= 50)
    circ_2.draw(-150)
    rect_1 = Rectangle(pen_size= 5, first_side= 100, second_side= 20)
    rect_1.draw(200, -200)
    rhomb_1 = Rhombus('brown', 'purple', 2, 50, 120)
    rhomb_1.draw(200, 100)
    square_1 = Square('orange', 'indigo', 10, 200)
    square_1.draw(-350, -350)
    trapez_1 = Trapezoid ('white', 'red', 1, 300, 90, 150, 70)
    trapez_1.draw(-200, 200)
    done()