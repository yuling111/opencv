#图像加法
x = np.uint8([250])
y = np.uint8([10])

print(cv.add(x,y)) #250 + 10 =260 => 255


print(x + y)
#Import only if not previously imported
import cv2
VariableName = cv2.imread("Address",flag)     #(flag = 0 or 1 or -1)
