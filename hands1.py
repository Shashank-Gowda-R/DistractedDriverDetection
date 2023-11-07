import cv2 as cv
from cvzone import HandTrackingModule

video = cv.VideoCapture(0)
detector = HandTrackingModule.HandDetector()

prev_num_hands = -1
count = 0

while True:
    isTrue, frame = video.read()
    hands, img = detector.findHands(frame)
    
    num_hands = len(hands)
    if count == 0 and num_hands == 2:
        cv.putText(frame, "Engine is started you can drive. Happy Journey", (50, 50), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv.LINE_AA)
        count += 1
    if count == 0:
        cv.putText(frame, "Place your hands on the steering to start the engine", (50, 50), cv.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 2, cv.LINE_AA)

    if count > 0:
        # if num_hands != prev_num_hands:
        #     prev_num_hands = num_hands  
        
            if num_hands == 2:
                cv.putText(frame, "You can drive at the max speed", (50, 50), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv.LINE_AA)
            elif num_hands == 1:
                cv.putText(frame, "You can drive at max speed of 25Km/h", (50, 50), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv.LINE_AA)
            elif num_hands == 0:
                cv.putText(frame, "Brakes are being applied", (50, 50), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv.LINE_AA)
    
    cv.imshow("Hands Detected", frame)
    
    key = cv.waitKey(10)
    if key & 0xFF == ord("d"):
        break

video.release()
cv.destroyAllWindows()