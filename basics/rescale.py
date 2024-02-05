import cv2 as cv

img = cv.imread("c:/Users/emine/Desktop/OpenCv/basics/Photos/cat.jpg")
cv.imshow("Cat", img)

def rescaleFrame(frame, scale=0.75):
    #ımages, videos and live video
    width = int(frame.shape[1]*scale)
    #frame.shape: Bu, çerçevenin boyutlarını (yükseklik, genişlik ve renk kanalları) içeren bir demet (tuple) döndürür.
    #frame.shape[1]: Bu, çerçevenin genişliğini temsil eder (çünkü genişlik, shape demetindeki ikinci öğedir)
    height = int(frame.shape[0]*scale)
    #scale: Çerçevenin genişliğini ölçeklendirme faktörüdür.
    #Örneğin, scale=0.75 olarak belirlenirse, çerçevenin genişliği ve yüksekliği orijinal genişliğin ve yüksekliğin %75'ine çarpılır
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation = cv.INTER_AREA)
#interpolation=cv.INTER_AREA: Bu, çerçevenin yeniden boyutlandırılması sırasında kullanılacak interpolasyon yöntemini belirtir. 
#cv.INTER_AREA, resmi küçültürken veya ölçeklendirirken kullanılan bir interpolasyon yöntemidir ve düşük çözünürlüklerde daha iyi sonuçlar verebilir.

def changeRes(width, height):
    #only works for live video 
    capture.set(3, width)
    capture.set(4, height)

resized_image =rescaleFrame(img)

cv.imshow("image", resized_image)
capture = cv.VideoCapture("c:/Users/emine/Desktop/OpenCv/basics/Videos/dog.mp4")

while True:
    isTrue, frame = capture.read()

    frame_resized= rescaleFrame(frame, scale=.2)

    cv.imshow("video", frame)
    cv.imshow("video resized", frame_resized)
    
    if cv.waitKey(20)& 0xff==ord("d"):
        break

capture.release()
cv.destroyAllWindows()

cv.waitKey(0)