from figures.tri import *

class Right_Triangle(Triangle):
    # Right triangle class  
    def __init__(self, pen_color: str = 'black', fill_color: str = 'white', 
                 pen_size: int = 1, base_len: int | float = 100, 
                 second_len: int | float = 100) -> None:
        """
        :second_len: vertical triangle leg length
        :type second_len: int | float
        """
        super().__init__(pen_color, fill_color, pen_size, base_len)
        self.__second_len = second_len
        
    def draw(self, x :int|float=0, y :int|float=0):
        """"Draw right triangle.
        :x: x coord
	    :type x: int | float
	    :y: x coord
	    :type y: int | float
        """
        self.begin_fill()
        self.go_to(x, y)
        self.forward(self._base_len)
        self.left(90)
        self.forward(self.__second_len)
        self.goto(x, y)
        self.setheading(0)
        self.end_fill()
        
if __name__ == '__main__':
    my_trngl = Right_Triangle(pen_size=4,
                            pen_color='red',fill_color='white', base_len=100,
                            second_len=200)
    my_trngl.draw(200, -50)
    my_trngl.set_pen_size(1)
    my_trngl.set_fill_color('black')
    my_trngl.draw(0, 0)
    my_trngl.set_pen_size(5)
    my_trngl.set_pen_color('black')
    my_trngl.set_fill_color('blue')
    my_trngl.draw(300, 300)
    my_trngl.set_pen_size(2)
    my_trngl.set_pen_color('yellow')
    my_trngl.set_fill_color('black')
    my_trngl.draw(-300, -300)
    my_trngl.set_pen_size(6)
    my_trngl.set_pen_color('blue')
    my_trngl.set_fill_color('red')
    my_trngl.draw(300, -300)
    my_trngl.set_pen_size(9)
    my_trngl._base_len = 200
    my_trngl.set_pen_color('orange')
    my_trngl.set_fill_color('blue')
    my_trngl.draw(-300, 200)
    done()