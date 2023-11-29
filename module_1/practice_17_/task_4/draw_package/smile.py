import turtle as t

def draw_smile(x_pos, y_pos):
    t.pensize(5)
    t.fillcolor('yellow')
    t.hideturtle()

    radius=45
    t.penup()
    t.setposition(x_pos, y_pos - radius)
    t.setheading(0)
    t.pendown()
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

    mouth_radius=radius*0.6
    mouth_angle=70
    t.penup()
    t.setposition(x_pos, y_pos - mouth_radius)
    t.setheading(0)
    t.pendown()
    t.circle(mouth_radius,mouth_angle)
    t.penup()
    t.setposition(x_pos, y_pos - mouth_radius)
    t.setheading(0)
    t.pendown()
    t.circle(mouth_radius,-mouth_angle)

    x=12.5
    y=12.5
    eye_size=15
    t.penup()
    t.setposition(x_pos + x, y_pos + y)

    t.pendown()
    t.dot(eye_size)
    t.penup()
    t.setposition(x_pos - x, y_pos + y)
    t.dot(eye_size)
    t.hideturtle()
        
if __name__ == '__main__':
    draw_smile(200, -100)
    