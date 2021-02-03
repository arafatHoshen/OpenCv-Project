#############  how to convert RGB image gaussain & Blur image   ###########
import cv2
img = cv2.imread("image/arafat.jpeg")
ImgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


ImgBlur = cv2.GaussianBlur(ImgGray,(99,99),0)

cv2.imshow("Gray Image", ImgGray)

cv2.imshow("Blur Image", ImgBlur)



cv2.waitKey(0)
