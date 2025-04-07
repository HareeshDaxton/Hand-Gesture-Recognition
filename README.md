# Hand Gesture Recognition - Sign Language Detection

A real-time **Hand Gesture Recognition System** for detecting and classifying **Sign Language gestures** using computer vision (OpenCV), **MediaPipe** hand landmarks, and a **Machine Learning model (Random Forest)**.

This project allows you to collect gesture images, process and extract hand landmark data, train a model, and run real-time sign language detection using your webcam.

---

## 📚 Features
- Real-time gesture recognition using webcam
- Single and dual hand detection
- 9 gesture classes (e.g., Yes, No, Thank you, Love, OK, Peace)
- MediaPipe Hands for robust landmark detection
- Trained using RandomForestClassifier for high accuracy
- Modular code structure (easy to modify or extend)

---

## 🗂️ Project Structure
```bash
Hand_Gesture/
│
├── Collection_Data.py     # Script to collect gesture images using webcam
├── Creat_data.py          # Extract hand landmarks from collected images
├── ML_model.py            # Train ML model using extracted data
├── main.py                # Real-time hand gesture recognition script
├── data/                  # Contains gesture images organized by class
├── data.pickle            # Processed data (features + labels)
├── model.p                # Trained Random Forest model
```

---

## ⚡ Installation
```bash
pip install opencv-python mediapipe scikit-learn numpy
```

---

## 🔧 How to Use

### 1. Data Collection:
Run the following command and show each gesture when prompted:
```bash
python Collection_Data.py    # After running this file "data/ " file will be created on your package
```

### 2. Extract Landmark Data:
```bash
python Creat_data.py      # After running this file "data.pickle" this file will be created
```

### 3. Train ML Model:
```bash
python ML_model.py      #  After running this file "model.p" will be created
```

### 4. Real-Time Prediction:
```bash
python main.py
```
Press **'h'** to close the window.

---

## 🔎 Gestures Recognized
| Label | Meaning        |
|-------|----------------|
| 0     | No             |
| 1     | Yes            |
| 2     | Thank you      |
| 3     | Greetings      |
| 4     | Hello          |
| 5     | Love           |
| 6     | OK             |
| 7     | Peace          |
| 8     | Super          |

---

## 💪 Future Improvements
- Add more gestures & classes
- Improve model accuracy using deep learning (e.g., CNN)
- Use LSTM for sequence-based gesture recognition
- Export as web or mobile app

---

## 👍 Acknowledgements
- [MediaPipe by Google](https://mediapipe.dev/)
- OpenCV
- scikit-learn

---

## 📅 License
This project is open-source and free to use for learning, research, and personal projects. No formal license is attached—just give credit if you find it helpful!

