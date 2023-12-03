from figure import *
from tri_isos import Isosceles_Triangle
from tri_eq import Equilateral_Triangle
from tri_right import Right_Triangle
from circle import Circle
from ellipse import Ellipse


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

    done()