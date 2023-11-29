from turtle import *


turtle = Turtle()

def semi_cir(color, rad, val):
    turtle.up()
    turtle.setpos(val + 100, 75)
    turtle.down()
    turtle.color(color)
    turtle.circle(rad, -180)
    turtle.up()
    turtle.setpos(val + 100, 75)
    turtle.down()
    turtle.right(180)

def draw_rainbow():
    color = ['violet', 'indigo', 'blue', 'green', 'yellow', 'orange', 'red']
    turtle.right(90)
    turtle.width(20)
    turtle.speed(7)
    for i in range(7):
        semi_cir(color[i], 10*(i+30), -10*(i+1))
    hideturtle()


if __name__ == '__main__':
    draw_rainbow()
