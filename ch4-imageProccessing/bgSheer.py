import cv2
import matplotlib.pyplot as plt

#需要做的就是向图像添加一个带有前景的Alpha通道。
file_name ="BG.png"
src = cv2.imread(file_name, 1)
src = cv2.cvtColor(src, cv2.COLOR_RGB2BGR)
tmp = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

_,alpha = cv2.threshold(tmp,0,255,cv2.THRESH_BINARY)
print(_,alpha)
b, g, r = cv2.split(src)
rgba = [b,g,r, alpha]
print(rgba[0])
dst = cv2.merge(rgba,4)

#cv2.imwrite("bgSheerPng.png", dst)  #要用png存
plt.subplot(3,3,1)
plt.title('original'), plt.imshow(src)

plt.subplot(3,3,2)
plt.title('BGR2GRAY'), plt.imshow(tmp)

plt.subplot(3,3,3)
plt.title('bgSheer'), plt.imshow(dst)
plt.show()

'''
src = https://www.codenong.com/40527769/
'''