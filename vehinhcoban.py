
import turtle
import math
import time 
import numpy as np
from phepdoihinh import tinhtien 

netve=7
turtle.tracer(0)

def draw_circle(t,A,radius):  # A là tâm
    t.hideturtle()
    t.speed(0)
    t.penup()
    
    # Hàm vẽ đối xứng 8 điểm

    def vedoixung(x, y):
        x = x * 5 
        y = y * 5 # cái này có nghĩa là 5pixel 1 đơn vị, phải nhớ là có cái này mới được 

        x0,y0=tinhtien([x,y],A[0]*5,A[1]*5)  #thêm dòng này để thực hiện phép tịnh tiến 
        t.goto(x0, y0)
        t.dot(netve)

        x1, y1 = -x, y
        x1,y1=tinhtien([x1,y1],A[0]*5,A[1]*5)

        t.goto(x1, y1)
        t.dot(netve)

        x2, y2 = -x, -y
        x2,y2=tinhtien([x2,y2],A[0]*5,A[1]*5)
        t.goto(x2, y2)
        t.dot(netve)

        x3, y3 = x, -y
        x3,y3=tinhtien([x3,y3],A[0]*5,A[1]*5)

        t.goto(x3, y3)
        t.dot(netve)

        x4, y4 = y, x
        x4,y4=tinhtien([x4,y4],A[0]*5,A[1]*5)

        t.goto(x4, y4)
        t.dot(netve)

        x5, y5 = y, -x
        x5,y5=tinhtien([x5,y5],A[0]*5,A[1]*5)

        t.goto(x5, y5)
        t.dot(netve)

        x6, y6 = -y, x
        x6,y6=tinhtien([x6,y6],A[0]*5,A[1]*5)

        t.goto(x6, y6)
        t.dot(netve)

        x7, y7 = -y, -x
        x7,y7=tinhtien([x7,y7],A[0]*5,A[1]*5)

        t.goto(x7, y7)
        t.dot(netve)

    # Thuật toán Bresenham để vẽ hình tròn
    x = 0
    y = radius
    p = 3 - 2 * radius
    count = 0
    while x <= radius * math.sqrt(2) / 2:
        vedoixung(x, y)
        if p < 0:
            p = p + 4 * x + 6
        else:
            p = p + 4 * (x - y) + 10
            y = y - 1
        x += 1
        count += 1

    



def draw_ellipse(t,A,a, b,c=0):

    t.penup()
    t.goto(A[0]*5,A[1]*5)
    t.dot(8)
    def vedoixung(x, y,count):
        t.hideturtle()
        t.speed(0)
        t.penup()
        x=x*5
        y=y*5
        # vẽ nữa trên
        if c==0:
            if count %5<3:
                x0,y0=tinhtien([x,y],A[0]*5,A[1]*5)
                t.goto(x0, y0)
                t.dot(8)

                x1, y1 = -x, y
                x1,y1=tinhtien([x1,y1],A[0]*5,A[1]*5)
                t.goto(x1, y1)
                t.dot(8)
        else:
            x0,y0=tinhtien([x,y],A[0]*5,A[1]*5)
            t.goto(x0, y0)
            t.dot(8)

            x1, y1 = -x, y
            x1,y1=tinhtien([x1,y1],A[0]*5,A[1]*5)
            t.goto(x1, y1)
            t.dot(8)
        #vẽ nữa dưới
        x2, y2 = -x, -y
        x2,y2=tinhtien([x2,y2],A[0]*5,A[1]*5)
        t.goto(x2, y2)
        t.dot(8)

        x3, y3 = x, -y
        x3,y3=tinhtien([x3,y3],A[0]*5,A[1]*5)

        t.goto(x3, y3)
        t.dot(8)

    x, y = 0, b
    d1 = b**2 - a**2 * b + 0.25 * a**2
    count=0
    vedoixung(x,y,count)


    while a**2 * (y - 0.5) > b**2 * (x + 1):
        if d1 < 0:
            d1 += b**2 * (2 * x + 3)
        else:
            d1 += b**2 * (2 * x + 3) + a**2 * (-2 * y + 2)
            y -= 1
        x += 1
        count+=1
        vedoixung(x,y,count)

    d2 = b**2 * (x + 0.5)**2 + a**2 * (y - 1)**2 - a**2 * b**2

    while y > 0:
        if d2 < 0:
            d2 += b**2 * (2 * x + 2) + a**2 * (-2 * y + 3)
            x += 1
        else:
            d2 += a**2 * (-2 * y + 3)
        y -= 1
        count+=1
        vedoixung(x,y,count)


def draw_circleleft(t,A,radius):  # A là tâm
    t.hideturtle()
    t.speed(0)
    t.penup()
    
    # Hàm vẽ đối xứng 8 điểm

    def vedoixung(x, y):
        x = x * 5 
        y = y * 5 # cái này có nghĩa là 5pixel 1 đơn vị, phải nhớ là có cái này mới được 


        x1, y1 = -x, y
        x1,y1=tinhtien([x1,y1],A[0]*5,A[1]*5)
        t.goto(x1, y1)
        t.dot(netve)

        x2, y2 = -x, -y
        x2,y2=tinhtien([x2,y2],A[0]*5,A[1]*5)
        t.goto(x2, y2)
        t.dot(netve)


        x6, y6 = -y, x
        x6,y6=tinhtien([x6,y6],A[0]*5,A[1]*5)
        t.goto(x6, y6)
        t.dot(netve)

        x7, y7 = -y, -x
        x7,y7=tinhtien([x7,y7],A[0]*5,A[1]*5)
        t.goto(x7, y7)
        t.dot(netve)

    # Thuật toán Bresenham để vẽ hình tròn
    x = 0
    y = radius
    p = 3 - 2 * radius
    count = 0
    while x <= radius * math.sqrt(2) / 2:
        vedoixung(x, y)
        if p < 0:
            p = p + 4 * x + 6
        else:
            p = p + 4 * (x - y) + 10
            y = y - 1
        x += 1
        count += 1



def draw_circleright(t,A,radius):  # A là tâm
    t.hideturtle()
    t.speed(0)
    t.penup()
    
    # Hàm vẽ đối xứng 8 điểm

    def vedoixung(x, y):
        x = x * 5 
        y = y * 5 # cái này có nghĩa là 5pixel 1 đơn vị, phải nhớ là có cái này mới được 

        x0,y0=tinhtien([x,y],A[0]*5,A[1]*5)  #thêm dòng này để thực hiện phép tịnh tiến 
        t.goto(x0, y0)
        t.dot(netve)

        x3, y3 = x, -y
        x3,y3=tinhtien([x3,y3],A[0]*5,A[1]*5)
        t.goto(x3, y3)
        t.dot(netve)

        x4, y4 = y, x
        x4,y4=tinhtien([x4,y4],A[0]*5,A[1]*5)
        t.goto(x4, y4)
        t.dot(netve)

        x5, y5 = y, -x
        x5,y5=tinhtien([x5,y5],A[0]*5,A[1]*5)
        t.goto(x5, y5)
        t.dot(netve)

    # Thuật toán Bresenham để vẽ hình tròn
    x = 0
    y = radius
    p = 3 - 2 * radius
    count = 0
    while x <= radius * math.sqrt(2) / 2:
        vedoixung(x, y)
        if p < 0:
            p = p + 4 * x + 6
        else:
            p = p + 4 * (x - y) + 10
            y = y - 1
        x += 1
        count += 1


def ve_doan_thang(t,A,B):
    t.hideturtle()
    t.speed(0)
    t.penup()
    x1=A[0]
    y1=A[1]
    x2=B[0]
    y2=B[1]
    dx = x2 - x1
    dy = y2 - y1
    steps = max(abs(dx), abs(dy))
    if steps != 0:
        x_increment = dx / steps
        y_increment = dy / steps
        current_x = x1
        current_y = y1
        for _ in range(steps):
            drawPoint(t,round(current_x), round(current_y))
            current_x += x_increment
            current_y += y_increment


def draw_filled_rectangle(t, A, B,color="lightblue"):
    x1 = A[0]
    y1 = A[1]
    x2 = B[0]
    y2 = B[1]

    width = abs(x2 - x1)
    height = abs(y2 - y1)

    start_x = min(x1, x2)
    start_y = min(y1, y2)

    t.penup()
    t.goto(start_x, start_y)
    t.pendown()

    ve_doan_thang(t, (start_x, start_y), (start_x + width, start_y))
    ve_doan_thang(t, (start_x + width, start_y), (start_x + width, start_y + height))
    ve_doan_thang(t, (start_x + width, start_y + height), (start_x, start_y + height))
    ve_doan_thang(t, (start_x, start_y + height), (start_x, start_y))

    t.begin_fill()
    t.fillcolor(color)

    ve_doan_thang(t, (start_x, start_y), (start_x + width, start_y))
    ve_doan_thang(t, (start_x + width, start_y), (start_x + width, start_y + height))
    ve_doan_thang(t, (start_x + width, start_y + height), (start_x, start_y + height))
    ve_doan_thang(t, (start_x, start_y + height), (start_x, start_y))

    t.end_fill()
def drawPoint(t,x, y):
    x=x*5
    y=y*5
    t.hideturtle()
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.dot(netve)


def dash_line(t,A,B):

    x1 = A[0]
    y1 = A[1]
    x2 = B[0]
    y2 = B[1]
    dash_length = 6
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    x_unit, y_unit = 1, 1
    p_i = dy - dx

    if x2 - x1 < 0:
        x_unit = -x_unit
    if y2 - y1 < 0:
        y_unit = -y_unit

    # write(f'({int(x1 / 5)}, {int(y1 / 5)})', align='left', font=('arial', 10, 'normal'))
   
    while True:
        if dash_length >= 3:
            drawPoint(t,x1,y1)
        dash_length -= 1
        if x1 == x2 and y1 == y2:
            break

        p = 2 * p_i
        if p > -dx:
            p_i -= dx
            y1 += y_unit
        if p < dy:
            p_i += dy
            x1 += x_unit

        if dash_length == 0:
            dash_length = 6

    # write(f'({int(x2 / 5)}, {int(y2 / 5)})', align='left', font=('arial', 10, 'normal'))
