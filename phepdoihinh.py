import numpy as np
import math


def tinhtien(A,dx,dy): #input là một mảng 1 chiều có 2 phần tử tọa độ x,y và hướng tịnh tiến dx,dy

    A=np.append(A,1)
    matrixA=A.reshape(1,-1)  #biến mảng 1 chiều thành ma trận 2 chiều
    matrixTinhTien=np.array([[1, 0, 0], 
                             [0, 1, 0], 
                             [dx, dy, 1]])

    ketqua=np.dot(matrixA,matrixTinhTien) #nhân 2 ma trận
    return np.delete(ketqua.flatten(), 2) #biến mảng 2 chiều thành mảng 1 chiều và xóa phần tử thứ 3 đi




def xoay(A,O,degree): #xoay điểm A quanh B một gốc degree độ
    A=np.append(A,1)
    matrixA=A.reshape(1,-1)  #biến mảng 1 chiều thành ma trận 2 chiều
    dx=O[0]
    dy=O[1]
    radian=math.radians(degree)   


    matrixTinhTien1=np.array([[1, 0, 0], 
                            [0, 1, 0], 
                            [-dx, -dy, 1]])
    
    matrixXoay=np.array([[math.cos(radian), math.sin(radian), 0], 
                        [-math.sin(radian), math.cos(radian), 0], 
                        [0, 0, 1]])
    
    matrixTinhTien2=np.array([[1, 0, 0], 
                            [0, 1, 0], 
                            [dx, dy, 1]])
    
    tichMatrix= np.dot(matrixTinhTien1, np.dot(matrixXoay, matrixTinhTien2))
    ketqua=np.dot(matrixA,tichMatrix)
    ketqua=np.delete(ketqua.flatten(), 2) 
    ketqua=[round(ketqua[0]),round(ketqua[1])]
    return ketqua
    
def thuphong(A,O,sx,sy):  # Thu Phóng điểm A so với B một size 
    A=np.append(A,1)
    matrixA=A.reshape(1,-1)  #biến mảng 1 chiều thành ma trận 2 chiều
    dx=O[0]
    dy=O[1]
    matrixTinhTien1=np.array([[1, 0, 0], 
                             [0, 1, 0], 
                             [-dx, -dy, 1]])
    

    matrixTyle=np.array([[sx, 0, 0], 
                        [0, sy, 0], 
                        [0, 0, 1]])
    
    matrixTinhTien2=np.array([[1, 0, 0], 
                        [0, 1, 0], 
                        [dx, dy, 1]])

    tichMatrix= np.dot(matrixTinhTien1, np.dot(matrixTyle, matrixTinhTien2))
    ketqua=np.dot(matrixA,tichMatrix)
    ketqua=np.delete(ketqua.flatten(), 2) 
    ketqua=[round(ketqua[0]),round(ketqua[1])]
    return ketqua

def doixungOy(A,O):
    A=np.append(A,1)
    matrixA=A.reshape(1,-1)  #biến mảng 1 chiều thành ma trận 2 chiều
    dx=O[0]
    dy=O[1]
    matrixTinhTien1=np.array([[1, 0, 0], 
                             [0, 1, 0], 
                             [-dx, -dy, 1]])
    

    matrixDoixung=np.array([[-1, 0, 0], 
                        [0, 1, 0], 
                        [0, 0, 1]])
    
    matrixTinhTien2=np.array([[1, 0, 0], 
                        [0, 1, 0], 
                        [dx, dy, 1]])

    tichMatrix= np.dot(matrixTinhTien1, np.dot(matrixDoixung, matrixTinhTien2))
    ketqua=np.dot(matrixA,tichMatrix)
    return np.delete(ketqua.flatten(), 2) 
    

if __name__=="__main__":

    a= np.array([1, 2])
    a=doixungOy([1,1],[0,0])
    x,y=a
    print (a)