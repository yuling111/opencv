from modifyHTModule import HandDetector
import cv2

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)
detector = HandDetector(detectionCon=0.5, maxHands=2)

while True:
    # Get image frame
    success, img = cap.read()

    # Find the hand and its landmarks
    img = detector.findHands(img)
    lmList, bboxInfo = detector.findPosition(img)
    if lmList:
        bbox = bboxInfo['bbox']
        # Find how many fingers are up
        fingers = detector.fingersUp()
        print(fingers)
        totalFingers = fingers.count(1)
        if totalFingers == 0:
            cv2.putText(img,'Stone',(bbox[0] + 200, bbox[1] - 30),cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)
        elif totalFingers ==5:
            cv2.putText(img,'Paper',(bbox[0] + 200, bbox[1] - 30),cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)
        elif fingers[1] == fingers[2] == 1:
            cv2.putText(img,'Scissors',(bbox[0] + 200, bbox[1] - 30),cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)
       

    # Display
    cv2.imshow("Image", img)
    k=cv2.waitKey(1)
    if k==27:
        break
cv2.destroyAllWindows()