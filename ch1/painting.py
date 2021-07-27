import numpy as np
import cv2 as cv
# 創建一个黑色的圖片
img = np.zeros((512,512,3), np.uint8)

#畫線cv.line(要畫的圖片, 開始的坐標, 结束的坐標, color, 线或圆等的寬度{ 數值為-1 :填滿}, lineType)
# 畫一條 5px 寬的藍色对角線
cv.line(img, (0, 0), (110, 110), (255, 0, 0), 5, cv.LINE_AA)
cv.line(img, (512, 0), (360, 110), (255, 0, 0), 5, cv.LINE_AA)

#畫矩形cv.rectangle(要畫的圖片, 矩形左上角的坐標, 矩形右下角的坐標, color, 线或圆等的寬度{ 數值為-1 :填滿})
cv.rectangle(img, (110,110), (210,220), (0,255,0),3)
cv.rectangle(img, (260,110), (360,220), (0,255,0),3)

#畫圓cv.circle(要畫的圖片, 圆心的坐標, 半徑, color, 线或圆等的寬度{ 數值為-1 :填滿})
cv.circle(img,(235,250), 63, (0,0,255), -1)

#畫橢圓(要畫的圖片, 圆心的坐標, 軸的長度 (長軸長度，短軸長度), 旋轉角度, startAngle, endAngle(startAngle, endAngle要畫多少面積0,360是完整橢圓 0,180半個橢圓),  color, 线或圆等的寬度{ 數值為-1 :填滿})
cv.ellipse(img, (236,340), (100,50), 0, 0, 180,   (200,110,100), -1)

#畫多邊形pts把點的座標標出來順序為逆時鐘
pts = np.array([[50,450],[35,470],[10,475],[30,480],[10,500],[50,490],[80,505],[70,480],[95,470],[70,465] ], np.int32)
pts = pts.reshape((-1,1,2))
cv.polylines(img,[pts],True,(0,255,255))

#加文字cv.putText(要畫的圖片,要加的字, 起始位置, 字體, 字體大小, 顏色)
cv.putText(img,'hello robot', (110,500), 5, 2.5, (255,255,0))

cv.imshow('paint',img)
cv.waitKey(0)
cv.destroyAllWindows