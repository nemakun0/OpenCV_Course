import cv2 as cv

img = cv.imread("c:/Users/emine/Desktop/OpenCv/basics/Photos/park.jpg")
cv.imshow("park", img)

# Converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.cvtColor fonksiyonu, görüntü rengini bir renk uzayından başka bir renk uzayına dönüştürmek için kullanılır. 
#Gri tonlamalı görüntüye dönüştürme, genellikle birçok görüntü işleme uygulamasında kullanılır çünkü gri tonlamalı görüntüler sadece tek bir renk kanalını içerir, bu da işlemleri daha basitleştirir ve bazı durumlarda daha hızlı işlem yapmayı sağlar.
cv.imshow("Gray", gray)

# Blur
blur = cv.GaussianBlur(img, (3,3), cv.BORDER_DEFAULT)
#blur = cv.GaussianBlur(img, (kernel_size, kernel_size), sigmaX)
#img: Bulanıklaştırılacak olan görüntüdür.
#(kernel_size, kernel_size): Gaussian çekirdeğinin boyutunu belirtir. Bu, genellikle tek sayı olmalıdır. Çekirdek boyutu arttıkça, bulanıklık miktarı da artar.
#sigmaX: X yönde standart sapmayı belirtir. Eğer 0 olarak belirlenirse, sigmaX otomatik olarak kernel boyutuna bağlı olarak hesaplanır.
cv.imshow("blur", blur)

# Edge Cascade
    # Kenar tespiti, bir görüntüdeki nesne sınırlarını veya özellikleri vurgulamayı amaçlayan bir görüntü işleme yöntemidir. 
    #Bu tür algoritmalar, görüntüdeki yoğunluk değişikliklerini tespit eder ve bu değişikliklerin olduğu yerleri belirler.
canny= cv.Canny(img,125,175)
#img: Kenar tespiti yapılacak olan giriş görüntüdür.
#125: Kenarlar için alt eşik değeridir. Bu değer, kenar pikselleri için bir eşik değeridir. 
    #Bu değerden düşük olan gradyan değerlerine sahip pikseller kenar olarak kabul edilmez.
#175: Kenarlar için üst eşik değeridir. Bu değer, kenar pikselleri için bir eşik değeridir. 
    #Bu değerden yüksek olan gradyan değerlerine sahip pikseller kesinlikle kenar olarak kabul edilir.
cv.imshow("canny edges", canny)

# Dilating the image
    #Dilatasyon, bir görüntü üzerindeki nesneleri genişletir ve kenarları kalınlaştırır.
dilated= cv.dilate(canny, (3,3), iterations=1)
#cv.dilate fonksiyonu, dilatasyon işlemi için kullanılır. 
    #İşlemin temel amacı, her bir pikselin etrafına bir yapısal öğe (kernel veya çekirdek) yerleştirerek, bu yapısal öğenin altındaki piksellerin maksimum değerini alarak görüntüyü genişletmektir
#dilated_img = cv.dilate(img, kernel, iterations)
    #(3, 3): Dilatasyon işlemi için kullanılacak olan 3x3 boyutundaki kare şeklinde bir yapısal öğedir (kernel). Bu, her bir pikselin etrafında 3x3'lük bir alanı ele alacak demektir.
    #iterations: Dilatasyon işleminin kaç kez uygulanacağını belirtir. İterasyon sayısı arttıkça, genişletme miktarı da artar.
cv.imshow("dilated",dilated)

#Eroding
    #Erozyon (erosion), morfolojik bir işlem olup, görüntüdeki nesnelerin boyutunu küçültmeyi veya kenarlarını aşındırmayı amaçlar. 
    #Genellikle görüntüdeki küçük gürültüleri veya kenarları temizlemek, nesneleri ayırmak veya şekilleri daha düzenli hale getirmek için kullanılır. 
    #Erozyon işlemi, kenarlardaki pikselleri kaldırarak veya azaltarak nesneleri küçültür.  
eroded= cv.erode(dilated, (3,3), iterations= 1)
#cv.erode :İşlemin temel amacı, her bir pikselin etrafına bir yapısal öğe (kernel veya çekirdek) yerleştirerek, bu yapısal öğenin altındaki piksellerin minimum değerini alarak görüntüyü erozyona uğratmaktır.
#eroded_img = cv.erode(img, kernel, iterations)
cv.imshow("eroded", eroded)

# Resize
resized= cv.resize(img, (500,500),interpolation= cv.INTER_CUBIC)
#(500, 500): Yeni boyutları belirtir.
#interpolation=cv2.INTER_CUBIC: Yeniden boyutlandırma işlemi sırasında kullanılacak interpolasyon yöntemini belirtir. 
    #cv2.INTER_CUBIC, kübik interpolasyonu kullanır ve genellikle daha pürüzsüz sonuçlar elde etmek için tercih edilir.
cv.imshow("resized", resized)

# Cropping
    #Bu satır, bir görüntü üzerinde belli bir bölgeyi kesip çıkarmak için kullanılır
cropped = img[50:200, 200:400]
#[50:200, 200:400]: Kesilecek bölgenin koordinatlarını belirtir. 
    #Bu, yükseklik (50-200) ve genişlik (200-400) aralıklarını ifade eder.
cv.imshow("cropped", cropped)

cv.waitKey(0)