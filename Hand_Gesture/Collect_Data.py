import os
import cv2

DATA_DIR = '../hand_gesture_samplae/data'

if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

no_of_gesture_class = 9
data_size= 300

cap = cv2.VideoCapture(0)

for i in range(no_of_gesture_class):
    if not os.path.exists(os.path.join(DATA_DIR, str(i))):
        os.makedirs(os.path.join(DATA_DIR, str(i)))

    print('Collecting the data from {}'.format(i))

    done = False
    while True:
        _, frame = cap.read()
        cv2.putText(frame, "AI Ready. Upload Your Gesture with 'h'",(120, 220), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0,255,0), 1 , cv2.LINE_AA)
        cv2.imshow('Gesture Frame', frame)
        if cv2.waitKey(30) & 0xff == ord('h'):
            break


    count = 0
    while count < data_size:
        _, frame = cap.read()
        cv2.imshow('Gesture Frame', frame)
        cv2.waitKey(30)
        cv2.imwrite(os.path.join(DATA_DIR, str(i), '{}.jpg'.format(count)), frame)
        count +=1

cap.release()
cv2.destroyWindow()