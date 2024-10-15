import cv2
import numpy as np

img = cv2.imread("klon.jpg")

dimension = img.shape #resmin boyutlarını verir
colour = img[125, 225] #pikseldeki rgb değerini verir
blue = img[25, 125, 0] #sondaki 0->mavi 1->yeşil 2->kırmızı

green = img.item(25, 125, 1) #hemen üstteki işlemin aynısı
img.itemset((25, 125, 1), 21) #o pixeldeki renk değerini yeniden set etme

cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()