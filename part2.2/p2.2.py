import numpy as np
import cv2

#Kameradan görüntü almak için bir döngüye ihtiyaç vardır. Hem kameradan nasıl görüntü alındığını hem de
#while döngüsünü kullanabileceğimiz bir kod yazalım.

kamera = cv2.VideoCapture(0)

while True:
    ret, goruntu=kamera.read()
    
    cv2.imshow("Live View",goruntu)

    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

kamera.release()

cv2.destroyAllWindows()

"""
KODU OKUYALIM:
kamera = cv2.VideoCapture(0) satırı ile: Videonun nasıl alınacağını belirttik. Ve bunuda kamera isimli değişkene 
atadık.
Daha sonrasında bir video zaten görüntülerden oluştuğu için "while True:" şeklinde bir döngü oluşturduk. Bu döngü 
içerisinde birden fazla görüntü çekilecek.
"if cv2.waitKey(30) & 0xFF == ('q'):" satırında milisaniyeyi 30 olarak belirledik. Böylece video kesik kesik 
olmayacaktır. Mesela 30 yerine 300 gibi daha büyük bir sayı yazsaydık 300 milisaniyede bir görüntü çekilecekti ve 
daha yavaş olucaktır. 
"ret, goruntu=kamera.read()" satırında kamerayı okuyor ve goruntu değişkenine atıyor. ret ile de kameranın çalışıp 
çalışmadığını kontrol ediyor.
Daha sonra da "cv2.imshow("ozengineer",goruntu)" satırı ile görüntüyü bize gösteriyor.
Döngünün içerisinde bulunan 
if cv2.waitKey(30) & 0xFF == ('q'):
        break
koşulu ile 30 milisaniyede bir olacağını belirttik. 30 milisaniye olduysa ve çıkışı belirten 0xFF i kullanıyoruz 
ve 0xFF, q ya eşit ise yani q ya basıldıysa if bloğu çalışır ve break ile çıkış yapılır. Eğer q ya basılmadıysa 
döngü tekrar çalışır yani videoyu devam ettiriyor. Döngünün tekrar çalışma sebebi videoyu devam ettirmesidir.
break ile çıkış yapıldığında kamera.release() satırına gelinir ve bu satır ile kamera serbest bırakılır.
"""