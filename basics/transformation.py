import cv2 as cv
import numpy as np

img = cv.imread("c:/Users/emine/Desktop/OpenCv/basics/Photos/park.jpg")
cv.imshow("park", img)

# Translation

#Bu fonksiyon, bir görüntüyü belirli bir miktar (x, y) kadar translasyon yaparak kaydırmak için kullanılır.
def translate(img, x,y):
    transMat= np.float32([[1,0,x],[0,1,y]])
    dimension = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat,dimension )
    #Fonksiyon, cv2.warpAffine fonksiyonunu kullanarak bir affin dönüşüm matrisi oluşturur ve bu matrisi kullanarak görüntüyü kaydırı
# Affin dönüşümler, kayma (translasyon), ölçekleme (scale), döndürme (rotation), ve yansıma (shear) gibi temel geometrik dönüşümleri içeren lineer dönüşüm matrisleri kullanarak gerçekleştirilen dönüşümlerdir.
#cv2.warpAffine(src, M, dsize[, dst[, flags[, borderMode[, borderValue]]]])
#src: Giriş görüntüsü.
#M: 2x3 boyutunda affin dönüşüm matrisi.
#dsize: Çıkış görüntüsünün boyutu (genişlik ve yükseklik).
#dst: Opsiyonel olarak, çıkış görüntüsü için ayrılan bellek alanı
#flags: İnterpolasyon yöntemini belirten bayraklar. Örneğin, cv2.INTER_LINEAR
#borderMode: Kenar pikselleri için kullanılacak piksel sınırlama modu
#borderValue: Eğer kenar sınırlama modu cv2.BORDER_CONSTANT olarak ayarlandıysa, kenar pikselleri için kullanılacak sabit bir değer.

# -x ---> Left
# -y ---> Up
#  x ---> Right
#  y ---> Down

translated = translate(img,100,100)
cv.imshow("translated", translated)

# Rotation

#Bu Python fonksiyonu, bir görüntüyü belirli bir açıda döndürmek için OpenCV'nin dönüşüm fonksiyonlarını kullanır.
    #img: Döndürülecek olan giriş görüntüsü.
    #angle: Döndürme açısı (derece cinsinden).
    #rotPoint: Döndürme merkezi. Eğer belirtilmezse, görüntünün merkezi varsayılır.
def rotate(img, angle, rotPoint=None):
    (height, width)= img.shape[:2]
    #(height, width) = img.shape[:2]: Giriş görüntüsünün yüksekliği ve genişliğini height ve width değişkenlerine atar. img.shape ifadesi, görüntünün boyutunu sağlayan bir NumPy dizisidir

    if rotPoint is None:
        rotPoint =(width//2,height//2)
        #varsayılan olarak döndürme merkezi görüntünün ortasıdır.

    rotMat = cv.getRotationMatrix2D(rotPoint,angle, 1.0)  
    # Belirtilen döndürme merkezi (rotPoint), açı (angle), ve ölçek faktörü (1.0) kullanılarak bir döndürme matrisi (rotMat) oluşturur. Bu matris, görüntüyü belirli bir açıda döndürmek için kullanılacaktır 
    dimension= (width,height)
    #Yeni boyutları belirlemek için görüntünün genişliği ve yüksekliğini içeren bir tuple oluşturur. 
        #Bu tuple, cv2.warpAffine fonksiyonuna verilecek olan çıkış görüntüsünün boyutunu belirlemek için kullanılır.
    
    return cv.warpAffine(img, rotMat, dimension)

rotated = rotate(img, -45)
cv.imshow("rotated", rotated)    

rotated_rotated = rotate(rotated, -45)
cv.imshow("rotated rotated", rotated_rotated)  
#döndürülmüş görüntü tekrar döndürülürse bu durmda ilk döndürme halinde oluşmuş olan görüntü döndürüldüğünden kenarlarında siyahlık olacak şekilde bir dönüş sergiler. 
#Bu durum görüntünün orjinalliğini bozar  

# Resizing
#bir görüntüyü belirli boyutlara yeniden boyutlandırmak için kullanıldı.
resize = cv.resize(img,(500,500), interpolation=cv.INTER_CUBIC)
cv.imshow("resized",resize)

# Flipping
flip= cv.flip(img,0)
#cv.flip(src, flipCode[, dst])
#src: Çevrilecek olan giriş görüntüsü.
#flipCode: Çevirme işleminin yapılacağı ekseni belirten bir kod. 
    #Bu, 0 (yatay eksende çevirme), 1 (dikey eksende çevirme) veya -1 (her iki eksende çevirme) değerlerini alabilir.
#dst: Opsiyonel olarak, çıkış görüntüsü için ayrılan bellek alanı.
cv.imshow("flip",flip)

# Cropping
# bir görüntüyü belirli bir bölgeye (200-400 yükseklik aralığı, 300-400 genişlik aralığı) kırpma (crop) işlemi yapmak için kullanılır.
cropped= img[200:400,300:400]
# Kırpılacak bölgenin koordinatlarını belirtir. Bu, yükseklik (200-400) ve genişlik (300-400) aralıklarını ifade eder.
cv.imshow("cropped",cropped)


cv.waitKey(0) 