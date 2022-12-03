import cv2 
import numpy as np

img = cv2.imread("p.png")

kernelx = np.array([[1,1,1],[0,0,0],[-1,-1,-1]])
kernely = np.array([[-1,0,1],[-1,0,1],[-1,0,1]])
img_prewittx = cv2.filter2D(img, -1, kernelx)
img_prewitty = cv2.filter2D(img, -1, kernely)

cv2.imshow("img_prewittx",img_prewittx)
cv2.imshow("img_prewitty",img_prewitty)

cv2.waitKey(0)
cv2.destroyAllWindows()