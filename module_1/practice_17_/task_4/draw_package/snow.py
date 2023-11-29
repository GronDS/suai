import turtle
from random import randint

turtle = turtle.Turtle()
# turtle.shape("turtle")

def draw_snowflake():
    turtle.speed(500)
    turtle.pensize(1)
    turtle.color("#0033FF")
    turtle.left(90)

    for i in range(0,6):
        turtle.forward(12.5)
        turtle.forward(-5)
        turtle.left(40)
        turtle.forward(3.75)
        turtle.forward(-3.75)
        turtle.right(80)
        turtle.forward(3.75)
        turtle.forward(-3.75)
        turtle.left(40)
        turtle.forward(-7.5)
        turtle.right(60)

def move_position(pos_x, pos_y):
    turtle.penup()
    turtle.setpos(pos_x, pos_y)
    turtle.pendown()
def draw_snow(pos_x, pos_y):
    for i in range(40):
        a = randint(pos_x, pos_x + 200)
        b = randint(pos_y, pos_y + 200)
        move_position(a, b)
        draw_snowflake()
        turtle.hideturtle()
if __name__ == '__main__':
    draw_snow(0, 0)
    