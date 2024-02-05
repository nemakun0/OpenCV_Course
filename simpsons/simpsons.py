#pylint:disable=no-member (Removes linting problems with cv)

# Installing `caer` and `canaro` since they don't come pre-installed
# Uncomment the following line:
# !pip install --upgrade caer canaro

import os
import caer
import canaro
import numpy as np
import cv2 as cv
import gc
import matplotlib.pyplot as plt
from keras.utils import to_categorical
from keras.callbacks import LearningRateScheduler
from sklearn.model_selection import train_test_split


IMG_SIZE = (80,80)
channels = 1
char_path = r'C:\Users\emine\Desktop\OpenCv\simpsons\archive\simpsons_dataset'

# Creating a character dictionary, sorting it in descending order
char_dict = {}
for char in os.listdir(char_path):
#os modülü kullanılarak karakter dizinindeki karakterleri listeleyen bir döngü başlatılır.
    char_dict[char] = len(os.listdir(os.path.join(char_path,char)))
    # Her karakterin alt dizinindeki dosya sayısını alıp sözlüğe ekler
    # os.path.join(char_path, char): Bu ifade, char_path (karakterlerin bulunduğu ana dizin) ve char (karakter adı) değerlerini birleştirerek, karakterin alt dizininin tam yolunu oluşturur. 
    # Örneğin, 'C:\Users\emine\Desktop\OpenCv\simpsons\archive\simpsons_dataset\Bart'.
    # os.listdir: belirtilen karakterin alt dizinindeki dosya ve dizinleri listeleyerek, bu karakterin dosya sayısını elde eder.

# Sort in descending order
char_dict = caer.sort_dict(char_dict, descending=True)
#char_dict sözlüğü, karakter adlarını anahtar olarak ve dosya sayılarını değer olarak içermeye devam eder, ancak bu sefer dosya sayılarına göre büyükten küçüğe sıralanmış olacaktır.


#  Getting the first 10 categories with the most number of images
characters = []
count = 0
for i in char_dict:
    characters.append(i[0])
    # burada i[0] yazmamızın sebebi sadece isimlerini almak istememiz.
    # yalnızca i yazsaydık bu durumda hem isimlerini hemde dosya sayısını almış olacaktı.
    count += 1
    if count >= 10:
        break

# Create the training data
# caer modülünün preprocess_from_dir fonksiyonunu kullanarak eğitim verilerini oluşturur.
train = caer.preprocess_from_dir(char_path, characters, channels=channels, IMG_SIZE=IMG_SIZE, isShuffle=True)
    # char_path: Eğitim verilerinin bulunduğu dizin.
    # characters: Eğitimde kullanılacak karakterlerin isimlerini içeren liste.
    # channels: Görüntülerin kaç renkli kanala sahip olduğunu belirten değişken.
    # IMG_SIZE: Görüntülerin boyutlarını belirten değişken.
    # isShuffle=True: Eğitim verilerinin karıştırılması için kullanılan bir parametre.

# Number of training samples
#print(len(train))

# Visualizing the data (OpenCV doesn't display well in Jupyter notebooks)
plt.figure(figsize=(30,30))
#bir matplotlib figürü oluşturur ve bu figürün boyutunu belirler. Burada (30,30) değeri, genişlik ve yükseklik boyutlarını belirtir.
plt.imshow(train[0][0], cmap='gray')
#imshow fonksiyonu kullanılarak bir görüntüyü ekrana çizdirilir.
plt.show()

# Separating the array and corresponding labels
    #caer modülündeki sep_train fonksiyonunu kullanarak eğitim verilerini ve etiketlerini ayırır.
featureSet, labels = caer.sep_train(train, IMG_SIZE=IMG_SIZE)
    #featureSet: Bu değişken, eğitim verilerini temsil eden bir yapıdır. Genellikle bu, görüntülerin piksel değerlerini içeren bir NumPy dizisi olacaktır.


# Normalize the featureSet ==> (0,1)
featureSet = caer.normalize(featureSet)
#caer.normalize: Bu fonksiyon, görüntü piksel değerlerini belirli bir aralığa normalleştirir

# Converting numerical labels to binary class vectors
labels = to_categorical(labels, len(characters))
#to_categorical: Bu fonksiyon, sayısal etiketleri ikili (binary) sınıf vektörlerine dönüştürür. 


# Creating train and validation data
#Bu kod satırı, caer modülündeki train_test_split fonksiyonunu kullanarak veri setini eğitim ve doğrulama (validation) setlerine ayırır. 
x_train, x_val, y_train, y_val = train_test_split(featureSet, labels, test_size=.2)
    # featureSet: Bu, önceki adımlarda oluşturulan ve özellik setini temsil eden veri yapısıdır. Genellikle, eğitim verilerinin normalleştirilmiş görüntü piksellerini içerir.
    # labels: Bu, önceki adımlarda oluşturulan ve etiketleri temsil eden veri yapısıdır. Genellikle, eğitim verilerine karşılık gelen sınıf etiketlerini içerir.
    # val_ratio=.2: Bu, veri setinin ne kadarının doğrulama seti olarak ayrılacağını belirten bir orandır. Burada %20 oranında doğrulama seti ayrılmıştır (val_ratio=0.2).

    # x_train: Eğitim verilerinin özellik seti.
    # x_val: Doğrulama verilerinin özellik seti.
    # y_train: Eğitim verilerine karşılık gelen etiketler.
    # y_val: Doğrulama verilerine karşılık gelen etiketler.
#Bu ayrım, modelin eğitimi sırasında kullanılmak üzere eğitim ve doğrulama setlerini oluşturur. 
    #Bu setler, modelin genelleme yeteneğini değerlendirmek ve aşırı uydurma (overfitting) durumlarını kontrol etmek için kullanılır.

# Deleting variables to save memory
del train #train değişkenini siler
del featureSet #featureSet değişkenini siler.
del labels #labels değişkenini siler. 
gc.collect() #garbage collector çağırır.

# Useful variables when training
BATCH_SIZE = 32
# batch size : her eğitim iterasyonunda kullanılacak örnek sayısını belirtir. Model ağırlıklarının güncellenmesi için kullanılır.
EPOCHS = 10

# Image data generator (introduces randomness in network ==> better accuracy)
datagen = canaro.generators.imageDataGenerator()
# görüntü verileri üzerinde çeşitli dönüşümler yaparak modelin daha genel bir şekilde öğrenmesine yardımcı olabilir
train_gen = datagen.flow(x_train, y_train, batch_size=BATCH_SIZE)

decay=1e-7
# Create our model (returns the compiled model)
model = canaro.models.createSimpsonsModel(IMG_SIZE=IMG_SIZE, channels=channels, output_dim=len(characters), 
                                         loss='binary_crossentropy', decay=1e-7, learning_rate=0.001, momentum=0.9,
                                         nesterov=True) 
    # output_dim=len(characters): Bu, modelin çıkış katmanının boyutunu belirten bir parametredir. len(characters), toplam karakter sayısını ifade eder. Modelin sınıflandırma yapması gereken sınıf sayısını belirtir.
    # loss='binary_crossentropy': Bu, modelin kullanacağı kayıp fonksiyonunu belirten bir parametredir. 'binary_crossentropy', ikili sınıflandırma problemleri için yaygın olarak kullanılan bir kayıp fonksiyonudur.
    # decay=1e-7: Bu, öğrenme hızının zamanla azalmasını kontrol eden bir parametredir. Bu, modelin daha düzgün bir şekilde öğrenmesine yardımcı olabilir.
    # learning_rate=0.001: Bu, öğrenme hızını belirten bir parametredir. Modelin öğrenme hızı, ağırlıkların güncellenme hızını kontrol eder.
    # momentum=0.9: Bu, momentum optimizasyon algoritmasının bir parametresidir. Momentum, ağırlıkların güncellenmesini hızlandırmak için kullanılır.
    # nesterov=True: Bu, Nesterov momentum'un kullanılıp kullanılmayacağını belirten bir parametredir. Nesterov momentum, momentum optimizasyon algoritmasının bir iyileştirmesidir.
#Bu satır, belirtilen parametrelerle özelleştirilmiş bir Sinir Ağı modeli oluşturur. Bu model, daha sonra eğitim verileri üzerinde eğitilecek ve sınıflandırma görevini yerine getirecektir.

model.summary()

# Training the model

callbacks_list = [LearningRateScheduler(canaro.lr_schedule)]
#LearningRateScheduler(canaro.lr_schedule) Fonksiyonu:
    # LearningRateScheduler, öğrenme oranını programlı bir şekilde değiştirmek için kullanılan bir Keras geri çağrısıdır. Bu geri çağrı, her epoch sonunda belirli bir öğrenme oranını uygulayan bir öğrenme oranı programı sağlar.
    # canaro.lr_schedule ise, öğrenme oranı programını sağlayan bir fonksiyondur. Bu fonksiyon genellikle öğrenme oranını her epoch'ta küçülten bir strateji uygular.

training = model.fit(train_gen,
                    steps_per_epoch=len(x_train)//BATCH_SIZE,
                    epochs=EPOCHS,
                    validation_data=(x_val,y_val),
                    validation_steps=len(y_val)//BATCH_SIZE,
                    callbacks = callbacks_list)
#model.fit Fonksiyonu:
    # train_gen: Eğitim verilerini üretecek olan veri jeneratörüdür. Veri jeneratörleri genellikle büyük veri setlerini eğitmek için kullanılır ve veri akışını sağlar.
    # steps_per_epoch: Her bir epoch (eğitim iterasyonu) için adım sayısını belirtir. Bu, bir epoch'un kaç adımdan oluşacağını belirler.
    # epochs: Toplam eğitim epoch sayısını belirtir. Bir epoch, modelin tamamıyla eğitildiği bir geçişidir.
    # validation_data: Doğrulama veri setini temsil eden bir demettir. Modelin eğitim sırasında doğrulama performansını değerlendirmek için kullanılır.
    # validation_steps: Her bir epoch için doğrulama adım sayısını belirtir.
    # callbacks: Eğitim sırasında çağrılacak geri çağrıları içeren bir liste. Geri çağrılar, eğitim sırasında belirli noktalarda özel işlemleri gerçekleştirmenizi sağlar.


print(characters)


"""## Testing"""

test_path = r'../input/the-simpsons-characters-dataset/kaggle_simpson_testset/kaggle_simpson_testset/charles_montgomery_burns_0.jpg'

img = cv.imread(test_path)

plt.imshow(img)
plt.show()

def prepare(image):
    image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    image = cv.resize(image, IMG_SIZE)
    image = caer.reshape(image, IMG_SIZE, 1)
    return image

predictions = model.predict(prepare(img))

# Getting class with the highest probability
print(characters[np.argmax(predictions[0])])