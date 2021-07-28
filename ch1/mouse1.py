import numpy as np
import cv2 as cv

img = np.zeros((512,512,3), np.uint8)
cv.namedWindow('image')


drawing = False # 如果 True 是鼠标按下
mode = True # 如果 True，画矩形，按下‘m’切换到曲线
ix,iy = -1,-1
b, g, r = 0,0,0
def nothing(x):
    pass

# 建一個拖曳調整BARcv.createTrackbar(trackbarName, 視窗名, 最小值(範圍), 最大值(範圍),要做什麼事(CALL function))
cv.createTrackbar('R','image',0,255,nothing)
cv.createTrackbar('G','image',0,255,nothing)
cv.createTrackbar('B','image',0,255,nothing)
# 鼠标回调函数
def draw_circle(event,x,y,flags,param):
    global ix,iy,drawing,mode,b,g,r
    if event == cv.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy = x,y
    elif event == cv.EVENT_MOUSEMOVE:
        if drawing == True:
            if mode == True:
                cv.rectangle(img,(ix,iy),(x,y),(b,g,r),-1)
            else:
                cv.circle(img,(x,y),5,(b,g,r),-1)
    elif event == cv.EVENT_LBUTTONUP:
        drawing = False
        if mode == True:
            cv.rectangle(img,(ix,iy),(x,y),(b,g,r),-1)
        else:
            cv.circle(img,(x,y),5,(b,g,r),-1)
cv.setMouseCallback('image',draw_circle)          


while(1):
    cv.imshow('image',img)
    r = cv.getTrackbarPos('R','image')
    g = cv.getTrackbarPos('G','image')
    b = cv.getTrackbarPos('B','image')
    k = cv.waitKey(1) & 0xFF

    if k == ord('m'):
        mode = not mode 
    elif k == 27:
        break
   
cv.destroyAllWindows()