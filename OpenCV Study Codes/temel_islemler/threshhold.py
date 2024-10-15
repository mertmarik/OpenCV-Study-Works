import cv2


img = cv2.imread("klon.jpg", 0)

ret, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

cv2.imshow("img", img)
cv2.imshow("th1", th1)

cv2.waitKey(0)