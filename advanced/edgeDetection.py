import cv2 as cv
import numpy as np

img = cv.imread("c:/Users/emine/Desktop/OpenCv/advanced/Photos/park.jpg")
cv.imshow("park", img)

gray  = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray", gray)

# Laplacian
    # Laplacian, bir matematiksel operatördür ve görüntülerdeki yoğunluk değişikliklerini belirleyerek kenarları tespit etmek için kullanılır. 
    # Laplacian operatörü, bir pikseldeki yoğunluk değişimini belirlemede yardımcı olur ve bu, görüntüdeki kenarların bulunmasına olanak tanır.
# cv.Laplacian(src, ddepth[, ksize[, scale[, delta[, borderType]]]])
    # src: Giriş görüntüsü.
    # ddepth: Çıkış görüntüsünün derinliği. Genellikle cv2.CV_64F veya cv2.CV_8U gibi değerler kullanılır.
    # ksize: Laplacian çekirdeğinin boyutu. Genellikle 1, 3 veya 5 kullanılır. Varsayılan değer 1'dir.
    # scale: Türetilmiş görüntüye uygulanan ölçek faktörü.
    # delta: Türetilmiş görüntüye eklenecek olan delta değeri.
    # borderType: Kenar pikselleri için kullanılan doldurma yöntemi.

lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
#cv.Laplacian() fonksiyonu, gri tonlamalı görüntü üzerinde Laplacian operatörünü uygular.
#Elde edilen Laplacian matrisindeki değerlerin mutlak değerini almak için np.absolute() fonksiyonu kullanılır.
#np.uint8() fonksiyonu ile Laplacian matrisinin veri tipi uygun bir şekilde dönüştürülür. 
    #Laplacian operatörünün sonucu genellikle negatif ve pozitif değerleri içerir, bu nedenle bu değerlerin mutlak değeri alınarak pozitif bir görüntü elde edilir.
cv.imshow ("laplacian", lap)

# Sobel
    # Sobel operatörü, bir görüntü üzerindeki yoğunluk değişikliklerini belirleyerek kenarları tespit etmek için kullanılan bir matematiksel operatördür. 
    # Bu operatör, bir pikseldeki yoğunluk değişimini dikey (yukarı-aşağı) ve yatay (sol-sağ) yönlere göre ayrı ayrı ölçer. 
    # Ardından, bu iki gradyanın büyüklüğü ve yönü kullanılarak kenar tespiti yapılır.

#sobelx = cv.Sobel(src, ddepth, dx, dy[, ksize[, scale[, delta[, borderType]]]])
    # src: Giriş görüntüsü.
    # ddepth: Çıkış görüntüsünün derinliği. Genellikle cv2.CV_64F veya cv2.CV_8U gibi değerler kullanılır.
    # dx ve dy: X ve Y yönlerindeki gradyanların derecesi.
    # ksize: Sobel çekirdeğinin boyutu. Genellikle 1, 3 veya 5 kullanılır. Varsayılan değer 3'tür.
    # scale: Türetilmiş görüntüye uygulanan ölçek faktörü.
    # delta: Türetilmiş görüntüye eklenecek olan delta değeri.
    # borderType: Kenar pikselleri için kullanılan doldurma yöntemi.

sobelx = cv.Sobel(gray, cv.CV_64F, 1,0)
sobely = cv.Sobel(gray, cv.CV_64F, 0,1)
combined_sobel = cv.bitwise_or(sobelx,sobely)

cv.imshow("sobel X",sobelx)
cv.imshow("sobel Y",sobely)
cv.imshow("combined sobel",combined_sobel)

canny= cv.Canny(gray,150,175)
cv.imshow("canny" ,canny)
#canny uygulayarak daha sade bir hal elde etmiş olduk ve bu sade hal laplacian ile daha çok benzerlik içerdi.

cv.waitKey(0)