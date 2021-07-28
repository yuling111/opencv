import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('images1.jpg')
cv2.namedWindow('image')
blur = cv2.GaussianBlur(img,(9,9),0)
gray = cv2.cvtColor(blur,cv2.COLOR_BGR2GRAY)
scharrx = cv2.Sobel(gray,cv2.CV_64F,1,0)
scharry = cv2.Sobel(gray,cv2.CV_64F,0,1)
scharrx = cv2.convertScaleAbs(scharrx)
scharry = cv2.convertScaleAbs(scharry)
scharrxy = cv2.addWeighted(scharrx,0.5,scharry,0.5,0)
edges1 = cv2.Canny(scharrxy,50,200) 
contours, hi = cv2.findContours(edges1,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
img1 = edges1
newcontours=[]

#contour(輪廓) features:輪廓面積 -> cv2.contourArea(contour) 輪廓周長 -> cv2.arcLength(contour,True)
if cv2.contourArea(contours) > 200 and cv2.arcLength(contours,True) < 200:
        newcontours.append(contours)

#畫contour(輪廓):cv2.drawContours(哪一張圖, 找出來的contours, 要畫第幾個contours(-1:全部), 顏色, 粗細)
cv2.drawContours(img,newcontours,-1,(0,255,0),2)
print(len(contours),len(newcontours))

for a in newcontours:
    print('周長:', cv2.arcLength(a,True), '面積:', cv2.contourArea(a))

#矩cv.moments(contours)图像矩可帮助您计算某些特征，例如物体的重心，物体的面积等。
# print(cv2.moments(contours[100]))


cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()  