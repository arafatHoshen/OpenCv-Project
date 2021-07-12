import cv2
cap = cv2.VideoCapture(0)

tracker = cv2.TrackerCSRT_create()
success, img = cap.read()
bbox = cv2.selectROI("Tracker fps", img, False)
tracker.init(img,bbox)

def drawbox(img, bbox):
    x,y,w,h = int(bbox[0]), int(bbox[1]), int(bbox[2]), int(bbox[3])
    cv2.rectangle(img, (x,y), ((x+w),(y+h)), (225,0,225),3,1)
    cv2.putText(img, "Tracker", (75,50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,225),2)

while True:
    time = cv2.getTickCount()
    success, img = cap.read()

    success, bbox = tracker.update(img)
    print(bbox)
    if success:
        drawbox(img,bbox)

    fps = cv2.getTickFrequency() / (cv2.getTickCount() - time);
    cv2.putText(img, str(int(fps)), (75,75), cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,255,255),2)
    cv2.imshow("Tracking img", img)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break