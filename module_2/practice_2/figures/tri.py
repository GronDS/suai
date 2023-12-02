from figure import *
class Triangle(Figure):
    
    def __init__(
        self, pos_x: int|float = 0, pos_y: int|float=0,
        pen_color: str='black', fill_color: str= 'white', pen_size: int=1,
        base_len :int|float=100
        ) -> None:
        super().__init__(pos_x, pos_y, pen_color,fill_color, pen_size)
        self._base_len = base_len
        
    def draw(self, x, y):
        self.begin_fill()
        self.go_to(x, y)
        self.forward(self._base_len)
        self.left(120)
        self.forward(self._base_len)
        self.left(120)
        self.forward(self._base_len)
        self.setheading(0)
        self.end_fill()

if __name__ =='__main__':
    my_trngl = Triangle(pos_x=200, pos_y=50,pen_size=4, pen_color='red',fill_color='white', base_len=100)
    my_trngl.draw(200, -50)
    my_trngl.set_pen_size(1)
    my_trngl.set_fill_color('black')
    my_trngl.draw(my_trngl._pos_x, my_trngl._pos_y)
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
    my_trngl.set_pen_size(12)
    my_trngl._base_len = 500
    my_trngl.set_pen_color('orange')
    my_trngl.set_fill_color('blue')
    my_trngl.draw(-300, 300)
    done()