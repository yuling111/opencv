import cv2

img1 = cv2.imread('./img/images.jpg')
res = cv2.resize(img1, None, fx = 2, fy = 2, interpolation = cv2.INTER_CUBIC)
cv2.imshow('images', img1)
cv2.imshow('res', res)
cv2.waitKey(0)

cv2.destroyAllWindows()


