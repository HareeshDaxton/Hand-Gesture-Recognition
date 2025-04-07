import os
import mediapipe as mp
import pickle
import cv2


mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils
mp_drawing_style = mp.solutions.drawing_styles

hands = mp_hands.Hands(static_image_mode=True, min_detection_confidence=0.4)

DATA_DIR = '../hand_gesture_samplae/data'

data = []
labels = []

for dir_ in os.listdir(DATA_DIR):
    for image_path in os.listdir(os.path.join(DATA_DIR, dir_)):
        temp_data = []
        x_ = []
        y_ = []

        img = cv2.imread(os.path.join(DATA_DIR, dir_, image_path))
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        result = hands.process(img_rgb)

        if result.multi_hand_landmarks:
            for hand_landmark in result.multi_hand_landmarks:
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

            data.append(temp_data)
            labels.append(dir_)

file = open('../hand_gesture_samplae/data.pickle', 'wb')
pickle.dump({'data': data, 'labels': labels}, file)
file.close()