import cv2 as cv
import numpy as np

img = cv.imread("c:/Users/emine/Desktop/OpenCv/advanced/Photos/cats.jpg")
cv.imshow("cats", img)

# Averaging
# 9 parçalı bir kare oluşturup bunun orta noktasını aldı ve bu orta noktadan yola çıkarak bütün kareleri ortalama bir değere getiridi burada işi bitince yana geçti yan bitince aşağı derken bütün resmi dolaştı
average = cv.blur(img,(3,3))
#(3,3) değerini daha büyük bir değerle değiştirirsek daha bulanık bir görüntü elde ederiz
cv.imshow("average blur", average)

# Gaussian Blur
#average a göre daha yumuşak bir blurlama işlemi yaptı
gauss = cv.GaussianBlur(img,(3,3), 0)
cv.imshow("Gaussian Blur", gauss)

# Median Blur
    # average ile neredeyse aynı şeyi yapar yalnızca etrafındaki pixellerin ortalamasını bulmak yerine etrafındaki pixellerin medianını(sıralandığında ortadaki terim) bulur
    # gürültü azaltma konusunda daha etkilidir (diğer ikisine göre de)
median = cv.medianBlur(img, 3)
cv.imshow("median blur", median)

# Bilateral
    #görüntüdeki detayları yumuşatırken aynı zamanda kenarları korumak için kullanılır. 
    #Bilateral blur, diğer blurring yöntemlerinden farklı olarak, hem uzak piksellerin hem de benzer renkli ancak farklı yoğunluktaki piksellerin dikkate alınmasını sağlar.
bileteral= cv.bilateralFilter(img, 5, 15, 15 )
#cv2.bilateralFilter(img, d=5, sigmaColor=15, sigmaSpace=15)
    # img: Giriş görüntüdür.
    # d: Renk benzerliği ifadesidir. Bu, etrafındaki piksellerin renk benzerliğini belirler.
    # sigmaColor: Renk benzerliği için kullanılan standart sapma değeridir.
    # sigmaSpace: Uzaklık ifadesidir. Bu, etrafındaki piksellerin uzaklığını belirler.
cv.imshow("bilateral", bileteral)

cv.waitKey(0)