import cv2
import numpy as np

img = cv2.imread("klon.jpg", 0)

kernel = np.ones((5,5), np.uint8)
erosion = cv2.erode(img, kernel, iterations = 10)
dilation = cv2.dilate(img, kernel, iterations = 10)
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel) #kenarları belirginleştiiyor

cv2.imshow("img", img)
cv2.imshow("gradient", gradient)
cv2.waitKey(0)