import cv2
import mediapipe as mp

class HandTracker:
    def __init__(self):
        self.hands = mp.solutions.hands.Hands(
            max_num_hands=1,
            min_detection_confidence=0.7,
            min_tracking_confidence=0.7
        )

    def process(self, frame):
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        return self.hands.process(rgb)

    def is_fist(self, hand):
        fingers = [(8,6),(12,10),(16,14),(20,18)]
        for tip, pip in fingers:
            if hand.landmark[tip].y < hand.landmark[pip].y:
                return False
        return True

    def get_x(self, frame, hand):
        w = frame.shape[1]
        return int(hand.landmark[8].x * w)
