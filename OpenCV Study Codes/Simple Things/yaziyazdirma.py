import numpy as np
import cv2

canvas = np.zeros((512,512,3), dtype=np.uint8) + 255
cv2.namedWindow("Canvas",cv2.WINDOW_NORMAL)

font1 = cv2.FONT_HERSHEY_COMPLEX
cv2.putText(canvas, "Mert", (31, 131), font1, 3, (0, 0, 0), cv2.LINE_AA)

cv2.imshow("Canvas", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()