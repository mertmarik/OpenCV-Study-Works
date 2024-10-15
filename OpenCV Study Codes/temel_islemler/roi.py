import cv2
import numpy as np

#roi ---> region of interest

img = cv2.imread("klon.jpg")

roi = img[30:200, 200:400]




cv2.imshow("ROI", roi)
#cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()