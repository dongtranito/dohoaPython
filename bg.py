import turtle
from vehinhcoban import ve_doan_thang, draw_circle
from toado import drawOxy
import time
from phepdoihinh import *

# screen = turtle.Screen()
# screen.setup(width=1.0, height=1.0)

#bo diem tuong trung cho duong chan troi


# def vemay(cloud):
#     draw_circle(cloud, may, r)
#     draw_circle(cloud, may1, r1)
#     draw_circle(cloud, may2, r)
#     draw_circle(cloud, may3, r1)
#     draw_circle(cloud, may4, r)
#     """
#     cloud.begin_fill()
#     cloud.fillcolor("lightblue")
#     draw_circle(cloud, may, r)
#     draw_circle(cloud, may1, r1)
#     draw_circle(cloud, may2, r)
#     draw_circle(cloud, may3, r1)
#     draw_circle(cloud, may4, r)
#     cloud.end_fill()
#     """
#     draw_circle(cloud, may21, r)
#     draw_circle(cloud, may22, r1)
#     draw_circle(cloud, may23, r)
#     draw_circle(cloud, may24, r1)
#     draw_circle(cloud, may25, r)
#     draw_circle(cloud, may26, r1)

import nha

# def maybay(cloud,co):
#     global may, may1, may2, may3, may4, may21, may22, may23, may24, may25, may26

#     count = 0
#     while True:
#         vemay(cloud)
#         nha.veco(co,"red")
#         turtle.update()
#         time.sleep(0.2)
#         cloud.clear()
#         co.clear()
#         if count % 40<20:
#             may = tinhtien(may, 1, 0)
#             may1 = tinhtien(may1, 1, 0)
#             may2 = tinhtien(may2, 1, 0)
#             may3 = tinhtien(may3, 1, 0)
#             may4 = tinhtien(may4, 1, 0)

#             may21 = tinhtien(may21, 1, 0)
#             may22 = tinhtien(may22, 1, 0)
#             may23 = tinhtien(may23, 1, 0)
#             may24 = tinhtien(may24, 1, 0)
#             may25 = tinhtien(may25, 1, 0)
#             may26 = tinhtien(may26, 1, 0)

#             nha.cotco1=tinhtien(nha.cotco1,-1,0)
#             nha.cotco2=tinhtien(nha.cotco2,-1,0)
#             nha.cotco3=tinhtien(nha.cotco3,-1,0)
#             nha.cotco4=tinhtien(nha.cotco4,-1,0)

#             nha.laco1=tinhtien(nha.laco1,-1,0)
#             nha.laco2=tinhtien(nha.laco2,-1,0)
#             nha.laco3=tinhtien(nha.laco3,-1,0)
#             nha.laco4=tinhtien(nha.laco4,-1,0)


#         else :
#             may = tinhtien(may, -1, 0)
#             may1 = tinhtien(may1, -1, 0)
#             may2 = tinhtien(may2, -1, 0)
#             may3 = tinhtien(may3, -1, 0)
#             may4 = tinhtien(may4, -1, 0)

#             may21 = tinhtien(may21, -1, 0)
#             may22 = tinhtien(may22, -1, 0)
#             may23 = tinhtien(may23, -1, 0)
#             may24 = tinhtien(may24, -1, 0)
#             may25 = tinhtien(may25, -1, 0)
#             may26 = tinhtien(may26, -1, 0)

#             nha.cotco1=tinhtien(nha.cotco1,1,0)
#             nha.cotco2=tinhtien(nha.cotco2,1,0)
#             nha.cotco3=tinhtien(nha.cotco3,1,0)
#             nha.cotco4=tinhtien(nha.cotco4,1,0)

#             nha.laco1=tinhtien(nha.laco1,1,0)
#             nha.laco2=tinhtien(nha.laco2,1,0)
#             nha.laco3=tinhtien(nha.laco3,1,0)
#             nha.laco4=tinhtien(nha.laco4,1,0)
#         count += 1

# if __name__ == "__main__":
#     bg = turtle.Turtle()
#     bg.hideturtle()

#     vebg(bg)
#     drawOxy()
#     thunhocay2(bg)

#     cloud = turtle.Turtle()
#     cloud.hideturtle()
#     maybay(cloud)
#     vemay(cloud)
#     turtle.exitonclick()