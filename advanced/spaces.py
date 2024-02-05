import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread("c:/Users/emine/Desktop/OpenCv/advanced/Photos/park.jpg")
cv.imshow("park", img)

#plt rgb renk kullanır bu yüzden bizim fotoğrafımız bgr formatında olduğundan renkler ters olacak
plt.imshow(img)
plt.show()

#Renk uzayları (color spaces), renkleri temsil etmek ve organize etmek için kullanılan matematiksel modellerdir. 
# Bir renk uzayı, bir renk sistemine sahip bir koordinat sistemi gibi düşünülebilir. 
# Farklı renk uzayları, renkleri farklı şekillerde temsil eder ve bu uzaylar, belirli uygulamalara veya görüntü işleme görevlerine daha uygun olabilir.

# BGR to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gary", gray)

#BGR to HSV
    # Renkleri daha doğal bir şekilde tanımlamak için kullanılır. 
    #Renk tonu, rengin kendisi; doygunluk, renk karışımının yoğunluğu; parlaklık, renk şiddetini temsil eder.
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV )
cv.imshow("HSV",hsv)

# BGR to L*a*b
lab= cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow("LAB", lab)

# BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv. imshow("RGB", rgb)

plt.imshow(rgb)
plt.show()

# HSV to BGR
hsv_bgr= cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow("HSV --> BGR", hsv_bgr) 

# bütün renk uzayalrını BGR'a dönüştürebilirsin ancak bu renk uzaylarını birbirine direk döndüremezsin
# grayscale i HSV ye döndürmek için önce grayscale to BGR sonra BGR to HSV yapmalısın.
cv.waitKey(0)