import cv2 as cv

#opencv ile fotoğraf okuma
img = cv.imread("c:/Users/emine/Desktop/OpenCv/basics/Photos/cat.jpg")
# cv.imread("...") ile yazılan dosya yolunun okunmasını sağlar
#okunulan resmi bir NumPy dizisine yükler 
cv.imshow("cat", img)
#Bu satır, cv.imshow fonksiyonunu kullanarak resmi ekranda görüntüler. 
#İlk parametre olan "cat", pencerenin adını temsil eder. 
#İkinci parametre olan img, cv.imread fonksiyonu ile okunan ve belleğe yüklenen resmi temsil eder. 
#Bu fonksiyon, resmi belirtilen ad altında bir pencerede görüntüler.
cv.waitKey(0)
# Bu fonksiyon, bir tuşa basılmasını bekleyerek pencereyi açık tutar.

#opencv ile video okuma
capture = cv.VideoCapture("c:/Users/emine/Desktop/OpenCv/basics/Videos/dog.mp4")
#Bu satır, belirtilen video dosyasını okumak için bir VideoCapture nesnesi oluşturur.

#Bu döngü, video çerçevelerini okumak ve ekranda görüntülemek için kullanılır.
#Döngü sonsuza kadar devam eder.
while True:
    isTrue, frame = capture.read()
    #Bu satır, bir sonraki video çerçevesini capture nesnesinden okur. 
    #isTrue değişkeni, çerçevenin başarılı bir şekilde okunup okunmadığını belirtir. 
    #frame değişkeni ise okunan çerçeveyi temsil eder.
    cv.imshow("video", frame)
     #Bu satır, okunan çerçeveyi "video" adlı bir pencerede görüntüler.

    if cv.waitKey(20)& 0xff==ord("d"):
    #Bu satır, bir tuşa basılmasını bekler.
    #Eğer beklenen tuş "d" ise (ord("d")), döngüyü kırar ve program sonlanır.
        break

capture.release()
cv.destroyAllWindows()

#(-215:Assertion failed) bu error çeşidi opencv nin aradığı şeyi bulamadığını gösteriri
#öğreniğin bir videonun sonuna geldğinde frame bulamaması
#veya bir fotoğrafın yolunun yanlış yazılması gibi