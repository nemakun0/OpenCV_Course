import cv2 as cv

img = cv.imread("c:/Users/emine/Desktop/OpenCv/faces/Photos/group 1.jpg")
cv.imshow("group of people", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray person" ,gray)

haar_cascade = cv.CascadeClassifier("c:/Users/emine/Desktop/OpenCv/faces/haar_face.xml")
faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=1)
    # gray: Gri tonlamalı görüntü.
    # scaleFactor: Nesnelerin tespit edilmesi için kullanılan ölçek faktörü. 
        # Her ölçekte (scale) görüntü boyutunu küçültmek veya büyütmek için kullanılır. 
        # Örneğin, 1.1 ölçek faktörü, her seferinde görüntü boyutunu %10 oranında artırır. 
        # Bu, nesnelerin farklı boyutlarda olabileceği durumlar için kullanışlıdır.
    # minNeighbors: Bir nesnenin tespit edilmesi için gereken komşu dikdörtgen sayısı. 
        # Bu değer ne kadar küçükse, algılanan nesnelerin sayısı o kadar fazla olacaktır. 
        # Ancak, daha yüksek bir değer, algılamalar arasında daha fazla "düzensiz" nesnenin reddedilmesine neden olabilir.

print(f"number of faces found = {len(faces_rect )}")

for(x,y,w,h) in faces_rect:
    cv.rectangle(img, (x,y), (x+w, y+h), (0,255,0), thickness= 2)

cv.imshow("detected faces", img)

cv.waitKey(0)

# Haar Cascade, nesne tanıma (object detection) amacıyla kullanılan bir özellik tabanlı sınıflandırma yöntemidir. 
# Bu yöntem, özellikle yüz tespiti gibi görevlerde yaygın olarak kullanılmaktadır. 
# Haar Cascade, öğrenilmiş özelliklere dayalı olarak nesneleri tespit etmek için bir makine öğrenimi yaklaşımıdır.
    # Negatif ve Pozitif Örneklerin Hazırlanması: Eğitim için negatif (nesne içermeyen) ve pozitif (nesneyi içeren) örneklerin hazırlanması gerekir.
    # Haar Özelliklerinin Hesaplanması: Belirli bir boyutta pencere üzerinde farklı konum ve büyüklüklerde Haar benzeri özelliklerin hesaplanması.
    # Öğrenme (Training) Aşaması: Pozitif ve negatif örneklerle eğitim yapılması. AdaBoost algoritması kullanılarak zayıf sınıflandırıcıların birleştirilmesi.
    # Cascade Yapısının Oluşturulması: Zayıf sınıflandırıcıların oluşturduğu güçlü sınıflandırıcılar zinciri. Bu yapı, sırasıyla daha fazla hesaplama yapılmasına izin verir ve yanlış pozitif oranını düşürmeye yardımcı olur.
    # Nesne Tespiti: Cascade yapısı kullanılarak nesne tespiti.