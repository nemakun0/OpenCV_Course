import cv2 as cv
import numpy as np
# MASKING
# Masking, bir görüntü üzerinde belirli bir bölgeyi seçmek veya belirli bir bölgeyi dışlamak için kullanılan bir işlemdir.

img = cv.imread("c:/Users/emine/Desktop/OpenCv/advanced/Photos/cats.jpg")
cv.imshow("cats", img)

blank = np.zeros(img.shape[:2], dtype="uint8")
cv.imshow("blank image", blank)

circle= cv.circle(blank.copy(), (img.shape[1]//2 + 45, img.shape[0]//2 + 45), 100, 255,-1)
cv.imshow("mask", circle)

rectangle = cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1)

weird_shape = cv.bitwise_and(circle,rectangle)
cv.imshow("weird shape", weird_shape)

masked= cv.bitwise_and(img,img, mask=weird_shape)
cv.imshow("weird shape masked image", masked)

cv.waitKey(0)