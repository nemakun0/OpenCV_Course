import cv2 as cv
import numpy as np

img = cv.imread("c:/Users/emine/Desktop/OpenCv/basics/Photos/cats.jpg")
cv.imshow("cats", img)

blank = np.zeros(img.shape,dtype="uint8")
cv.imshow("blank", blank)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray", gray)

blur = cv.GaussianBlur(gray,(5,5), cv.BORDER_DEFAULT)
cv.imshow("blur", blur)

canny = cv.Canny(blur,125,175)
cv.imshow("canny", canny)

ret,  thresh = cv.threshold(gray,125,255, cv.THRESH_BINARY)
#Bu satır, bir gri tonlamalı görüntüyü siyah-beyaz (binary) bir görüntüye dönüştürmek için kullanılan bir işlemi gerçekleştirir.
    #125: Eşik değeri. Bu değerden düşük pikseller siyah, bu değerden yüksek pikseller beyaz olacaktır.
    #255: Maksimum değer. Eşikleme sonrasında kullanılacak maksimum değer (genellikle beyaz için kullanılır).
    #cv.THRESH_BINARY: Thresholding tipini belirten bir bayrak. Bu durumda, eşik değerini geçen pikseller beyaz, geçmeyen pikseller siyah olacaktır.
#Bu satırın çıkışı iki değer içerir:
    #ret: Kullanılan eşik değerini döndürür. Bu, uygulanan eşikleme işleminde otomatik olarak belirlenen bir değer olabilir.
    #thresh: Eşiklenmiş (siyah-beyaz) görüntüyü temsil eden bir matristir.
cv.imshow("thresh", thresh)

#"Contours" (veya konturlar), bir nesnenin sınırlarını temsil eden, aynı renk veya yoğunluğa sahip olan piksellerin birleşiminden oluşan bir çizgi dizisidir.
contours, hierarchies= cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
#contours, hierarchy = cv2.findContours(image, mode, method)
    #image: Konturları bulmak için kullanılacak binarize (siyah-beyaz) görüntü.
    #mode: Kontur bulma modunu belirten bir parametre. Örneğin, cv2.RETR_EXTERNAL yalnızca dış konturları bulur.
    #method: Kontur yaklaşım yöntemini belirten bir parametre. Örneğin, cv2.CHAIN_APPROX_SIMPLE konturun yalnızca başlangıç ve bitiş noktalarını saklar.
#Fonksiyonun çıkışı:
    #contours: Bulunan konturların listesi.
    #hierarchy: Konturların hiyerarşik yapısını içeren bir dizidir.
#RETR_LIST: Bu mod, tüm konturları bulur, ancak hiyerarşik yapıyı dikkate almaz.
#RETR_TREE: Bu mod, konturları hiyerarşik bir yapı içinde bulur. Yani, konturların iç içe geçmiş bir yapıda olup olmadığını gösterir.
#CHAIN_APPROX_NONE:  Bu yöntem, konturları herhangi bir yaklaşım (approximation) yapmadan tespit eder ve her pikseli içeren bir liste olarak saklar. 
#CHAIN_APPROX_LIST: Bu yöntem, bir konturu daha basitleştirmek için Douglas-Peucker algoritmasını kullanarak temsil eder. Yani, benzer noktaları birleştirir ve daha az sayıda noktayla bir yaklaşık kontur oluşturur.
print(f"{len(contours)} contour(s) found!")

cv.drawContours(blank, contours, -1, (0,0,255),1)
#cv.drawContours(image, contours, contourIdx, color, thickness)
    # image: Çizilecek olan hedef görüntü.
    # contours: Çizilecek olan konturların listesi.
    # contourIdx: Çizilecek olan konturun indeksi. -1 değeri, tüm konturları çizmeyi ifade eder.
    # color: Kontur rengi. (B, G, R) formatında bir renk değeri.
    # thickness: Kontur kalınlığı. Negatif bir değer verilirse kontur içini doldurur.
cv.imshow("contours drawn", blank)

cv.waitKey(0)