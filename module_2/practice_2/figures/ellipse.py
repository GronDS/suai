from oval import *


class Ellipse(Oval):
    
    def draw(self, x :int|float=0, y :int|float=0):
        return super().draw(x, y)

if __name__ == '__main__':
    ellipse_1 = Ellipse('red', 'yellow', 2, 100, 70)
    ellipse_1.draw(1, 2)
    done()