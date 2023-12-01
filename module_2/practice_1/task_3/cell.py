from turtle import Turtle, done

class Cell(Turtle):
    # Cell for a tic-tac-toe board, inheriting the turtle class
    def __init__(self, order :list[int]= [0, 0]) -> None:
        """Initializes the main attributes of the cell.
	:order: cell position on the board
	:type order: list[int]
	:__occupied: cell occupancy status
	:type __occupied: bool
	:return: None
	"""
        super().__init__()
        self.__order: list = order
        self.__occupied: bool = False
        self.pensize(3)
        self.hideturtle()
        
    @property
    def order(self):
        return self.__order

    @order.setter
    def order(self, order):
        if type(order) == list:
            self.__order = order
        else:
            print("Incorrect value!")
            
    @property
    def occupied(self):
        return self.__occupied

    @occupied.setter
    def occupied(self, occupied):
        if type(occupied) == bool:
                self.__occupied = occupied
        else:
            print("Incorrect value")
    
    def draw_cell(self, cell_len, x, y):
        # Drawing a cell using a turtle 
        self.speed(0)
        self.penup()
        self.goto(x, y)
        self.pendown()
        for _ in range(4):
            self.forward(cell_len)
            self.left(90)
        self.penup()
        self.forward(cell_len)
        
    def draw_black_cell(self, cell_len, x, y):
        # Drawing a black cell using a turtle 
        self.speed(0)
        self.penup()
        self.goto(x, y)
        self.pendown()
        self.color('black', 'black')
        self.begin_fill()
        self.draw_cell(cell_len, x, y)
        self.end_fill()
        self.penup()

if __name__ == '__main__':    
    pass
