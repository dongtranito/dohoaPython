
import turtle 

#đây là hàm vẽ hệ tọa độ
# hideturtle()
def drawOxy(t):
    t.hideturtle()
    t.pensize(2)
    t.color('red')

    t.penup()
    t.goto(-1000, 0)

    t.pendown()
    t.forward(2000)

    t.penup()
    t.forward(10)
    t.write('x', align='left', font=('arial', 14, 'normal'))
    t.pendown()
    t.right(90)
    t.penup()

    t.goto(0,0)
    t.pensize(1)
    for i in range(0, 1000, 5):
        t.goto(i, 3)
        t.pendown()
        t.forward(6)
        t.penup()

    t.goto(0, 0)
    for i in range(0, 1000, 5):
        t.goto(-i, 3)
        t.pendown()
        t.forward(6)
        t.penup()

    t.goto(0, 0)

    t.pendown()
    t.forward(1000)
    t.right(180)
    t.forward(2000)

    t.penup()
    t.forward(10)
    t.write('y', align='left', font=('arial', 14, 'normal'))
    t.pendown()

    t.penup()
    t.goto(0, 0)
    t.right(90)

    for i in range(0, 1000, 5):
        t.goto(-3, i)
        t.pendown()
        t.forward(6)
        t.penup()

    t.goto(0, 0)
    for i in range(0, 1000, 5):
        t.goto(-3, -i)
        t.pendown()
        t.forward(6)
        t.penup()

    t.penup()
    t.goto(0, 0)
    t.right(180)
    # turtle.update()


# def drawPoint(x,y):
#     t1 = turtle.RawTurtle(ui.screen)
#     t1.penup()
#     t1.goto(x, y)
#     t1.pendown()
#     t1.dot('10', 'blue')
#     t1.write(f'({int(x/5)}, {int(y/5)})', align= 'left', font=('arial', 14, 'normal'))


def drawOxy3d(t):
    t.clear()
    t.pensize(2)
    t.color('red')

    t.penup()
    t.goto(0, 0)
    
    t.pendown()
    t.forward(500)

    t.penup()
    t.forward(10)
    t.write('x', align='left', font=('arial', 14, 'normal'))
    t.pendown()
    t.right(90)
    t.penup()

    t.goto(0,0)
    t.pensize(1)
    for i in range(0, 500, 5):
        t.goto(i, 3)
        t.pendown()
        t.forward(6)
        t.penup()

    t.goto(0, 0)

    t.pensize(2)
    t.pendown()
    t.right(180)
    t.forward(350)

    t.penup()
    t.forward(10)
    t.write('z', align='left', font=('arial', 14, 'normal'))
    t.pendown()

    t.penup()
    t.goto(0, 0)
    t.right(90)

    t.pensize(1)
    for i in range(0, 350, 5):
        t.goto(-3, i)
        t.pendown()
        t.forward(6)
        t.penup()


    t.penup()
    t.goto(0, 0)
    t.pensize(2)
    t.pendown()
    t.goto(-300, -300)

    t.penup()
    t.forward(30)
    t.write('y', align='left', font=('arial', 14, 'normal'))
    t.pendown()

    t.penup()
    t.goto(0, 0)
    
    t.pensize(1)
    t.right(45)
    for i in range(0, 300, 5):
        t.goto(-i-3,-i)
        t.pendown()
        t.forward(6)
        t.penup()
    t.left(45)

# if __name__=="__main__":
#     tracer(0)
#     drawOxy()
#     onscreenclick(drawPoint)
#     update()
#     # giữ cho màn hình ko tắt khi vẽ xong để bắt sự kiện
#     mainloop()