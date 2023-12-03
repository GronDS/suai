from oval import *


class Ellipse(Oval):
    # Ellipse class 
    def draw(self, x :int|float=0, y :int|float=0):
        """"Draw ellipse.
        :x: x coord
	    :type x: int | float
	    :y: x coord
	    :type y: int | float
        """
        return super().draw(x, y)

if __name__ == '__main__':
    ellipse_1 = Ellipse('red', 'yellow', 2, 100, 70)
    ellipse_1.draw(1, 2)
    done()