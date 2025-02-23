from toado import drawOxy
from vehinhcoban import *
from phepdoihinh import xoay
import turtle
import time
from main import veco


# hàm vẽ cờ bao gồm 1 object flag là 1 object turtle, điểm bên phải phía dưới
# # và điểm bên trái phía trên để vẽ ra hình chữ nhật, color
# def flag (flag, rightBottomFlag, leftTopFlag, color):
#     draw_filled_rectangle(flag, rightBottomFlag, leftTopFlag, color)


# # hàm quay cờ gồm 1 object flag là 1 object turtle, 1 điểm được xoay và tâm xoay
# # và thời gian xoay. Ở đây tâm xoay là điểm bên trái phía trên của lá cờ còn điểm
# # xoay quay là điểm bên phải phía dưới của lá cờ, qua ngược chiều kim đồng hồ

# def spinFlag(flagObject, diemDuocXoay, tamXoay, timeSpin):
#     # timeSpin càng lớn thì cờ xoay càng chậm
#     count = 0
#     # Cụ thể ở đây xoay 10 lần mỗi lần 23deg thời gian quay cách nhau timeSpin
#     while True:
#         diemDuocXoay = xoay(diemDuocXoay, tamXoay, 23)
#         flag(flagObject, diemDuocXoay, tamXoay, 'yellow')
#         turtle.update()
#         time.sleep(timeSpin)
#         flagObject.clear()
#         count += 1
#         if(count == 10):
#             flagObject.clear()
#             flag(flagObject, diemDuocXoay, tamXoay, 'red')
#             break

# bản chất của hàm vẽ ngôi nhà là lấy hình chữ nhật to nhất làm trung tâm và
# phần lớn những thứ khác đều phụ thuộc vào tọa độ đó
def drawHome(nha) :
    # chọn 2 điểm trái trên và phải dưới sao cho phù hợp vs bối cảnh
    leftTopPoint = (50 + 15, 40 - 7)
    rightBottomPoint = (129 + 15, 3)
    # screen = turtle.Screen()
    # screen.setup(width=1.0, height=1.0)

    # drawOxy()
    # tạo đối tượng turtle cho home


    # Large Rectangle
    # tọa độ điểm trái trên của large Rectangle
    leftTopLargeX = leftTopPoint[0]
    leftTopLargeY = leftTopPoint[1]

    # tọa độ điểm phải dưới của large Rectangle
    rightBottomLargeX = rightBottomPoint[0]
    rightBottomLargeY = rightBottomPoint[1]

    # 2 điểm cần thiết để để vẽ large Rectangle
    leftTopLarge=[leftTopLargeX, leftTopLargeY]
    rightBottomLarge=[rightBottomLargeX,rightBottomLargeY]

    # vẽ large Rectangle
    draw_filled_rectangle(nha, rightBottomLarge, leftTopLarge, color='')



    # Small Rectangle (hình chữ nhật nhỏ phía trên large Rectangle)
    # tọa độ x trái trên (tọa độ x trái trên của large Rectangle  +  tọa độ x phải dưới của large Rectangle) / 2 rồi lấy số nguyên
    leftTopSmallX = int((leftTopLargeX + rightBottomLargeX) / 2)

    # chiều dài và cao của Small Rectangle
    wideSmallRegtangle = 10
    heightSmallRegtangle = 5


    leftTopSmallY = leftTopLargeY + heightSmallRegtangle

    # tạo độ trái trên của Small Rectangle
    leftTopSmall=[leftTopLargeX + 10, leftTopSmallY]

    # tạo độ phải dưới của Small Rectangle
    rightBottomSmall=[rightBottomLargeX - wideSmallRegtangle,leftTopLargeY]

    # vẽ hình chữ nhật nhỏ
    draw_filled_rectangle(nha, rightBottomSmall, leftTopSmall, color='yellow')

    # Post Flag
    # chiều dài và cao của Post Flag
    widePostFlag = 1
    heightPostFlag = 20


    leftTopPostFlagX1 = leftTopSmallX - widePostFlag
    leftTopPostFlagY1 = leftTopSmallY + heightPostFlag

    # Tọa độ trái trên của Post Flag
    leftTopPostFlag = [leftTopPostFlagX1,leftTopPostFlagY1]

    rightBottomPostFlagX2 = leftTopSmallX + widePostFlag

    # Tọa độ phải dưới của Post Flag
    rightBottomPostFlag = [rightBottomPostFlagX2,leftTopSmallY]

    # vẽ Post Flag
    # draw_filled_rectangle(home, rightBottomPostFlag, leftTopPostFlag, color='gray')

    # Flag
    leftTopFlagX = leftTopPostFlagX1
    leftTopFlagY = leftTopPostFlagY1

    # Tọa độ trái trên của Flag
    leftTopFlag = [leftTopFlagX, leftTopFlagY]

    # chiều dài và cao của Flag
    lengtOfFlag = 20
    wideOfFlag = 10

    rightBottomFlagX = leftTopFlagX + lengtOfFlag
    rightBottomFlagY = leftTopFlagY - wideOfFlag

    # Tọa độ phải dưới của Flag
    rightBottomFlag = [rightBottomFlagX, rightBottomFlagY]


    # vẽ Flag là 1 hàm riêng
    # flag(flagObject, rightBottomFlag, leftTopFlag, 'yellow')

    # Rectangle Decoration

    # chiều dài và cao của từng Rectangle Decoration
    lengtDecorate = 11
    wideDecorate = 6

    # tọa độ x trái trên của Rectangle Decoration (tọa độ x phải dưới của large Rectangle  -  tọa độ x trái trên của large Rectangle) / 8
    # + tọa độ x trái trên của large Rectangle) rồi lấy số nguyên
    leftTopDecorateX = int((rightBottomLargeX - leftTopLargeX) / 8 + leftTopLargeX)

    # tọa độ y trái trên Rectangle Decoration (tọa độ y trái trên của large Rectangle  +  tọa độ y phải dưới của large Rectangle) / 2
    # + chiều cao của Rectangle Decoration
    leftTopDecorateY = int((leftTopLargeY + rightBottomLargeY) / 2 + lengtDecorate)

    # Tọa độ trái trên của Rectangle Decoration
    leftTopDecorate = [leftTopDecorateX, leftTopDecorateY]

    # tọa độ x phải dưới của Rectangle Decoration (tọa độ x phải dưới của large Rectangle  -  tọa độ x trái trên của large Rectangle) / 8
    # + tọa độ x trái trên của large Rectangle + độ rộng của Rectangle Decoration) rồi lấy số nguyên
    rightBottomDecorateX = int((rightBottomLargeX - leftTopLargeX) / 8 + leftTopLargeX + wideDecorate)

    # tọa độ y phải dưới Rectangle Decoration (tọa độ y trái trên của large Rectangle  +  tọa độ y phải dưới của large Rectangle) / 2
    # - chiều cao của Rectangle Decoration
    rightBottomDecorateY = int((leftTopLargeY + rightBottomLargeY) / 2 - lengtDecorate)

    # Tọa độ phải dưới của Rectangle Decoration
    rightBottomDecorate = [rightBottomDecorateX, rightBottomDecorateY]

    # khoảng cách giữa các Rectangle Decoration
    space = 0
    for i in range(5):
        draw_filled_rectangle(nha, [rightBottomDecorate[0] + space, rightBottomDecorate[1]],
                              [leftTopDecorate[0] + space, leftTopDecorate[1]], color='yellow')
        space += 14

    # turtle.mainloop()
    # return flagObject, (rightBottomFlag, leftTopFlag)




# bổ xung phần bạn Bảo
#bộ điểm đại diện cho lá cờ
# cotco1=[103,38]
# cotco2=[105,38]
# cotco3=[105,48]
# cotco4=[103,48]

laconha1=[103,48]
laconha2=[122,48]
laconha3=[122,58]
laconha4=[103,58]

# def veco(co,color="yellow"):
#     ve_doan_thang(co,cotco1,cotco2)
#     ve_doan_thang(co,cotco2,cotco3)
#     ve_doan_thang(co,cotco3,cotco4)
#     ve_doan_thang(co,cotco4,cotco1)
#     co.begin_fill()
#     co.fillcolor("gray")
#     ve_doan_thang(co,cotco1,cotco2)
#     ve_doan_thang(co,cotco2,cotco3)
#     ve_doan_thang(co,cotco3,cotco4)
#     ve_doan_thang(co,cotco4,cotco1)
#     co.end_fill()

#     co.begin_fill()
#     co.fillcolor(color)
#     ve_doan_thang(co,laco1,laco2)
#     ve_doan_thang(co,laco2,laco3)
#     ve_doan_thang(co,laco3,laco4)
#     ve_doan_thang(co,laco4,laco1)
#     co.end_fill()


# def xoayco(co):
#     global cotco1,cotco2,cotco3,cotco4,laconha1,laconha2,laconha3,laconha4
#     count=0
#     while True:
#         if count <=12:
#             veco(co)
#         elif count <=22:
#             veco(co,"red")
#         else:
#             break
#         turtle.update()
#         time.sleep(0.03)
#         co.clear()   
        
#         cotco2=xoay(cotco2,cotco1,15)
#         cotco3=xoay(cotco3,cotco1,15)
#         cotco4=xoay(cotco4,cotco1,15)

#         laconha1=xoay(laconha1,cotco1,15)
#         laconha2=xoay(laconha2,cotco1,15)
#         laconha3=xoay(laconha3,cotco1,15)
#         laconha4=xoay(laconha4,cotco1,15)
#         count+=1
       
            


# if __name__=="__main__":
#     co=turtle.Turtle()
#     co.hideturtle()
#     drawHome()
#     veco(co)
#     xoayco(co)
#     veco(co,"red")
#     turtle.exitonclick()
