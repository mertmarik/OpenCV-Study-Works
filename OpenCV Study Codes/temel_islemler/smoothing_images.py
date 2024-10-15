import cv2
import numpy as np

img_filter = cv2.imread(r"C:\Users\MERT\PycharmProjects\pythonProject2\fotolar\filter.jpg")
img_median = cv2.imread(r"C:\Users\MERT\PycharmProjects\pythonProject2\fotolar\median.jpg")
img_bilateral = cv2.imread(r"C:\Users\MERT\PycharmProjects\pythonProject2\fotolar\bilateral.jpg")

blur = cv2.blur(img_median, (9, 9))
blurM = cv2.medianBlur(img_median,1)
blurB = cv2.bilateralFilter(img_bilateral, 9, 75, 75)#75 kısmı ne kadar artarsa pütürler o kadar azaları

cv2.imshow("Median Blur", blurM)
cv2.imshow("Blur", blur)
cv2.imshow("Foto", img_median)
cv2.imshow("Bilateral", blurB)

cv2.waitKey(0)
cv2.destroyAllWindows()
