from tkinter import *
import turtle
from ve3d import *
# from xetang import *
from nha import *
from bg import *
from vehinhcoban import draw_circle,draw_ellipse,draw_circleleft,draw_circleright,ve_doan_thang,draw_filled_rectangle
from toado import drawOxy
import time
# from xetang import reset
from phepdoihinh import *
from playmusic import *


###################

chantroi1 = [-155,25+15]
chantroi2 = [155,25+15]
channui11 = [-155+25, 25+15]
channui12 = [-155+55, 25+50-5]
channui13 = [-155+55+30, 24+15]

channui21 = [-155+55+5, 25+15]
channui22 = [-155+55+30, 25+40-5]
channui23 = [-155+55+65, 24+15]

channui31 = [-15-20, 25+15]
channui32 = [-25+45-20, 25+45-5]
channui33 = [-25+70-20, 25+15]

channui41 = [0-20, 25+15]
channui42 = [45-20, 25+55-5]
channui43 = [45+40-20-10, 24+15]

#may
may_ = [80, 70] #r
may1_ = [87, 66]
may2_ = [89, 74] #r
may3_ = [95, 67]
may4_ = [99, 74] #r

may21_ = [-80-40, 70] #r
may22_ = [-87-40, 66]
may23_ = [-89-40, 74] #r
may24_ = [-95-40, 67]
may25_ = [-99-40, 74] #r
may26_ = [-102-40, 66]

#mattroi
mt = [-25, 75]

r = 6
r1 = 5
r2 = 4

#cay
cay11 = [100, -50]
cay12 = [102, -20]
cay13 = [104, -53]
nhanh11 = [102, -28]
nhanh12 = [97, -22]
nhanh21 = [103, -32]
nhanh22 = [108, -24]
nhanh31 = [101, -35]
nhanh32 = [95, -28]
nhanh41 = [103, -40]
nhanh42 = [114, -31]
nhanh4111 = [107, -36]
nhanh4112 = [110, -28]
nhanh51 = [100, -45]
nhanh52 = [95, -38]
nhanh53 = [90, -40]

#cay2
cay211_ = [100-170, -50+70]
cay212_ = [102-170, -20+70]
cay213_ = [104-170, -53+70]
nhanh211_ = [102-170, -28+70]
nhanh212_ = [97-170, -22+70]
nhanh221_ = [103-170, -32+70]
nhanh222_ = [108-170, -24+70]
nhanh231_ = [101-170, -35+70]
nhanh232_ = [95-170, -28+70]
nhanh241_ = [103-170, -40+70]
nhanh242_ = [114-170, -31+70]
nhanh24111_ = [107-170, -36+70]
nhanh24112_ = [110-170, -28+70]
nhanh251_ = [100-170, -45+70]
nhanh252_ = [95-170, -38+70]
nhanh253_ = [90-170, -40+70]

def resetbg():
    global may, may1, may2, may3, may4, may21, may22, may23, may24, may25, may26
    global cay211, cay212, cay213, nhanh211, nhanh212, nhanh221, nhanh222, nhanh231, nhanh232, nhanh241, nhanh242, nhanh24111, nhanh24112, nhanh251, nhanh252, nhanh253

    
    may =may_
    may1 =may1_
    may2 =may2_
    may3 =may3_
    may4 =may4_
    may21 =may21_
    may22 =may22_
    may23 =may23_
    may24 =may24_
    may25 =may25_
    may26 =may26_

    cay211 =cay211_
    cay212 =cay212_
    cay213 =cay213_
    nhanh211 =nhanh211_
    nhanh212 =nhanh212_
    nhanh221 =nhanh221_
    nhanh222 =nhanh222_
    nhanh231 =nhanh231_
    nhanh232 =nhanh232_
    nhanh241 =nhanh241_
    nhanh242 =nhanh242_
    nhanh24111 =nhanh24111_
    nhanh24112 =nhanh24112_
    nhanh251 =nhanh251_
    nhanh252 =nhanh252_
    nhanh253 =nhanh253_




def vebg(bg):
    ve_doan_thang(bg, channui21, channui22)
    ve_doan_thang(bg, channui22, channui23)
    bg.begin_fill()
    bg.fillcolor("Gray31")
    ve_doan_thang(bg, channui21, channui22)
    ve_doan_thang(bg, channui22, channui23)
    bg.end_fill()

    ve_doan_thang(bg, channui11, channui12)
    ve_doan_thang(bg, channui12, channui13)
    bg.begin_fill()
    bg.fillcolor("Gray")
    ve_doan_thang(bg, channui11, channui12)
    ve_doan_thang(bg, channui12, channui13)
    bg.end_fill()

    ve_doan_thang(bg, channui31, channui32)
    ve_doan_thang(bg, channui32, channui33)
    bg.begin_fill()
    bg.fillcolor("Gray51")
    ve_doan_thang(bg, channui31, channui32)
    ve_doan_thang(bg, channui32, channui33)
    bg.end_fill()

    ve_doan_thang(bg, channui41, channui42)
    ve_doan_thang(bg, channui42, channui43)
    bg.begin_fill()
    bg.fillcolor("Gray71")
    ve_doan_thang(bg, channui41, channui42)
    ve_doan_thang(bg, channui42, channui43)
    bg.end_fill()

    #ve mat troi
    draw_circle(bg, mt, r2)
    draw_circle(bg, mt, r2)
    


    #ve cay1
    ve_doan_thang(bg, cay11, cay12)
    ve_doan_thang(bg, cay12, cay13)
    ve_doan_thang(bg, cay11, cay13)
    bg.begin_fill()
    bg.fillcolor("maroon")
    ve_doan_thang(bg, cay11, cay12)
    ve_doan_thang(bg, cay12, cay13)
    ve_doan_thang(bg, cay11, cay13)
    bg.end_fill()
    ve_doan_thang(bg, nhanh11, nhanh12)
    ve_doan_thang(bg, nhanh21, nhanh22)
    ve_doan_thang(bg, nhanh31, nhanh32)
    ve_doan_thang(bg, nhanh41, nhanh42)
    ve_doan_thang(bg, nhanh4111, nhanh4112)
    ve_doan_thang(bg, nhanh51, nhanh52)
    ve_doan_thang(bg, nhanh52, nhanh53)



    ve_doan_thang(bg, chantroi1, chantroi2)

def vecay2(bg):
    # ve cay 2
    ve_doan_thang(bg, cay211, cay212)
    ve_doan_thang(bg, cay212, cay213)
    ve_doan_thang(bg, cay211, cay213)
    bg.begin_fill()
    bg.fillcolor("maroon")
    ve_doan_thang(bg, cay211, cay212)
    ve_doan_thang(bg, cay212, cay213)
    ve_doan_thang(bg, cay211, cay213)
    bg.end_fill()
    ve_doan_thang(bg, nhanh211, nhanh212)
    ve_doan_thang(bg, nhanh221, nhanh222)
    ve_doan_thang(bg, nhanh231, nhanh232)
    ve_doan_thang(bg, nhanh241, nhanh242)
    ve_doan_thang(bg, nhanh24111, nhanh24112)
    ve_doan_thang(bg, nhanh251, nhanh252)
    ve_doan_thang(bg, nhanh252, nhanh253)

def thunhocay2(bg):
    global cay211, cay212, cay213, nhanh211, nhanh212, nhanh221, nhanh222, nhanh231, nhanh232, nhanh241, nhanh242, nhanh24111, nhanh24112, nhanh251, nhanh252, nhanh253

    #vecay2(bg)
    O = cay211
    sx = 0.6
    sy = 0.6
    turtle.update()
    cay211 = thuphong(cay211, O, sx, sy)
    cay212 = thuphong(cay212, O, sx, sy)
    cay213 = thuphong(cay213, O, sx, sy)
    nhanh211 = thuphong(nhanh211, O, sx, sy)
    nhanh212 = thuphong(nhanh212, O, sx, sy)
    nhanh221 = thuphong(nhanh221, O, sx, sy)
    nhanh222 = thuphong(nhanh222, O, sx, sy)
    nhanh231 = thuphong(nhanh231, O, sx, sy)
    nhanh232 = thuphong(nhanh232, O, sx, sy)
    nhanh241 = thuphong(nhanh241, O, sx, sy)
    nhanh242 = thuphong(nhanh242, O, sx, sy)
    nhanh24111 = thuphong(nhanh24111, O, sx, sy)
    nhanh24112 = thuphong(nhanh24112, O, sx, sy)
    nhanh251 = thuphong(nhanh251, O, sx, sy)
    nhanh252 = thuphong(nhanh252, O, sx, sy)
    nhanh253 = thuphong(nhanh253, O, sx, sy)

    vecay2(bg)
############################


cotco1_main=[103,38]
cotco2_main=[105,38]
cotco3_main=[105,48]
cotco4_main=[103,48]

laconha1_main=[103,48]
laconha2_main=[122,48]
laconha3_main=[122,58]
laconha4_main=[103,58]


####

def resetco():
    global cotco1,cotco2,cotco3,cotco4,laconha1,laconha2,laconha3,laconha4
    cotco1=cotco1_main
    cotco2=cotco2_main
    cotco3=cotco3_main
    cotco4=cotco4_main

    laconha1=laconha1_main
    laconha2=laconha2_main
    laconha3=laconha3_main
    laconha4=laconha4_main

# def resetall():
#     reset()

def veco(co,color="yellow"):
    ve_doan_thang(co,cotco1,cotco2)
    ve_doan_thang(co,cotco2,cotco3)
    ve_doan_thang(co,cotco3,cotco4)
    ve_doan_thang(co,cotco4,cotco1)
    co.begin_fill()
    co.fillcolor("gray")
    ve_doan_thang(co,cotco1,cotco2)
    ve_doan_thang(co,cotco2,cotco3)
    ve_doan_thang(co,cotco3,cotco4)
    ve_doan_thang(co,cotco4,cotco1)
    co.end_fill()

    co.begin_fill()
    co.fillcolor(color)
    ve_doan_thang(co,laconha1,laconha2)
    ve_doan_thang(co,laconha2,laconha3)
    ve_doan_thang(co,laconha3,laconha4)
    ve_doan_thang(co,laconha4,laconha1)
    co.end_fill()

    data = {
        "cotco1":cotco1,
        "cotco2":cotco2,
        "cotco3":cotco3,
        "cotco4":cotco4,
        "laconha1":laconha1,
        "laconha2":laconha2,
        "laconha3":laconha3,
        "laconha4":laconha4,
    }
    update_labels(labels4, data)
    frame_show_toado.update()


def xoayco(co):
    global cotco1,cotco2,cotco3,cotco4,laconha1,laconha2,laconha3,laconha4
    count=0
    while True:
        if count <=12:
            veco(co)
        elif count <=22:
            veco(co,"red")
        else:
            break
        turtle.update()
        time.sleep(0.03)
        co.clear()   
        
        cotco2=xoay(cotco2,cotco1,15)
        cotco3=xoay(cotco3,cotco1,15)
        cotco4=xoay(cotco4,cotco1,15)

        laconha1=xoay(laconha1,cotco1,15)
        laconha2=xoay(laconha2,cotco1,15)
        laconha3=xoay(laconha3,cotco1,15)
        laconha4=xoay(laconha4,cotco1,15)
        count+=1




############################################################33



def vemay(cloud):
    draw_circle(cloud, may, r)
    draw_circle(cloud, may1, r1)
    draw_circle(cloud, may2, r)
    draw_circle(cloud, may3, r1)
    draw_circle(cloud, may4, r)
    """
    cloud.begin_fill()
    cloud.fillcolor("lightblue")
    draw_circle(cloud, may, r)
    draw_circle(cloud, may1, r1)
    draw_circle(cloud, may2, r)
    draw_circle(cloud, may3, r1)
    draw_circle(cloud, may4, r)
    cloud.end_fill()
    """
    draw_circle(cloud, may21, r)
    draw_circle(cloud, may22, r1)
    draw_circle(cloud, may23, r)
    draw_circle(cloud, may24, r1)
    draw_circle(cloud, may25, r)
    draw_circle(cloud, may26, r1)

    data = {
        "may":may,
        "may1":may1,
        "may2":may2,
        "may3":may3,
        "may4":may4,
        "may21":may21,
        "may22":may22,
        "may23":may23,
        "may24":may24,
        "may25":may25,
        "may26":may26,
    }
    update_labels(labels3, data)
    # frame_show_toado.update()

def maybay(cloud,co):
    global may, may1, may2, may3, may4, may21, may22, may23, may24, may25, may26,cotco1,cotco2,cotco3,cotco4,laconha1,laconha2,laconha3,laconha4

    count = 0
    while True:
        vemay(cloud)
        veco(co,"red")
        turtle.update()
        time.sleep(0.2)
        cloud.clear()
        co.clear()
        if count % 40<20:
            may = tinhtien(may, 1, 0)
            may1 = tinhtien(may1, 1, 0)
            may2 = tinhtien(may2, 1, 0)
            may3 = tinhtien(may3, 1, 0)
            may4 = tinhtien(may4, 1, 0)

            may21 = tinhtien(may21, 1, 0)
            may22 = tinhtien(may22, 1, 0)
            may23 = tinhtien(may23, 1, 0)
            may24 = tinhtien(may24, 1, 0)
            may25 = tinhtien(may25, 1, 0)
            may26 = tinhtien(may26, 1, 0)


            cotco1=tinhtien(cotco1,-1,0)
            cotco2=tinhtien(cotco2,-1,0)
            cotco3=tinhtien(cotco3,-1,0)
            cotco4=tinhtien(cotco4,-1,0)

            laconha1=tinhtien(laconha1,-1,0)
            laconha2=tinhtien(laconha2,-1,0)
            laconha3=tinhtien(laconha3,-1,0)
            laconha4=tinhtien(laconha4,-1,0)


        else :
            may = tinhtien(may, -1, 0)
            may1 = tinhtien(may1, -1, 0)
            may2 = tinhtien(may2, -1, 0)
            may3 = tinhtien(may3, -1, 0)
            may4 = tinhtien(may4, -1, 0)

            may21 = tinhtien(may21, -1, 0)
            may22 = tinhtien(may22, -1, 0)
            may23 = tinhtien(may23, -1, 0)
            may24 = tinhtien(may24, -1, 0)
            may25 = tinhtien(may25, -1, 0)
            may26 = tinhtien(may26, -1, 0)

            cotco1=tinhtien(cotco1,1,0)
            cotco2=tinhtien(cotco2,1,0)
            cotco3=tinhtien(cotco3,1,0)
            cotco4=tinhtien(cotco4,1,0)

            laconha1=tinhtien(laconha1,1,0)
            laconha2=tinhtien(laconha2,1,0)
            laconha3=tinhtien(laconha3,1,0)
            laconha4=tinhtien(laconha4,1,0)
        count += 1

###############################################
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

    data = {
        "banhxetrai": banhxetrai,
        "banhxephai": banhxephai,
        "banhxe1": banhxe1,
        "banhxe2": banhxe2,
        "banhxe3": banhxe3,
        "banhxe4": banhxe4,
        "duongthang11": duongthang11,
        "duongthang12": duongthang12,
        "duongthang21": duongthang21,
        "duongthang22": duongthang22,
        "tambanhxe11": tamxebanh11,
        "tambanhxe12": tamxebanh12,
        "tambanhxe21": tamxebanh21,
        "tambanhxe22": tamxebanh22,
        "tambanhxe31": tamxebanh31,
        "tambanhxe32": tamxebanh32,
        "tambanhxe41": tamxebanh41,
        "tambanhxe42": tamxebanh42,
        "nongxetang1": nongxetang1,
        "nongxetang2": nongxetang2,
        "nongxetang3": nongxetang3,
        "nongxetang4": nongxetang4,
        "chunhat2B": chunhat2B,
        "chunhat2A": chunhat2A,
        "chunhat1B": chunhat1B,
        "chunhat1A": chunhat1A,
        "laco3": laco3,
        "cayco2": cayco2,
        "cayco1": cayco1,
    }
    update_labels(labels1, data)
    frame_show_toado.update()
    turtle.update()


def xetangchay(xetang):
    global cayco1,cayco2,laco3,banhxetrai,nongxetang1,nongxetang2,nongxetang3,nongxetang4,chunhat2A,chunhat2B,tambanhxengang41,tambanhxengang42,tambanhxengang11,tambanhxengang12,tambanhxengang21,tambanhxengang22,tambanhxengang31,tambanhxengang32,banhxe4,chunhat1A,chunhat1B,tamxebanh32,tamxebanh31,tamxebanh41,tamxebanh42, tamxebanh22,tamxebanh21,banhxephai, banhxe1, banhxe2, banhxe3,tamxebanh11,tamxebanh12,duongthang12,duongthang11,duongthang22,duongthang21
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

    data = {
        "banhxetrai_2": banhxetrai_2,
        "banhxephai_2": banhxephai_2,
        "banhxe1_2": banhxe1_2,
        "banhxe2_2": banhxe2_2,
        "banhxe3_2": banhxe3_2,
        "banhxe4_2": banhxe4_2,
        "duongthang11_2": duongthang11_2,
        "duongthang12_2": duongthang12_2,
        "duongthang21_2": duongthang21_2,
        "duongthang22_2": duongthang22_2,
        "tambanhxe11_2": tamxebanh11_2,
        "tambanhxe12_2": tamxebanh12_2,
        "tambanhxe21_2": tamxebanh21_2,
        "tambanhxe22_2": tamxebanh22_2,
        "tambanhxe31_2": tamxebanh31_2,
        "tambanhxe32_2": tamxebanh32_2,
        "tambanhxe41_2": tamxebanh41_2,
        "tambanhxe42_2": tamxebanh42_2,
        "nongxetang1_2": nongxetang1_2,
        "nongxetang2_2": nongxetang2_2,
        "nongxetang3_2": nongxetang3_2,
        "nongxetang4_2": nongxetang4_2,
        "chunhat2B_2": chunhat2B_2,
        "chunhat2A_2": chunhat2A_2,
        "chunhat1B_2": chunhat1B_2,
        "chunhat1A_2": chunhat1A_2,
        "laco3_2": laco3_2,
        "cayco2_2": cayco2_2,
        "cayco1_2": cayco1_2,
        "rn":rn,
        "rt":rt

    }

    update_labels(labels2, data)
    frame_show_toado.update()


#####################

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

        label_tamdan1.config(text="tamdan3: "+str(tamdan))
        frame_show_toado.update()


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

        label_tamdan2.config(text="tamdan2: "+str(tamdan))
        frame_show_toado.update()


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

        label_tamdan3.config(text="tamdan3: "+str(tamdan))
        frame_show_toado.update()

        if count==10:
            break
        count+=1



#########################################
def draw_background():
    
    bg.hideturtle()
    vebg(bg)
    thunhocay2(bg)


def draw_tank():
    
    xetang.hideturtle()
    dan.hideturtle()
    vexetang2(xetang2)
    xetangchay(xetang)
    vexetang(xetang)
    danbay2(dan)
    danbay2(dan)
    danbay2(dan)
    hanongxetang(xetang)
    vexetang(xetang)
    danbay(dan)
    danbay(dan)
    danbay(dan)
    thunhoxetang(xetang2)
    xetangchay(xetang)
    xetangchay(xetang)
    xetangchay(xetang)
    xetangchay(xetang)
    tangnongxetang(xetang)
    vexetang(xetang)
    danbay3(dan)
    danbay3(dan)
    danbay3(dan)
    vexetang(xetang)
    
def draw_home(co):
    drawHome(home)
    veco(co)
    
def create_new_canvas():
    global canvas2
    canvas2 = Canvas(page2,width=1920, height=1080)
    canvas2.pack(fill=BOTH, expand=True)
    global screen2
    screen2 = turtle.TurtleScreen(canvas2)
    screen2.tracer(0)

def clear_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()

def create_labels2(frame):
    global labels2
    labels2 = {}

    def add_label(name, row, column, text=""):
        label = Label(frame, text=text)
        label.grid(row=row, column=column)
        labels2[name] = label

    # XETANG2 Labels
    add_label("xetang2", 2, 6, "XETANG2   --->")
    add_label("cayco1_2", 2, 7)
    add_label("cayco2_2", 2, 8)
    add_label("laco3_2", 2, 9)
    add_label("chunhat1A_2", 2, 10)
    add_label("chunhat1B_2", 2, 11)
    add_label("chunhat2A_2", 3, 0)
    add_label("chunhat2B_2", 3, 1)
    add_label("nongxetang1_2", 3, 2)
    add_label("nongxetang2_2", 3, 3)
    add_label("nongxetang3_2", 3, 4)
    add_label("nongxetang4_2", 3, 5)
    add_label("tambanhxe41_2", 3, 6)
    add_label("tambanhxe42_2", 3, 7)
    add_label("tambanhxe31_2", 3, 8)
    add_label("tambanhxe32_2", 3, 9)
    add_label("tambanhxe22_2", 3, 10)
    add_label("tambanhxe21_2", 3, 11)
    add_label("tambanhxe12_2", 4, 0)
    add_label("tambanhxe11_2", 4, 1)
    add_label("duongthang11_2", 4, 2)
    add_label("duongthang12_2", 4, 3)
    add_label("duongthang21_2", 4, 4)
    add_label("duongthang22_2", 4, 5)
    add_label("banhxe1_2", 4, 6)
    add_label("banhxe2_2", 4, 7)
    add_label("banhxe3_2", 4, 8)
    add_label("banhxe4_2", 4, 9)
    add_label("banhxetrai_2", 4, 10)
    add_label("banhxephai_2", 4, 11)
    add_label("rn",5,0)
    add_label("rt",5,1)

    return labels2

def create_labels1(frame):
    global labels1
    labels1 = {}

    def add_label(name, row, column, text=""):
        label = Label(frame, text=text)
        label.grid(row=row, column=column)
        labels1[name] = label

    # XETANG1 Labels
    add_label("xetang1", 0, 0, "XETANG1   --->")
    add_label("cayco1", 0, 1)
    add_label("cayco2", 0, 2)
    add_label("laco3", 0, 3)
    add_label("chunhat1A", 0, 4)
    add_label("chunhat1B", 0, 5)
    add_label("chunhat2A", 0, 6)
    add_label("chunhat2B", 0, 7)
    add_label("nongxetang1", 0, 8)

    add_label("nongxetang2", 0, 9)
    add_label("nongxetang3", 0, 10)
    add_label("nongxetang4", 0, 11)
    add_label("tambanhxe41", 1, 0)
    add_label("tambanhxe42", 1, 1)
    add_label("tambanhxe31", 1, 2)
    add_label("tambanhxe32", 1, 3)
    add_label("tambanhxe22", 1, 4)
    add_label("tambanhxe21", 1, 5)

    add_label("tambanhxe12", 1, 6)
    add_label("tambanhxe11", 1, 7)
    add_label("duongthang11", 1, 8)
    add_label("duongthang12", 1, 9)
    add_label("duongthang21", 1, 10)
    add_label("duongthang22", 1, 11)
    add_label("banhxe1", 2, 0)
    add_label("banhxe2", 2, 1)
    add_label("banhxe3", 2, 2)

    add_label("banhxe4", 2, 3)
    add_label("banhxetrai", 2, 4)
    add_label("banhxephai", 2, 5)

    return labels1


# may
def create_labels3(frame):
    global labels3
    labels3 = {}

    def add_label(name, row, column, text=""):
        label = Label(frame, text=text)
        label.grid(row=row, column=column)
        labels3[name] = label

    # MAY Labels
    add_label("may", 5, 2, "MAY   --->")
    add_label("may", 5, 3)
    add_label("may1", 5, 4)
    add_label("may2", 5, 5)
    add_label("may3", 5, 6)
    add_label("may4", 5, 7)
    add_label("may21", 5, 8)
    add_label("may22", 5, 9)
    add_label("may23", 5, 10)
    add_label("may24", 5, 11)
    add_label("may25", 6, 0)
    add_label("may26", 6, 1)

    return labels3

def create_labels4(frame):
    global labels4
    labels4 = {}

    def add_label(name, row, column, text=""):
        label = Label(frame, text=text)
        label.grid(row=row, column=column)
        labels4[name] = label

    # LACO Labels
    add_label("cotco1", 6, 2, "LACO   --->")
    add_label("cotco1", 6, 3)
    add_label("cotco2", 6, 4)
    add_label("cotco3", 6, 5)
    add_label("cotco4", 6, 6)
    add_label("laconha1", 6, 7)
    add_label("laconha2", 6, 8)
    add_label("laconha3", 6, 9)
    add_label("laconha4", 6, 10)

    return labels4

def update_labels(labels, data):
    for key, value in data.items():
        if key in labels:
            labels[key].config(text=f"{key}: {value}")




def resetall():
    reset()
    resetco()
    resetbg()

def info2D():
    resetall()
    play_music("music.mp3")
    page2.tkraise()
    frame_show.tkraise()
    clear_frame(frame_info)
    canvas2.destroy()
    create_new_canvas()
   

    t.clear()
    toado3d.clear()
    global frame_show_toado
    frame_show_toado = Frame(frame_info)
    frame_show_toado.pack()

    create_labels1(frame_show_toado)
    create_labels2(frame_show_toado)
    create_labels3(frame_show_toado)
    create_labels4(frame_show_toado)

    label_dan = Label(frame_show_toado,text= "DAN   --->")
    label_dan.grid(row=6,column=11)

    global label_tamdan1
    label_tamdan1 = Label(frame_show_toado)
    label_tamdan1.grid(row=7,column=0)

    global label_tamdan2
    label_tamdan2 = Label(frame_show_toado)
    label_tamdan2.grid(row=7,column=1)

    global label_tamdan3
    label_tamdan3 = Label(frame_show_toado)
    label_tamdan3.grid(row=7,column=2)

    label_bg = Label(frame_show_toado,text="BACKGROUND  --->")
    label_bg.grid(row=7,column=3)

    label_r1 = Label(frame_show_toado,text="r1: 3")
    label_r1.grid(row=7,column=4)

    label_r2 = Label(frame_show_toado,text="R1: 5")
    label_r2.grid(row=7,column=5)

    label_rmay1 = Label(frame_show_toado,text="R_may_1: 5")
    label_rmay1.grid(row=7,column=6)

    label_rmay2 = Label(frame_show_toado,text="R_may_2: 6")
    label_rmay2.grid(row=7,column=7)

    label_chantroi = Label(frame_show_toado,text="chantroi: "+str(chantroi1)+"," +str(chantroi2))
    label_chantroi.grid(row=7,column=8)

    label_mattroi = Label(frame_show_toado,text="mattroi: " + str(mt))
    label_mattroi.grid(row=7,column=9)

    label_rmt = Label(frame_show_toado,text="rmt: 4")
    label_rmt.grid(row=7,column=10)

    label_channui11 = Label(frame_show_toado,text= "channui11: " +str(channui11))
    label_channui11.grid(row=7,column=11)

    label_channui12 = Label(frame_show_toado,text= "channui12: " +str(channui12))
    label_channui12.grid(row=8,column=0)

    label_channui13 = Label(frame_show_toado,text= "channui13: " +str(channui13))
    label_channui13.grid(row=8,column=1)

    label_channui21 = Label(frame_show_toado,text= "channui21: " +str(channui21))
    label_channui21.grid(row=8,column=2)

    label_channui22 = Label(frame_show_toado,text= "channui22: " +str(channui22))
    label_channui22.grid(row=8,column=3)

    label_channui23 = Label(frame_show_toado,text= "channui23: " +str(channui23))
    label_channui23.grid(row=8,column=4)

    label_channui31 = Label(frame_show_toado,text= "channui31: " +str(channui31))
    label_channui31.grid(row=8,column=5)

    label_channui32 = Label(frame_show_toado,text= "channui32: " +str(channui32))
    label_channui32.grid(row=8,column=6)

    label_channui33 = Label(frame_show_toado,text= "channui33: " +str(channui33))
    label_channui33.grid(row=8,column=7)

    label_channui41 = Label(frame_show_toado,text= "channui41: " +str(channui41))
    label_channui41.grid(row=8,column=8)

    label_channui42 = Label(frame_show_toado,text= "channui42: " +str(channui42))
    label_channui42.grid(row=8,column=9)

    label_channui43 = Label(frame_show_toado,text= "channui43: " +str(channui43))
    label_channui43.grid(row=8,column=10)


    t2 = turtle.RawTurtle(screen2)
    t2.hideturtle()
    global bg
    bg = turtle.RawTurtle(screen2)
    global xetang
    xetang=turtle.RawTurtle(screen2)
    global xetang2
    xetang2=turtle.RawTurtle(screen2)
    global dan
    dan=turtle.RawTurtle(screen2)
    global home
    home=turtle.RawTurtle(screen2)
    global co
    co=turtle.RawTurtle(screen2)
    co.hideturtle()
    global cloud
    cloud = turtle.RawTurtle(screen2)
    cloud.hideturtle()
    vemay(cloud)
    draw_background()
    drawOxy(t2)
    draw_home(co)
    draw_tank()
    xoayco(co)
    veco(co,"red")
    maybay(cloud,co)
    


def input3D():
    stop_music()
    canvas2.destroy()
    page1.tkraise()
    frame_show.tkraise()
    t.clear()
    clear_frame(frame_info)
    frame_toado = Frame(frame_info)
    frame_toado.pack(padx=5,pady=5)
    label_toado_x = Label(frame_toado,text='X')
    label_toado_x.grid(row=0,column=0)
    global entry_toado_x
    global entry_toado_y
    global entry_toado_z
    global entry_h
    global entry_r
    entry_toado_x = Entry(frame_toado)
    entry_toado_x.grid(row=0,column=1)
    label_toado_y = Label(frame_toado,text='Y')
    label_toado_y.grid(row=0,column=2)
    entry_toado_y = Entry(frame_toado)
    entry_toado_y.grid(row=0,column=3)
    label_toado_z = Label(frame_toado,text='Z')
    label_toado_z.grid(row=0,column=4)
    entry_toado_z = Entry(frame_toado)
    entry_toado_z.grid(row=0,column=5)
    
    frame_h = Frame(frame_info)
    frame_h.pack()
    label_h = Label(frame_h, text='Chiều cao')
    label_h.grid(row=0,column=0)
    entry_h = Entry(frame_h)
    entry_h.grid(row=0,column=1)
    
    frame_r = Frame(frame_info)
    frame_r.pack()
    label_r = Label(frame_r,text='Bán kính')
    label_r.grid(row=0,column=0)
    entry_r = Entry(frame_r)
    entry_r.grid(row=0,column=1)   

def hinh_tru():
    toado3d.clear()
    drawOxy3d(toado3d)
    input3D()
    btn_ve = Button(frame_info,text='Vẽ hình trụ',command=draw_hinh_tru)
    btn_ve.pack()

def draw_hinh_tru():
    t.clear()
    tamday = [int(entry_toado_x.get()),int(entry_toado_y.get()),int(entry_toado_z.get())]
    r = int(entry_r.get())
    h = int(entry_h.get())
    vehinhtru(t,tamday,r,h)

def hinh_non():
    toado3d.clear()
    drawOxy3d(toado3d)
    input3D()
    btn_ve = Button(frame_info,text='Vẽ hình nón',command=draw_hinh_non)
    btn_ve.pack()

def draw_hinh_non():
    t.clear()
    tamday = [int(entry_toado_x.get()),int(entry_toado_y.get()),int(entry_toado_z.get())]
    r = int(entry_r.get())
    h = int(entry_h.get())
    vehinhnon(t,tamday,r,h)


if __name__=="__main__":
    root = Tk()
    root.state('zoomed')

    page1 = Frame(root)
    page1.grid(column=0,row=0)

    page2 = Frame(root)
    page2.grid(column=0,row=0)

    global canvas
    canvas = Canvas(page1,width=1920, height=1080)
    canvas.pack(fill=BOTH, expand=True)

    # Tạo một turtle screen để vẽ
    global screen
    screen = turtle.TurtleScreen(canvas)
    screen.tracer(0)
    

    global t
    t = turtle.RawTurtle(screen)
    t.hideturtle()

    global toado3d
    toado3d = turtle.RawTurtle(screen)
    toado3d.hideturtle()

   
    canvas2 = Canvas(page2,width=1920, height=1080)

    frame_show = Frame(root)
    frame_show.place(relx=0, rely=0.81)
    frame_show.lift()
    # Frame chứa button
    frame_btn = Frame(frame_show)
    frame_btn.grid(row=0, column=0)

    btn_2D = Button(frame_btn, text='2D',command=info2D)
    btn_3D_1 = Button(frame_btn, text='3D Hình trụ', command=hinh_tru)
    btn_3D_2 = Button(frame_btn, text='3D Hình nón', command=hinh_non)

    btn_2D.grid(row=0, column=0)
    btn_3D_1.grid(row=0, column=1)
    btn_3D_2.grid(row=0, column=2)

    # Frame chứa thông tin 2D hoặc input 3D
    frame_info = Frame(frame_show)
    frame_info.grid(row=0, column=1)

    root.title('Đồ án cuối kỳ')

    root.mainloop()
