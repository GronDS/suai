from turtle import Turtle, done, Screen

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
        try:
            if type(order) == list and len(order) == 2:
                self.__order: list = order
            elif type(order) != list:
                raise TypeError("Cell incorrect type!")
            elif len(order) != 2:
                raise ValueError("Cell incorrect value!")
            else:
                raise Exception('Error!')
        except (TypeError, ValueError, Exception) as error:
            print(error)
            raise
        
        self.__occupied: bool = False
        self.pensize(3)
        self.hideturtle()
        
    @property
    def order(self):
        return self.__order

    @order.setter
    def order(self, order):
        # try:
        if type(order) == list and len(order) == 2:
            self.__order = order
        elif type(order) != list:
            print("Cell incorrect type!")
            # raise TypeError("Cell incorrect type!")
        elif len(order) != 2:
            print("Cell incorrect value!")
            # raise ValueError("Cell incorrect value!")
        else:
            print("Error!")
            # raise Exception('Error!')
        # except (TypeError, ValueError, Exception) as error:
        #     print(error)
        #     raise
            
            
    @property
    def occupied(self):
        return self.__occupied

    @occupied.setter
    def occupied(self, occupied):
        if type(occupied) == bool:
                self.__occupied = occupied
        else:
            raise ValueError("Incorrect Cell.occupied value")
    
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
    test_cell = Cell([1,2])
    print(test_cell.order)
    test_cell.draw_cell(25, 0, 0)
    test_cell.occupied = False
    done()
    