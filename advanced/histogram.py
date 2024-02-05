import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

#Histogram, bir görüntüdeki piksellerin renk yoğunluklarını gösteren bir grafiktir. 
#Bu grafik, görüntüdeki farklı renk seviyelerinin dağılımını ve frekansını analiz etmeye yardımcı olur.

img = cv.imread("c:/Users/emine/Desktop/OpenCv/advanced/Photos/cats.jpg")
cv.imshow("cats", img)

blank = np.zeros(img.shape[:2], dtype="uint8")

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray", gray)

mask= cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255,-1)

masked = cv.bitwise_and(img,img, mask=mask)
cv.imshow("mask", masked)

# Grayscale Histogram
gray_hist = cv.calcHist([gray], [0], mask, [256], [0,256])
    #cv2.calcHist() fonksiyonu, görüntünün histogramını hesaplar. 
    #[0] ile kanal numarası belirtilir (siyah-beyaz olduğu için 0), 
    #None ile maske belirtilmez, 
    #[256] ile histogramın toplam bin sayısı belirtilir, 
    #[0, 256] ile histogramın değer aralığı belirtilir

plt.figure()
plt.title("Grayscale Histogram")
plt.xlabel("bins")
plt.ylabel("# of pixels")
plt.plot(gray_hist)
plt.xlim([0,256])
plt.show()

plt.figure()
plt.title("Grayscale Histogram")
plt.xlabel("bins")
plt.ylabel("# of pixels")

# Color Histogram
    #Renk histogramı, bir renkli görüntünün renk bileşenlerinin (örneğin, kırmızı, yeşil ve mavi) histogramını gösteren bir grafiktir. 
    #Her renk bileşeni için ayrı bir histogram oluşturularak renk dağılımının analizi yapılabilir. 
    #Bu analiz, görüntüdeki renklerin frekansını anlamak ve renk dağılımını değerlendirmek için kullanılır.
colors = ("b", "g","r")
for i,col in enumerate(colors):
    hist  = cv.calcHist([img], [i], mask, [256], [0,256])
    #cv2.calcHist() fonksiyonu, görüntünün renk histogramını her bir renk kanalı (mavi, yeşil, kırmızı) için ayrı ayrı hesaplar.
    plt.plot(hist, color = col)
    plt.xlim([0,256])
    #plt.xlim([0, 256]) kodu, x-ekseni sınırlarını belirleyerek histogram grafiğinin x-ekseni aralığını 0 ile 256 arasında sınırlar.

plt.show()


cv.waitKey(0)