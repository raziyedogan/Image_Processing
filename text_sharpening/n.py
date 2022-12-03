import cv2
import numpy as np

image = cv2.imread("yz.jpg")

kernel = np.ones((3,3),np.uint8)

dilation = cv2.dilate(image,kernel,iterations=1)
 
cv2.imshow("Orijinal resim",image)
cv2.imshow("Dilation",dilation)

cv2.waitKey(0)
cv2.destroyAllWindows()