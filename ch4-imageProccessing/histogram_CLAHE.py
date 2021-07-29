import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('cloudy.jpg', 0)


# 使用OpenCV函数实现直方图均衡化
img3 = cv2.equalizeHist(img)
hist3, bins = np.histogram(img3.flatten(), 256, [0, 256])
cdf3 = hist3.cumsum()
cdf_m = cdf3 * hist3.max() / cdf3.max()

plt.subplot(221), plt.imshow(img3, 'gray'), plt.axis('off')
plt.title('OpenCV Equalized')

plt.subplot(222), plt.plot(cdf_m, color='b'),
plt.hist(img3.flatten(), 256, [0, 256], color='r'),
plt.xlim([0, 256]),
plt.legend(('cdf', 'histogram'), loc='upper left'), plt.title('Histogram')

clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
cl1 = clahe.apply(img)
hist4, bins = np.histogram(cl1.flatten(), 256, [0, 256])
cdf4 = hist4.cumsum()
cdf_m1 = cdf4 * hist4.max() / cdf4.max()
plt.subplot(223), plt.imshow(cl1, 'gray'), plt.axis('off')
plt.title('OpenCV CLAHE')

plt.subplot(224), plt.plot(cdf_m1, color='b'),
plt.hist(cl1.flatten(), 256, [0, 256], color='r'),
plt.xlim([0, 256]),
plt.legend(('cdf', 'histogram'), loc='upper left'), plt.title('Histogram')


plt.show()
