import numpy as np
import cv2 as cv
def nothing(x):
    pass
# 创建一个黑色图像，一个窗口
img = np.zeros((300,512,3), np.uint8)
cv.namedWindow('image')
# 建一個拖曳調整BARcv.createTrackbar(trackbarName, 視窗名, 最小值(範圍), 最大值(範圍),要做什麼事(CALL function))
cv.createTrackbar('R','image',0,255,nothing)
cv.createTrackbar('G','image',0,255,nothing)
cv.createTrackbar('B','image',0,255,nothing)
# 创建一个开关用来启用和关闭功能的
switch = '0 : OFF \n1 : ON'
cv.createTrackbar(switch, 'image',0,1,nothing)
while(1):
    cv.imshow('image',img)

    k = cv.waitKey(1) & 0xFF
    if k == 27:
        break

    # get current positions of four trackbars
    #cv.setMouseCallback會自動回傳滑鼠位置，trackbar要用cv.getTrackbarPos(抓哪一個trackbar名,視窗)
    r = cv.getTrackbarPos('R','image')
    g = cv.getTrackbarPos('G','image')
    b = cv.getTrackbarPos('B','image')
    s = cv.getTrackbarPos(switch,'image')
    if s == 0:
        img[:] = 0 
    else:
        img[:] = [b,g,r]

cv.destroyAllWindows()