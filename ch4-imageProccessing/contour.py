import cv2
import numpy as np
from matplotlib import pyplot as plt

src = cv2.imread('test21.jpg')
img = src.copy()
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgray, 127, 255, 0)

#找contour(輪廓):cv2.findContours(哪一張圖(註), 找contour的方法(註1), 逼近的方法(註2))
'''
註:为了获得更高的准确性，请使用二进制图像。因此，在找到轮廓之前，请应用阈值或 Canny 边缘检测
註1:找contour的方法 -> cv2.RETR_EXTERNAL, cv2.RETR_TREE, cv2.RETR_CCOMP, cv2.RETR_LIST
註2:逼近的方法 -> cv2.CHAIN_APPROX_NONE(會儲存所有邊界點), cv2.CHAIN_APPROX_SIMPLE(删除所有冗餘並壓縮輪廓，從而節省内存。)
'''
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
print(len(contours),contours[0])
#cnt = contours[0]


#畫contour(輪廓):cv2.drawContours(哪一張圖, 找出來的contours, 要畫第幾個contours(-1:全部), 顏色, 粗細)
draw = cv2.drawContours(img, contours, -1, (0, 255, 0), 10)

plt.subplot(121), plt.imshow(cv2.cvtColor(src, cv2.COLOR_BGR2RGB)), plt.title('Src')
plt.subplot(122), plt.imshow(cv2.cvtColor(draw, cv2.COLOR_BGR2RGB)), plt.title('image')
plt.show()
