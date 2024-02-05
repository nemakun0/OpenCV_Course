import cv2 as cv
import numpy as np

blank = np.zeros((400,400), dtype="uint8")

rectangle = cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1)
circle = cv.circle(blank.copy(), (200,200), 200,255,-1)

cv.imshow("rectangle", rectangle)
cv.imshow("circle", circle)

# bitwise AND ---> intersection regions
    #Bitwise AND işlemi, her iki pikselin karşılık gelen bitlerinin 1 olduğu durumu işaret eder. 
    #Bu, iki görüntünün belirli bir bölgesinde her iki görüntüde de beyaz piksellerin olduğu yerlerin belirlenmesinde kullanılır.
bitwise_and = cv.bitwise_and(rectangle,circle)
cv.imshow("bitwise AND", bitwise_and)

# bitwise OR ---> non-intersection and intersecting regions
    #her iki pikselin karşılık gelen bitlerinden en az birinin 1 olduğu durumu işaret eder. 
    #Bu işlem, iki görüntüde en az birinde beyaz piksellerin olduğu yerleri birleştirmek için kullanılır.
bitwise_or = cv.bitwise_or(rectangle, circle)
cv.imshow("bitwise OR", bitwise_or)

# bitwise XOR ---> non-intersecting regions
    #her iki pikselin karşılık gelen bitlerinin farklı (biri 1, diğeri 0) olduğu durumu işaret eder. 
    #Bu işlem, iki görüntüde sadece birinde beyaz piksellerin olduğu yerleri belirlemek için kullanılır.
bitwise_xor = cv.bitwise_xor(rectangle,circle)
cv.imshow("bitwise XOR", bitwise_xor)

# bitwise NOT
    #Bitwise NOT işlemi, her pikselin değerini tersine çevirir; yani, 1'leri 0 yapar, 0'ları 1 yapar.
bitwise_not = cv.bitwise_not(rectangle)
cv.imshow("rectangle NOT", bitwise_not)

cv.waitKey(0)