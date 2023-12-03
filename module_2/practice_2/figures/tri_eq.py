from tri import *
class Equilateral_Triangle(Triangle):
        
    def draw(self, x: int | float = 0, y: int | float = 0):
        return super().draw(x, y)
    
if __name__ == '__main__':
    my_trngl = Equilateral_Triangle(pen_size=4, pen_color='red',
                                    fill_color='white', base_len=100)
    my_trngl.draw(200, 50)
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