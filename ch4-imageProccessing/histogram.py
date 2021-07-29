import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('images1.jpg')     
plt.subplot(211)
plt.title('Use plt.hist(Matplotlib)')
plt.hist(img.ravel(), 256,[0,256])


# cv2.calcHist([哪張圖且'[]'是必須的],[計算哪個顏色],mask遮罩图像,[histSize(256全尺)],[ranges])
'''
註1:如果输入為灰度圖像，則其值为[0]。對於彩色图像，藍色 -> [0]，綠色 -> [1]，红色 -> [2]。
'''
color = ('b','g','r')
plt.subplot(212)
plt.title('Use cv2.calcHist')
for i,col in enumerate(color):
    histr = cv2.calcHist([img],[i],None,[256],[0,256])
 
    plt.plot(histr,color = col)
    plt.xlim([0,256])

plt.show()

img = cv2.imread('images2.jpg',0)
# create a mask
mask = np.zeros(img.shape[:2], np.uint8)
mask[150:280, 100:400] = 255
masked_img = cv2.bitwise_and(img,img,mask = mask)
# Calculate histogram with mask and without mask
# Check third argument for mask
hist_full = cv2.calcHist([img],[0],None,[256],[0,256])
hist_mask = cv2.calcHist([img],[0],mask,[256],[0,256])
plt.subplot(221), plt.title('img'), plt.imshow(img, 'gray')
plt.subplot(222), plt.plot(hist_full)
plt.subplot(223), plt.title('masked_img'), plt.imshow(masked_img, 'gray')
plt.subplot(224), plt.plot(hist_full), plt.plot(hist_mask)
plt.xlim([0,256])
plt.show()