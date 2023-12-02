from oval import *


class Ellipse(Oval):
    
    def draw(self, x :int|float=0, y :int|float=0):
        return super().draw(x, y)

if __name__ == '__main__':
    ellipse_1 = Ellipse(1, 2, 'red', 'yellow', 2, 100, 70)
    ellipse_1.draw(ellipse_1._pos_x, ellipse_1._pos_y)
    done()