import numpy as np
import cv2 as cv

# 鼠标回调函数

def draw_circle(event,x,y,flags,param):
    if event == cv.EVENT_LBUTTONDBLCLK:
        cv.circle(img,(x,y),10,(255,0,0),-1)
    elif event == cv.EVENT_RBUTTONDOWN:
        cv.rectangle(img, (x,y), (x+50,y+5), (0,0,255),3)   
# 创建一个黑色图像，一个窗口，然后和回调绑定
img = np.zeros((512,512,3), np.uint8)
cv.namedWindow('image')

#抓滑鼠的動作cv.setMouseCallback(視窗, 要做什麼動作(觸發哪個funtion))
cv.setMouseCallback('image',draw_circle)

while(1):
    cv.imshow('image',img)
    if cv.waitKey(20) & 0xFF == 27:
        break
cv.destroyAllWindows()