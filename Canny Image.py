import cv2
import numpy as np
img = cv2.imread("Mas.jpg")
kernel = np.ones((5, 5))
CannyImg = cv2.Canny(img, 50, 200)
ImgDialation = cv2.dilate(CannyImg, kernel, iterations=1)

cv2.imshow("Original img", img)
cv2.imshow("Canny Img", CannyImg)
cv2.imshow("Dialation img", CannyImg)
cv2.waitKey(0)

