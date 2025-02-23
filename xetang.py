import turtle
from vehinhcoban import draw_circle,draw_ellipse,draw_circleleft,draw_circleright,ve_doan_thang,draw_filled_rectangle
from toado import drawOxy
import time
from phepdoihinh import *


#bộ điểm tượng trưng cho xe tăng tâm các hình tròn

#bộ điểm tượng trưng cho xe tăng tâm các hình tròn
banhxetrai_main=[-80-10-53,-20]
banhxephai_main=[-80-10-17,-20]
banhxe1_main=[-80-10-50,-20]
tamxebanh11_main=[-80-10-50,-17]
tamxebanh12_main=[-80-10-50,-23]
tambanhxengang11_main=[-80-10-50-3,-20]
tambanhxengang12_main=[-80-10-50+3,-20] 


banhxe2_main=[-80-10-40,-20]
tamxebanh21_main=[-80-10-40,-17]
tamxebanh22_main=[-80-10-40,-23]
tambanhxengang21_main=[-80-10-40-3,-20]
tambanhxengang22_main=[-80-10-40+3,-20]


banhxe3_main=[-80-10-30,-20]
tamxebanh31_main= [-80-10-30,-17]
tamxebanh32_main=[-80-10-30,-23]
tambanhxengang31_main=[-80-10-30-3,-20]
tambanhxengang32_main=[-80-10-30+3,-20]


banhxe4_main=[-80-10-20,-20]
tamxebanh41_main= [-80-10-20,-17]
tamxebanh42_main=[-80-10-20,-23]
tambanhxengang41_main=[-80-10-20-3,-20]
tambanhxengang42_main=[-80-10-20+3,-20]

    #đây là đường thằng trên dưới bánh xe tăng
duongthang11_main=[-80-10-53,-20+5]
duongthang12_main=[-80-10-17,-20+5]
duongthang21_main=[-80-10-53,-20-5]
duongthang22_main=[-80-10-17,-20-5]

    #đây là hình chữ nhật trên xe tăng
chunhat1A_main=[-80-10-53,-20+5]
chunhat1B_main=[-80-10-17,-5-5]

chunhat2A_main=[-80-10-50,-5-5]
chunhat2B_main=[-80-10-25,-5+5]

nongxetang1_main=[-80-10-25,-7]
nongxetang2_main=[-80-10-25,-2]
nongxetang3_main=[-80-10+5,3]
nongxetang4_main=[-80-10+5,-2]
# lá cờ 
cayco1_main=[-80-10-50+5,0]
cayco2_main=[-80-10-50+5,10]
laco3_main=[-80-10-60+5,15]

# tâm đạn
tamdan1_main=[-80-10+5+20+6,3]
tamdan2_main=[-10,2]
tamdan3_main=[23,5]
r=5
r2=3




#diem xe tang thu 2
def diemxetang2():
    global rt,rn,duongthang21_2,cayco1_2,cayco2_2,laco3_2,banhxetrai_2,nongxetang1_2,nongxetang2_2,nongxetang3_2,nongxetang4_2,chunhat2A_2,chunhat2B_2,tambanhxengang41_2,tambanhxengang42_2,tambanhxengang11_2,tambanhxengang12_2,tambanhxengang21_2,tambanhxengang22_2,tambanhxengang31_2,tambanhxengang32_2,banhxe4_2,chunhat1A_2,chunhat1B_2,tamxebanh32_2,tamxebanh31_2,tamxebanh41_2,tamxebanh42_2, tamxebanh22_2,tamxebanh21_2,banhxephai_2, banhxe1_2, banhxe2_2, banhxe3_2,tamxebanh11_2,tamxebanh12_2,duongthang12_2,duongthang11_2,duongthang22_2,duongthang21

    O=[-45,0]
    banhxetrai_2 = doixungOy(banhxetrai, O)
    banhxephai_2 = doixungOy(banhxephai, O)
    banhxe1_2 = doixungOy(banhxe1, O)
    tamxebanh11_2 = doixungOy(tamxebanh11, O)
    tamxebanh12_2 = doixungOy(tamxebanh12, O)
    tambanhxengang11_2 = doixungOy(tambanhxengang11, O)
    tambanhxengang12_2 = doixungOy(tambanhxengang12, O)

    banhxe2_2 = doixungOy(banhxe2, O)
    tamxebanh21_2 = doixungOy(tamxebanh21, O)
    tamxebanh22_2 = doixungOy(tamxebanh22, O)
    tambanhxengang21_2 = doixungOy(tambanhxengang21, O)
    tambanhxengang22_2 = doixungOy(tambanhxengang22, O)

    banhxe3_2 = doixungOy(banhxe3, O)
    tamxebanh31_2 = doixungOy(tamxebanh31, O)
    tamxebanh32_2 = doixungOy(tamxebanh32, O)
    tambanhxengang31_2 = doixungOy(tambanhxengang31, O)
    tambanhxengang32_2 = doixungOy(tambanhxengang32, O)

    banhxe4_2 = doixungOy(banhxe4, O)
    tamxebanh41_2 = doixungOy(tamxebanh41, O)
    tamxebanh42_2 = doixungOy(tamxebanh42, O)
    tambanhxengang41_2 = doixungOy(tambanhxengang41, O)
    tambanhxengang42_2 = doixungOy(tambanhxengang42, O)

    duongthang11_2 = doixungOy(duongthang11, O)
    duongthang12_2 = doixungOy(duongthang12, O)
    duongthang21_2 = doixungOy(duongthang21, O)
    duongthang22_2 = doixungOy(duongthang22, O)

    chunhat1A_2 = doixungOy(chunhat1A, O)
    chunhat1B_2 = doixungOy(chunhat1B, O)
    chunhat2A_2 = doixungOy(chunhat2A, O)
    chunhat2B_2 = doixungOy(chunhat2B, O)

    nongxetang1_2 = doixungOy(nongxetang1, O)
    nongxetang2_2 = doixungOy(nongxetang2, O)
    nongxetang3_2 = doixungOy(nongxetang3, O)
    nongxetang4_2 = doixungOy(nongxetang4, O)

    cayco1_2 = doixungOy(cayco1, O)
    cayco2_2 = doixungOy(cayco2, O)
    laco3_2 = doixungOy(laco3, O)
    rn=5
    rt=3




############
def reset():
    global tamdan1,tamdan2,tamdan3,duongthang21,cayco1,cayco2,laco3,banhxetrai,nongxetang1,nongxetang2,nongxetang3,nongxetang4,chunhat2A,chunhat2B,tambanhxengang41,tambanhxengang42,tambanhxengang11,tambanhxengang12,tambanhxengang21,tambanhxengang22,tambanhxengang31,tambanhxengang32,banhxe4,chunhat1A,chunhat1B,tamxebanh32,tamxebanh31,tamxebanh41,tamxebanh42, tamxebanh22,tamxebanh21,banhxephai, banhxe1, banhxe2, banhxe3,tamxebanh11,tamxebanh12,duongthang12,duongthang11,duongthang22,duongthang21

    banhxetrai= banhxetrai_main
    banhxephai= banhxephai_main
    banhxe1=banhxe1_main
    tamxebanh11= tamxebanh11_main
    tamxebanh12= tamxebanh12_main
    tambanhxengang11= tambanhxengang11_main
    tambanhxengang12= tambanhxengang12_main
    banhxe2=  banhxe2_main
    tamxebanh21= tamxebanh21_main
    tamxebanh22= tamxebanh22_main
    tambanhxengang21= tambanhxengang21_main
    tambanhxengang22= tambanhxengang22_main
    banhxe3=banhxe3_main
    tamxebanh31=tamxebanh31_main
    tamxebanh32=tamxebanh32_main
    tambanhxengang31=tambanhxengang31_main
    tambanhxengang32=tambanhxengang32_main
    banhxe4=banhxe4_main
    tamxebanh41=tamxebanh41_main
    tamxebanh42=tamxebanh42_main
    tambanhxengang41=tambanhxengang41_main
    tambanhxengang42=tambanhxengang42_main
    duongthang11=duongthang11_main
    duongthang12=duongthang12_main
    duongthang21=duongthang21_main
    duongthang22=duongthang22_main
    chunhat1A=chunhat1A_main
    chunhat1B=chunhat1B_main
    chunhat2A=chunhat2A_main
    chunhat2B=chunhat2B_main
    nongxetang1=nongxetang1_main
    nongxetang2=nongxetang2_main
    nongxetang3=nongxetang3_main
    nongxetang4=nongxetang4_main
    cayco1=cayco1_main
    cayco2=cayco2_main
    laco3=laco3_main
    tamdan1=tamdan1_main
    tamdan2=tamdan2_main
    tamdan3=tamdan3_main
    diemxetang2()


def vexetang(xetang):
    draw_circleleft(xetang,banhxetrai,r)
    draw_circleright(xetang,banhxephai,r)
    draw_circle(xetang,banhxe1,r2)
    draw_circle(xetang,banhxe2,r2)
    draw_circle(xetang,banhxe3,r2)
    draw_circle(xetang,banhxe4,r2)
    ve_doan_thang(xetang,duongthang11,duongthang12)
    ve_doan_thang(xetang,duongthang21,duongthang22)
    ve_doan_thang(xetang,tamxebanh11,tamxebanh12)
    ve_doan_thang(xetang,tamxebanh21,tamxebanh22)
    ve_doan_thang(xetang,tamxebanh31,tamxebanh32)
    ve_doan_thang(xetang,tamxebanh41,tamxebanh42)
    draw_filled_rectangle(xetang,chunhat1A,chunhat1B)
    draw_filled_rectangle(xetang,chunhat2A,chunhat2B)
    ve_doan_thang(xetang,nongxetang2,nongxetang3)
    ve_doan_thang(xetang,nongxetang3,nongxetang4)
    ve_doan_thang(xetang,nongxetang4,nongxetang1)
    ve_doan_thang(xetang,cayco1,cayco2)
    draw_filled_rectangle(xetang,cayco2,laco3,"red")
    

    #vẽ phần trên



    turtle.update()


def xetangchay(xetang):
    global duongthang21,cayco1,cayco2,laco3,banhxetrai,nongxetang1,nongxetang2,nongxetang3,nongxetang4,chunhat2A,chunhat2B,tambanhxengang41,tambanhxengang42,tambanhxengang11,tambanhxengang12,tambanhxengang21,tambanhxengang22,tambanhxengang31,tambanhxengang32,banhxe4,chunhat1A,chunhat1B,tamxebanh32,tamxebanh31,tamxebanh41,tamxebanh42, tamxebanh22,tamxebanh21,banhxephai, banhxe1, banhxe2, banhxe3,tamxebanh11,tamxebanh12,duongthang12,duongthang11,duongthang22,duongthang21
    count=0
    while True:
        vexetang(xetang)
        turtle.update()
        time.sleep(0.1)
        xetang.clear()
        banhxetrai=tinhtien(banhxetrai,1,0)
        banhxephai=tinhtien(banhxephai,1,0)
        banhxe1 =tinhtien(banhxe1,1,0)
        banhxe2=tinhtien(banhxe2,1,0)
        banhxe3=tinhtien(banhxe3,1,0)
        banhxe4=tinhtien(banhxe4,1,0)
        duongthang11=tinhtien(duongthang11,1,0)
        duongthang12=tinhtien(duongthang12,1,0)
        duongthang21=tinhtien(duongthang21,1,0)
        duongthang22=tinhtien(duongthang22,1,0)
        
        tamxebanh11=tinhtien(tamxebanh11,1,0)
        tamxebanh12=tinhtien(tamxebanh12,1,0)
        tamxebanh11=xoay(tamxebanh11,banhxe1,-45)
        tamxebanh12=xoay(tamxebanh12,banhxe1,-45)

        tamxebanh21=tinhtien(tamxebanh21,1,0)
        tamxebanh22=tinhtien(tamxebanh22,1,0)
        tamxebanh21=xoay(tamxebanh21,banhxe2,-45)
        tamxebanh22=xoay(tamxebanh22,banhxe2,-45)

        tamxebanh31=tinhtien(tamxebanh31,1,0)
        tamxebanh32=tinhtien(tamxebanh32,1,0)
        tamxebanh31=xoay(tamxebanh31,banhxe3,-45)
        tamxebanh32=xoay(tamxebanh32,banhxe3,-45)

        tamxebanh41=tinhtien(tamxebanh41,1,0)
        tamxebanh42=tinhtien(tamxebanh42,1,0)
        tamxebanh41=xoay(tamxebanh41,banhxe4,-45)
        tamxebanh42=xoay(tamxebanh42,banhxe4,-45)
         
#Phần trên xe tăng
        chunhat1B=tinhtien(chunhat1B,1,0)
        chunhat1A=tinhtien(chunhat1A,1,0)
        chunhat2A=tinhtien(chunhat2A,1,0)
        chunhat2B=tinhtien(chunhat2B,1,0)
        nongxetang1=tinhtien(nongxetang1,1,0)
        nongxetang2=tinhtien(nongxetang2,1,0)
        nongxetang3=tinhtien(nongxetang3,1,0)
        nongxetang4=tinhtien(nongxetang4,1,0)


#lá cờ
        cayco2=tinhtien(cayco2,1,0)
        cayco1=tinhtien(cayco1,1,0)
        laco3=tinhtien(laco3,1,0)

        #get_xetang_value(duongthang21,cayco1,cayco2,laco3,banhxetrai,nongxetang1,nongxetang2,nongxetang3,nongxetang4,chunhat2A,chunhat2B,tambanhxengang41,tambanhxengang42,tambanhxengang11,tambanhxengang12,tambanhxengang21,tambanhxengang22,tambanhxengang31,tambanhxengang32,banhxe4,chunhat1A,chunhat1B,tamxebanh32,tamxebanh31,tamxebanh41,tamxebanh42, tamxebanh22,tamxebanh21,banhxephai, banhxe1, banhxe2, banhxe3,tamxebanh11,tamxebanh12,duongthang12,duongthang11,duongthang22,duongthang21)


        if count==20:
            break
        count+=1
    




def thunhoxetang(xetang):
    global rt,rn,duongthang21_2,cayco1_2,cayco2_2,laco3_2,banhxetrai_2,nongxetang1_2,nongxetang2_2,nongxetang3_2,nongxetang4_2,chunhat2A_2,chunhat2B_2,tambanhxengang41_2,tambanhxengang42_2,tambanhxengang11_2,tambanhxengang12_2,tambanhxengang21_2,tambanhxengang22_2,tambanhxengang31_2,tambanhxengang32_2,banhxe4_2,chunhat1A_2,chunhat1B_2,tamxebanh32_2,tamxebanh31_2,tamxebanh41_2,tamxebanh42_2, tamxebanh22_2,tamxebanh21_2,banhxephai_2, banhxe1_2, banhxe2_2, banhxe3_2,tamxebanh11_2,tamxebanh12_2,duongthang12_2,duongthang11_2,duongthang22_2,duongthang21
            
            
    count=0
    while True:
        vexetang2(xetang)
        O=banhxe1_2
        sx=0.8
        sy=0.8
        turtle.update()
        time.sleep(0.7)
        xetang.clear()
        banhxetrai_2 = thuphong(banhxetrai_2, O, sx, sy)
        banhxephai_2 = thuphong(banhxephai_2, O, sx, sy)
        banhxe1_2 = thuphong(banhxe1_2, O, sx, sy)
        tamxebanh11_2 = thuphong(tamxebanh11_2, O, sx, sy)
        tamxebanh12_2 = thuphong(tamxebanh12_2, O, sx, sy)
        tambanhxengang11_2 = thuphong(tambanhxengang11_2, O, sx, sy)
        tambanhxengang12_2 = thuphong(tambanhxengang12_2, O, sx, sy)
        banhxe2_2 = thuphong(banhxe2_2, O, sx, sy)
        tamxebanh21_2 = thuphong(tamxebanh21_2, O, sx, sy)
        tamxebanh22_2 = thuphong(tamxebanh22_2, O, sx, sy)
        tambanhxengang21_2 = thuphong(tambanhxengang21_2, O, sx, sy)
        tambanhxengang22_2 = thuphong(tambanhxengang22_2, O, sx, sy)
        banhxe3_2 = thuphong(banhxe3_2, O, sx, sy)



        tamxebanh31_2 = thuphong(tamxebanh31_2, O, sx, sy)
        tamxebanh32_2 = thuphong(tamxebanh32_2, O, sx, sy)
        tambanhxengang31_2 = thuphong(tambanhxengang31_2, O, sx, sy)
        tambanhxengang32_2 = thuphong(tambanhxengang32_2, O, sx, sy)
        banhxe4_2 = thuphong(banhxe4_2, O, sx, sy)
        tamxebanh41_2 = thuphong(tamxebanh41_2, O, sx, sy)
        tamxebanh42_2 = thuphong(tamxebanh42_2, O, sx, sy)
        tambanhxengang41_2 = thuphong(tambanhxengang41_2, O, sx, sy)
        tambanhxengang42_2 = thuphong(tambanhxengang42_2, O, sx, sy)
        duongthang11_2 = thuphong(duongthang11_2, O, sx, sy)
        duongthang12_2 = thuphong(duongthang12_2, O, sx, sy)

        
        duongthang21_2 = thuphong(duongthang21_2, O, sx, sy)
        duongthang22_2 = thuphong(duongthang22_2, O, sx, sy)
        chunhat1A_2 = thuphong(chunhat1A_2, O, sx, sy)
        chunhat1B_2 = thuphong(chunhat1B_2, O, sx, sy)
        chunhat2A_2 = thuphong(chunhat2A_2, O, sx, sy)
        chunhat2B_2 = thuphong(chunhat2B_2, O, sx, sy)
        nongxetang1_2 = thuphong(nongxetang1_2, O, sx, sy)
        nongxetang2_2 = thuphong(nongxetang2_2, O, sx, sy)
        nongxetang3_2 = thuphong(nongxetang3_2, O, sx, sy)
        nongxetang4_2 = thuphong(nongxetang4_2, O, sx, sy)
        
        cayco1_2 = thuphong(cayco1_2, O, sx, sy)
        cayco2_2 = thuphong(cayco2_2, O, sx, sy)
        laco3_2 = thuphong(laco3_2, O, sx, sy)
        rt=rt*sx
        rn=rn*sx

        if count==5:
            break
        count+=1




def vexetang2(xetang):
    draw_circleright(xetang,banhxetrai_2,rn)
    draw_circleleft(xetang,banhxephai_2,rn)
    draw_circle(xetang,banhxe1_2,rt)
    draw_circle(xetang,banhxe2_2,rt)
    draw_circle(xetang,banhxe3_2,rt)
    draw_circle(xetang,banhxe4_2,rt)
    ve_doan_thang(xetang,duongthang11_2,duongthang12_2)
    ve_doan_thang(xetang,duongthang21_2,duongthang22_2)
    ve_doan_thang(xetang,tamxebanh11_2,tamxebanh12_2)
    ve_doan_thang(xetang,tamxebanh21_2,tamxebanh22_2)
    ve_doan_thang(xetang,tamxebanh31_2,tamxebanh32_2)
    ve_doan_thang(xetang,tamxebanh41_2,tamxebanh42_2)
    draw_filled_rectangle(xetang,chunhat1A_2,chunhat1B_2)
    draw_filled_rectangle(xetang,chunhat2A_2,chunhat2B_2)
    ve_doan_thang(xetang,nongxetang2_2,nongxetang3_2)
    ve_doan_thang(xetang,nongxetang3_2,nongxetang4_2)
    ve_doan_thang(xetang,nongxetang4_2,nongxetang1_2)
    ve_doan_thang(xetang,cayco1_2,cayco2_2)

    draw_filled_rectangle(xetang,cayco2_2,laco3_2,"yellow")


#####################
# nongxetang4=[-80-10+5,-2]s

tamdan1=[-80-10+5+20+6,3]
tamdan2=[-10,2]

def danbay(dan):
    tamdan=tamdan1
    count=0
    while True:
        draw_circle(dan,tamdan,3)
        turtle.update()
        time.sleep(0.1)
        dan.clear()
        tamdan=xoay(tamdan,[-6,-70],-5)
        if count==14:
            break
        count+=1
        
# def danbay2(dan):
def danbay2(dan):
    tamdan=tamdan2
    count=0
    while True:
        draw_circle(dan,tamdan,3)
        turtle.update()
        time.sleep(0.2)
        dan.clear()
        tamdan=xoay(tamdan,[-100,-110],5)
        if count==22:
            break
        count+=1

def hanongxetang(xetang):
     global nongxetang3,nongxetang4
     count=0

     while True:
        vexetang(xetang)
        turtle.update()
        time.sleep(0.4)
        xetang.clear()
        if count <5: 
            nongxetang3=tinhtien(nongxetang3,0,1)
            nongxetang4=tinhtien(nongxetang4,0,1)
        elif count <11:
            nongxetang3=tinhtien(nongxetang3,0,-1)
            nongxetang4=tinhtien(nongxetang4,0,-1) 
        else: 
            break
        count+=1

def tangnongxetang(xetang):
    global nongxetang3,nongxetang4
    count =0
    while True:
        vexetang(xetang)
        turtle.update()
        time.sleep(0.4)
        xetang.clear()
        if count<5:
            nongxetang3=tinhtien(nongxetang3,0,1)
            nongxetang4=tinhtien(nongxetang4,0,1)
            count +=1
        else:
            break

tamdan3=[23,5]
def danbay3(dan):
    tamdan=tamdan3
    count=0
    while True:
        draw_circle(dan,tamdan,3)
        turtle.update()
        time.sleep(0.2)
        dan.clear()
        tamdan=tinhtien(tamdan,4,2)
        if count==10:
            break
        count+=1

# if __name__=="__main__":
#     drawOxy()
#     xetang=turtle.Turtle()
#     xetang2=turtle.Turtle()
#     dan=turtle.Turtle()
#     xetang.hideturtle()
#     dan.hideturtle()
    
#     vexetang2(xetang2)
#     xetangchay(xetang)
#     vexetang(xetang)
#     # danbay2(dan)
#     # danbay2(dan)
#     # danbay2(dan)
#     # hanongxetang(xetang)
#     vexetang(xetang)
#     danbay(dan)
#     danbay(dan)
#     danbay(dan)
#     thunhoxetang(xetang2)
#     xetangchay(xetang)
#     vexetang(xetang)
#     turtle.exitonclick()


