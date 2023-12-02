from figure import *
from tri_isos import Isosceles_Triangle
from tri_eq import Equilateral_Triangle
from tri_right import Right_Triangle
from circle import Circle
from ellipse import Ellipse


if __name__ == '__main__':
    isos_1 = Isosceles_Triangle(0,0,'white','yellow',base_angle=30)
    isos_1.draw(0, 0)
    eq_1 = Equilateral_Triangle(0,0,'red','blue',2, 200)
    eq_1.draw(100, 200)
    right_1 = Right_Triangle(100, 200, 'green', 'pink', 5, 50, 100)
    right_1.draw(-100, -200)
    circ_1 = Circle(-100, -100, 'pink', 'grey', 3, 60)
    circ_1.draw(circ_1._pos_x, circ_1._pos_y)
    circ_2 = Ellipse(main_radius=30, second_radius= 50)
    circ_2.draw()

    done()