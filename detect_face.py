# -*- coding:utf-8 -*-

import cv2
import numpy as np


def process_frame(cascade, frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face = cascade.detectMultiScale(gray, 1.1, 3)
    for (x, y, w, h) in face:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 50, 255), 3)


if __name__ == "__main__":
    # Load cascade
    CADCADE_FILE = '/usr/local/opt/opencv/share/OpenCV/haarcascades/haarcascade_frontalface_alt.xml'
    cascade = cv2.CascadeClassifier(CADCADE_FILE)

    # Capture setting
    cap = cv2.VideoCapture(0)
    width = int(cap.get(3)/2)
    height = int(cap.get(4)/2)

    # Read loop
    print("Press Ctrl-C to stop screen.")
    while cap.isOpened():
        ret, frame = cap.read()
        frame = cv2.resize(frame, (width, height))

        process_frame(cascade, frame)
        
        cv2.imshow('camera capture', frame)
        if cv2.waitKey(10) > 0:
            break
    
    # Release
    cap.release()
    cv2.destroyAllWindows()

