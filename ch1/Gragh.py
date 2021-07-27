import cv2 as cv
from matplotlib import pyplot as plt

#讀圖cv.imread(圖片路徑, 取圖片的方式 )
'''
取圖片的方式:cv.IMREAD_COLOR     =1  ->彩色(default)
            cv.IMREAD_GRAYSCALE =0  ->灰階
            cv.IMREAD_UNCHANGED =-1 ->加载图像，包括 alpha 通道
'''
img = cv.imread('./img/images.jpg', cv.IMREAD_COLOR)
img1 = cv.imread('./img/images.jpg', 1)
img2 = cv.imread('./img/images.jpg', 0)

#秀圖
'''
cv.imshow(視窗名, 要顯示的圖片)
cv.waitKey() 是一个键盘绑定函数，它的参数是以毫秒为单位的时间。
该函数为任意键盘事件等待指定毫秒。如果你在这段时间内按下任意键，程序将继续。
如果传的是 0，它会一直等待键盘按下。它也可以设置检测特定的击键，例如，按下键 a 等
'''
cv.imshow('image', img) 
cv.imshow('image1', img1) 
cv.imshow('image2', img2) 
cv.waitKey(0)
cv.destroyAllWindows()

#保存圖片cv.imwrite(檔名, 要存的圖)
cv.imwrite('messigray.png',img)

k = cv.waitKey(0) & 0xFF
if k == 27: # 按 ESC 退出
    cv.destroyAllWindows()
elif k == ord('s'): # 按 's' 保存退出
    cv.imwrite('messigray.png',img)
    cv.destroyAllWindows()

#使用 Matplotlib可以直接在視窗缩放图像，保存图像等
imgPlt = cv.imread('./img/images.jpg',0)
plt.imshow(imgPlt, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([]) # 隐藏 X 和 Y 轴的刻度值
plt.show()

'''
彩色圖片 OpenCV 用的是 BGR 模式，但是 Matplotlib 顯示用的是 RGB 模式。
因此如果圖片用 OpenCV 加载，則 Matplotlib 中彩色圖片將無法正常顯示。
如下方範例
'''
imgPltColor = cv.imread('./img/images.jpg',1)
plt.imshow(imgPltColor, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([]) # 隐藏 X 和 Y 轴的刻度值
plt.show()

#解決辦法，使用 cv.cvtColor BGR to RGB:
img2 = cv.cvtColor(imgPltColor, cv.COLOR_BGR2RGB)
plt.imshow(img2, interpolation = 'bicubic')
# plt.xticks([]), plt.yticks([]) # 隐藏 X 和 Y 轴的刻度
plt.show()