from turtle import *

def draw_tree(pos_x, pos_y):
    speed('fastest') 
    penup()
    setpos(pos_x, pos_y)
    pendown()  
    angle = 30 
    def y(sz, level):
    
        if level > 0: 
            colormode(255) 
            pencolor(0, 255//level, 0) 
            
            # drawing the base 
            fd(sz)   
            rt(angle) 
            # the right subtree 
            y(0.8 * sz, level-1) 
            
            pencolor(0, 255//level, 0) 
            
            lt( 2 * angle ) 
    
            # the left subtree 
            y(0.8 * sz, level-1) 
            
            pencolor(0, 255//level, 0) 
            
            rt(angle) 
            fd(-sz)   
    y(80, 7)
    hideturtle()
    
if __name__ == '__main__':
    draw_tree(200, -300)