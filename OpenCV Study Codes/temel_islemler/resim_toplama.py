import cv2
import numpy as np

circleCanvas = np.zeros((512, 512, 3), np.uint8) + 255
cv2.circle(circleCanvas , (256,256) , 60 , (255,0,0), -1, )

rectangleCanvas = np.zeros((512, 512, 3), np.uint8) + 255
cv2.rectangle(rectangleCanvas , (150,150), (350,350), (0,0,255,), -1)

ekle = cv2.add(circleCanvas, rectangleCanvas)
dst = cv2.addWeighted(circleCanvas, 0.5, rectangleCanvas, 0.5, 0)

#cv2.imshow("SA", circleCanvas)
#cv2.imshow("AS", rectangleCanvas)
cv2.imshow("ekle", ekle)
cv2.imshow("dst", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()