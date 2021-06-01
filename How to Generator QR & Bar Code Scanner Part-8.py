import cv2
from pyzbar.pyzbar import decode
import numpy as np

capture = cv2.VideoCapture(0)
received_data = None
while True:
    success, frame = capture.read()

    decode_data = decode(frame)

    try:
        data = decode_data[0][0]
        if data != received_data:
            print(data)
            received_data = data
    except:
        pass
    cv2.imshow("QR Code Scanner App", frame)
    key = cv2.waitKey(1)

    if key == ord('q'):
        break
