import numpy as np
import cv2
import mediapipe as mp
import pickle

mode_dict = pickle.load(open('../hand_gesture_samplae/model.p', 'rb'))
model = mode_dict['model']

cap = cv2.VideoCapture(0)

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

hands = mp_hands.Hands(static_image_mode=True, model_complexity=1, min_detection_confidence=0.3, min_tracking_confidence=0.3)

labels_dir = {0:'No', 1:'Yes', 2:'Thank you', 3:'Greetings', 4:'Hello', 5:'Love', 6:'OK', 7:'Peace', 8:'Super'}
padding = 30

while True:
    temp_data = []
    x_ = []
    y_ = []

    _, frame = cap.read()
    if not _:
        break
    h, w, _ = frame.shape

    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(frame_rgb)

    if result.multi_hand_landmarks:
        for hand_landmark in result.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmark, mp_hands.HAND_CONNECTIONS)


            for i in range(len(hand_landmark.landmark)):
               x = hand_landmark.landmark[i].x
               y = hand_landmark.landmark[i].y

               x_.append(x)
               y_.append(y)

            for i in range(len(hand_landmark.landmark)):
                x = hand_landmark.landmark[i].x
                y = hand_landmark.landmark[i].y

                temp_data.append(x - min(x_))
                temp_data.append(y - min(y_))


        x1 =  max(0, int(min(x_) * w) - padding)
        y1 =  max(0, int(min(y_) * h) - padding)

        x2 = min(w, int(max(x_) * w) + padding)
        y2 = min(h, int(max(y_) * h) + padding)

        if len(temp_data) == 42:
            prediction = model.predict([np.asarray(temp_data)])
            predicted_char = labels_dir[int(prediction[0])]

            cv2.rectangle(frame, (x1, y1), (x2, y2), (51, 255, 51), 3 )
            cv2.putText(frame, predicted_char, (x1, y1 -10), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 0, 0), 2, cv2.LINE_AA)
            # cv2.putText(frame, predicted_char, (20, 40) , cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 0, 0), 2, cv2.LINE_AA)


    cv2.imshow('Sign Language', frame)

    if cv2.waitKey(1) & 0xff == ord('h'):
        break


cap.release()
cv2.destroyWindow()

