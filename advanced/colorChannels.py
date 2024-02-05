import cv2 as cv
import numpy as np

img = cv.imread("c:/Users/emine/Desktop/OpenCv/advanced/Photos/park.jpg")
cv.imshow("park", img)

blank  =np.zeros(img.shape[:2], dtype= "uint8")

#bu şekilde parçalayıp baktığımızda grayscale formatında resimler elde ediyoruz
b,g,r = cv.split(img)

#bu şekilde parçaladığımızda ise renkli şekilde parçalanmış resimler elde
blue = cv.merge([b,blank,blank])
green = cv.merge([blank,g,blank])
red = cv.merge([blank,blank,r])

cv.imshow("blue", blue)
cv.imshow("green", green)
cv.imshow("red", red)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

merged = cv.merge([b,g,r])
cv.imshow("Merged Image", merged)

cv.waitKey(0)