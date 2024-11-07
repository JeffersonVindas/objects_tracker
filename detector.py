import cv2
from tracker import *

following = Tracker()

cap = cv2.VideoCapture("resources/Street.mp4")

detection = cv2.createBackgroundSubtractorMOG2(history= 10000, varThreshold= 12)

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame,(1280,720))

    zone = frame[220:1076, 200:1910]

    mask = detection.apply(zone)
    _, mask = cv2.threshold(mask, 254, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    detections = []

    for count in contours:
        area = cv2.contourArea(count)
        if area > 800:
            x, y, width, height = cv2.boundingRect(count)
            cv2.rectangle(zone, (x, y), (x + width, y + height), (255, 255, 0), 3)
            detections.append([x, y, width, height])

    info_id = following.Tracking(detections)
    for inf in info_id:
        x, y, width, height, id = inf
        cv2.putText(zone, str(id), (x, y -15), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255),2)
        cv2.rectangle(zone, (x, y), (x+ width, y + height), (255, 255, 0), 3)

    print(info_id)
    #cv2.imshow("Zona de Interes", zone)
    cv2.imshow("Carretera", frame)
    cv2.imshow("Mascara", mask)

    key = cv2.waitKey(5)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()