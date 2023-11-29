import turtle
import math

from draw_package.house.figures import drawParallelogram, drawRectangle, drawTriangle

turtle = turtle.Turtle()
turtle.speed(5)



def front_house(pos_x, pos_y):
  turtle.penup() 
  turtle.goto(pos_x - 30, pos_y)
  turtle.pendown()
  drawRectangle(turtle, 200, 220, "brown")

def draw_front_door(pos_x, pos_y):
  turtle.penup()
  turtle.goto(pos_x, pos_y)
  turtle.pendown()
  drawRectangle(turtle, 80, 120, "lightgreen")

def draw_front_roof(pos_x, pos_y):
  turtle.penup()
  turtle.goto(pos_x - 30, pos_y + 220)
  turtle.pendown()
  drawTriangle(turtle, 200, "orange")

def draw_side_house(pos_x, pos_y):
  turtle.penup()
  turtle.goto(pos_x + 170, pos_y)
  turtle.pendown()
  drawParallelogram(turtle, 120, 220, "brown")

def draw_window(pos_x, pos_y):
  turtle.penup()
  turtle.goto(pos_x + 200, pos_y + 90)
  turtle.pendown()
  drawParallelogram(turtle, 40, 60, "white")

def draw_side_roof(pos_x, pos_y):
  turtle.penup()
  turtle.goto(pos_x + 170, pos_y +220)
  turtle.pendown()
  turtle.fillcolor("orange")
  turtle.begin_fill()
  turtle.left(30)
  turtle.forward(120)
  turtle.left(105)
  turtle.forward(200 / math.sqrt(2))
  turtle.left(75)
  turtle.forward(120)
  turtle.left(105)
  turtle.forward(200 / math.sqrt(2))
  turtle.left(45)
  turtle.end_fill()


def main_house(pos_x, pos_y):
  front_house(pos_x, pos_y)
  draw_front_door(pos_x, pos_y) 
  draw_front_roof(pos_x, pos_y)
  draw_side_house(pos_x, pos_y)
  draw_window(pos_x, pos_y)
  draw_side_roof(pos_x, pos_y)
  turtle.penup()
  turtle.hideturtle()

if __name__ == '__main__':
  main_house(-120, -120)