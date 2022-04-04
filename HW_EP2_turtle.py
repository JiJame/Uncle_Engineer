import turtle
tao = turtle.Pen()
tao.shape('turtle')

def draw():
    for i in range(8):
        tao.forward(100)
        tao.left(45)

def warp(x,y):
    tao.penup()
    tao.goto(x,y)
    tao.pendown()

def fuction():
    x=0
    y=0
    for i in range(5):
        draw()
        warp(x,y)
        x=x+10
        y=y+10

    while x>=50 and y<=50 and x<51 and y<51:
        for i in range(3):
            tao.forward(100)
            tao.circle(30)
            x=x+1
            y=y+1

fuction()
    



