import cv2 as cv

img = cv.imread("c:/Users/emine/Desktop/OpenCv/advanced/Photos/cats.jpg")
cv.imshow("cats", img)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("gray", gray)

# Simple Thresholding
    #Basit thresholding (eşikleme), bir gri tonlamalı görüntüyü siyah ve beyaz bölgelere ayırmak için kullanılan bir yöntemdir. 
    #Bu yöntemde, bir eşik değeri belirlenir ve bu değerin altındaki pikseller siyah, üstündeki pikseller beyaz olur. 
    #Bu, görüntüdeki belirli bir kontrast eşiğini belirleyerek nesneleri veya özellikleri vurgulamak için kullanılır.
threshold, thresh = cv.threshold(gray, 150,255, cv.THRESH_BINARY)
# cv.threshold() : 
    # gray: Gri tonlamalı görüntü.
    # threshold_value: Eşik değeri (150).
    # 255: Eşik değerini aşan piksellerin atanacağı değer (beyaz için).
    # cv2.THRESH_BINARY: Binary thresholding işlemi uygula
cv.imshow("simple thresholded", thresh)

threshold, thresh_inv = cv.threshold(gray, 150,255, cv.THRESH_BINARY_INV)
cv.imshow("simple thresholded inverse", thresh_inv)
#tam tersini alır. beyaz olanlar siyah; siyah olanlar beyaz olur.

# Adaptive Thresholding
    #Adaptive thresholding, bir görüntü üzerinde lokal adaptasyon sağlamak için kullanılan bir eşikleme yöntemidir. 
    # Geleneksel basit thresholding, tüm görüntü üzerinde tek bir eşik değeri kullanırken, adaptif thresholding, görüntüdeki farklı bölgeler için adaptasyon sağlar. 
    # Bu yöntem, görüntünün farklı bölgelerindeki kontrast ve aydınlık değişimlerine daha iyi uyum sağlar.

#cv.adaptiveThreshold():
    # gray: Gri tonlamalı görüntü.
    # 255: Eşik değerini aşan piksellerin atanacağı değer (beyaz için).
    # cv2.ADAPTIVE_THRESH_MEAN_C: Adaptif thresholding tipi (ortalama değer kullanılarak).
    # cv2.THRESH_BINARY: Binary thresholding işlemi uygula.
    # 11: Blok boyutu (komşu piksellerin etkileşim alanı).
    # 3: C sabiti (eşik değerinin ortalama değere eklenmesi veya çıkarılması için kullanılan sabit).
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 3)
cv.imshow("adaptive thresholding", adaptive_thresh)
#cv2.ADAPTIVE_THRESH_GAUSSIAN_C : Bu, adaptif thresholding işleminin daha yumuşak geçişlere sahip olmasına ve daha gürültü dirençli olmasına neden olabilir. 

cv.waitKey(0)