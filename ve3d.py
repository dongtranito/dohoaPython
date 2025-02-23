import math
from toado import *
from vehinhcoban import *
import turtle

def cabinet(A):
    xA=A[0]
    yA=A[1]
    zA=A[2]
    x=round(xA-yA*math.sqrt(2)/4)
    y=round(zA-yA*math.sqrt(2)/4) 
    return ([x,y])

# tamday=[-20,-10,-30]
# r=25
# h=50


def vehinhtru(t,tamday,r,h):
    t.hideturtle()
    t.speed(0)
    t.penup()
    t.color("black")

    # Biến đổi ban kinh  elip
    tamday1=cabinet(tamday)
    # print (tamday1)
    R=[0,r,0]
    r1=r #bán kính 1

    r2=-cabinet(R)[1] #bán kính 2
    r2=r2/math.sqrt(2)

    # # biến đổi tâm 2
    tamday2=tamday1.copy()
    tamday2[1]=tamday1[1]+h

    #
    a1=tamday1.copy()
    a1[0]=a1[0]-r1
    a2=tamday2.copy()
    a2[0]=a2[0]-r1

    b1=tamday1.copy()
    b1[0]=b1[0]+r1
    b2=tamday2.copy()
    b2[0]=b2[0]+r1
    
    #ve hinh tru
    draw_ellipse(t,tamday1,r1,r2)
    draw_ellipse(t,tamday2,r1,r2,1)
    dash_line(t,tamday1,tamday2)
    ve_doan_thang(t,a1,a2)
    ve_doan_thang(t,b1,b2)
    



def vehinhnon(t,tamday,r,h):
    t.hideturtle()
    t.speed(0)
    t.penup()
    t.color("black")
    # Biến đổi ban kinh  elip
    tamday1=cabinet(tamday)
    # print (tamday1)
    R=[0,r,0]
    r1=r #bán kính 1
    r2=-cabinet(R)[1] #bán kính 2
    r2=r2/math.sqrt(2)


    # # biến đổi tâm 2
    tamday2=tamday1.copy()
    tamday2[1]=tamday1[1]+h
    #
    a1=tamday1.copy()
    a1[0]=a1[0]-r1
    a2=tamday2.copy()
    a2[0]=a2[0]-r1

    b1=tamday1.copy()
    b1[0]=b1[0]+r1
    b2=tamday2.copy()
    b2[0]=b2[0]+r1
    
    #ve hinh non
    draw_ellipse(t,tamday1,r1,r2)
    dash_line(t,tamday1,tamday2)
    ve_doan_thang(t,tamday2,a1)
    ve_doan_thang(t,tamday2,b1)
    

# if __name__=="__main__":
#     t=turtle.Turtle()
#     vehinhtru(t,tamday,r,h)
#     drawOxy3d()
#     turtle.exitonclick()


