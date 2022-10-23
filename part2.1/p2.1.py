import numpy as np	
import cv2 

#numpy'ın array, zeros ve ones fonksiyonları:
A = np.array([[1,2,3],[3,4,5]])
print("A matrix:\n",A)

array =np.zeros( (2,3) )
print("zeros matrix:\n",array)

array2 =np.ones( (1,5) )
print("ones matrix:\n",array2)

#python if kullanımı:
image1 = cv2.imread("bugs_bunny.png")
image2 = cv2.imread("Daffy_Duck.png")
image3 = cv2.imread("tazmanya-canavari.jpg")

print("1: bugs bunny")
print("2: Daffy Duck")
print("3: Looney Tunes")
open = input("Kac numarali resmi goruntulemek istersiniz?: ")

if int(open)==1:
    cv2.imshow("Bugs Bunny",image1)
elif int(open)==2:
    cv2.imshow("Duffy Duck",image2)
elif int(open)==3:
    cv2.imshow("Looney Tunes",image3)
else:
    print("Gecerli bir numara giriniz.")

cv2.waitKey(0)
cv2.destroyAllWindows()