import cv2
import numpy as np

img = cv2.imread('images2.jpg')
lower = cv2.pyrDown(img)
lower1 = cv2.pyrDown(lower)
higher = cv2.pyrUp(lower1)
higher1 = cv2.pyrUp(higher)


cv2.imshow('src', img)
cv2.imshow('lower', lower)
cv2.imshow('lower1', lower1)
cv2.imshow('higher', higher)
cv2.imshow('higher1', higher1)
cv2.waitKey(0) 
cv2.destroyAllWindows()
