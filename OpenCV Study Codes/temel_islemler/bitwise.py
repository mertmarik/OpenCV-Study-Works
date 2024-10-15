import cv2
import numpy as np

img1 = cv2.imread(r"C:\Users\MERT\PycharmProjects\pythonProject2\fotolar\bitwise_1.png")
img2 = cv2.imread(r"C:\Users\MERT\PycharmProjects\pythonProject2\fotolar\bitwise_2.png")

bitt = cv2.bitwise_and(img1, img2)

cv2.imshow("bitt", bitt)
cv2.imshow("img1", img1)
cv2.imshow("img2", img2)

cv2.waitKey(0)
cv2.destroyAllWindows()