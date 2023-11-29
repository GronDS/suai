import turtle 
t = turtle.Turtle()
 
def drawFourRats(pos_t, length, radius):
     
    for i in range(4):
        pos_t.penup()
        pos_t.forward(radius)
        pos_t.pendown()
        pos_t.forward(length)
        pos_t.penup()
        pos_t.backward(length + radius)
        pos_t.left(90)
 
def draw_sun(pos_x, pos_y):
    t.penup()
    t.goto(pos_x, pos_y)
    t.fillcolor("yellow")
    t.pendown()
    t.begin_fill()
    t.circle(45)
    t.end_fill()
    
    t.penup()
    t.goto(pos_x, pos_y + 59)
    t.pendown()
    drawFourRats(t, 85, 54)
    t.right(45)
    drawFourRats(t, 85, 54)
    t.left(45)
    t.hideturtle()

if __name__ == '__main__':
    draw_sun(-150, 150)