import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype= "uint8")
#Bu ifade, NumPy kütüphanesinin zeros fonksiyonunu kullanarak tüm elemanları sıfır olan bir dizi oluşturur. 
#Bu dizi, üç boyutlu bir yapıdır ve boyutları (500, 500, 3) olarak belirtilmiştir. 
#Bu boyutlar, sırasıyla yükseklik, genişlik ve renk kanallarıdır.

#dtype="uint8": Bu parametre, dizinin elemanlarının veri tipini belirtir. 
#"uint8" (unsigned integer 8-bit) olarak belirlenmiştir, bu da elemanların 0 ile 255 arasında tam sayı değerlerini alabileceği anlamına gelir.
cv.imshow("blank", blank)

#1. paint the image a certain color
blank[200:300, 300:400] = 0,255,0
#Bu ifade, blank görüntüsünün belirli bir bölgesini seçer. 
#Burada, yükseklik (200-300) ve genişlik (300-400) aralığı içindeki bir bölge seçilmiştir.
#= 0, 255, 0: Bu ifade, seçilen bölgeyi belirtilen renk değeriyle doldurur
cv.imshow("green", blank)

#2. Draw a rectangle
cv.rectangle(blank, (0, 0), (blank.shape[1]//2, blank.shape[0]//2), (0,255,0), thickness=cv.FILLED)
#((0, 0), (250, 250)): Bu, çizilecek dikdörtgenin iki köşe noktasını belirtir. 
#İlk köşe (sol üst), ikinci köşe ise (sağ alt) noktasını temsil eder.
#(0, 255, 0): Bu, çizilen dikdörtgenin rengini belirtir. 
#thickness=2: Bu, çizilen dikdörtgenin kenar kalınlığını belirtir.
#dikdörtgenin içini doldurmak istersek thickness=cv.FILLED ifadesini yazmalıyız
# veya = -1 yazarsak da içi doldurulur
#((0, 0), (blank.shape[1]//2, blank.shape[0]//2)): Bu örnekte, sol üst köşesi (0, 0) ve sağ alt köşesi (blank'ın yüksekliğinin yarısı, blank'ın genişliğinin yarısı) olan bir dikdörtgen çizilir.
cv.imshow("rectangle",blank)

#3. Draw A Circle
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0,0,255), thickness=-1)
#((blank.shape[1]//2, blank.shape[0]//2), 40): Bu, çizilecek dairenin merkez noktasını ve yarıçapını belirtir. 
# Merkez noktası, görüntünün genişliğinin yarısı ve yüksekliğinin yarısı olarak belirlenmiştir. 
# Yarıçapı ise 40 pikseldir.
cv.imshow("circle",blank)

#4. Draw A Lime
cv.line(blank, (0,0),(blank.shape[1]//2, blank.shape[0]//2), (255,255,255), thickness=3)
#cv.line(img, pt1, pt2, color, thickness, lineType, shift)
#img: Çizim işleminin uygulanacağı görüntüdür.
#pt1: Çizginin başlangıç noktasıdır (x1, y1).
#pt2: Çizginin bitiş noktasıdır (x2, y2).
#color: Çizgi rengidir. (B, G, R) formatında bir renk tuple'ı veya bir renk kodu olabilir.
#thickness: Çizgi kalınlığıdır. Negatif bir değer verilirse, çizgi içi doldurulur.
#lineType: Çizgi tipidir. Varsayılan olarak 8-connected line kullanılır. cv.LINE_AA kullanılarak antialiasing uygulanabilir.
#shift: Koordinatları kaydırmak için kullanılır. Varsayılan değeri 0'dır.
cv.imshow("line", blank)

#5. Write Text
cv.putText(blank, "hello", (255,255), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0),2)
#cv.putText: Bu OpenCV fonksiyonu, bir görüntü üzerine metin eklemek için kullanılır.
#blank: Metnin eklenme işleminin uygulanacağı görüntüdür.
#"hello": Eklenen metindir.
#(255, 255): Metnin sol üst köşesinin konumunu belirtir. Bu durumda, (255, 255) koordinatlarından başlayacak.
#cv.FONT_HERSHEY_TRIPLEX: Kullanılan yazı tipini belirtir. cv.FONT_HERSHEY_TRIPLEX, üç katmanlı (triple-layer) bir yazı tipidir.
#1.0: Yazı tipinin ölçeğini belirtir. Bu durumda, 1.0 olarak belirlenmiştir.
#(0, 255, 0): Metin rengini belirtir. Yeşil renk için RGB formatında (0, 255, 0) kullanılmıştır.
#2: Metnin kalınlığını belirtir.
cv.imshow("text", blank)

cv.waitKey(0) 