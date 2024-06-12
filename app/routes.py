from flask import Blueprint, render_template, Response
import cv2
import dlib
import numpy as np
import os

main = Blueprint('main', __name__)

# Use an absolute path for the predictor file
predictor_path = os.path.join(os.path.dirname(__file__), '..', 'shape_predictor_68_face_landmarks.dat')
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(predictor_path)

def detect_gaze(landmarks, frame, gray):
    # [remaining code unchanged]
    pass

@main.route('/')
def index():
    return render_template('index.html')

def gen_frames():
    cap = cv2.VideoCapture(0)
    while True:
        success, frame = cap.read()
        if not success:
            break
        else:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = detector(gray)

            for face in faces:
                x, y, w, h = (face.left(), face.top(), face.width(), face.height())
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                landmarks = predictor(gray, face)
                for n in range(0, 68):
                    x = landmarks.part(n).x
                    y = landmarks.part(n).y
                    cv2.circle(frame, (x, y), 2, (0, 64, 100), -1)
                gaze = detect_gaze(landmarks, frame, gray)
                cv2.putText(frame, gaze, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@main.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')
