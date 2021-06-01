import cv2
import numpy as np
from pyzbar.pyzbar import decode

capture = cv2.VideoCapture(0)
capture.set(3,500)
capture.set(4,500)

while True:
    success, img = capture.read()
    for bacode in decode(img):
        myData = bacode.data.decode('utf-8')
        print(myData)
        dtc = np.array([bacode.polygon], np.int32)
        dtc = dtc.reshape((-1,1,2))
        cv2.polylines(img,[dtc],True,(0,255,0),6)
    cv2.imshow("Result ", img)
    cv2w.waitKey(1)
