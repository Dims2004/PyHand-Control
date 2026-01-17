import cv2
import os
from hand_tracker import HandTracker
from desktop_window import DesktopWindow

# ==== Load Image ====
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGE_PATH = os.path.join(BASE_DIR, "..", "assets", "image.png")
image = cv2.imread(IMAGE_PATH)

if image is None:
    raise FileNotFoundError("image.png tidak ditemukan")

# ==== Init Desktop Windows ====
desktop1 = DesktopWindow("Desktop 1", image)
desktop2 = DesktopWindow("Desktop 2", image)

desktop1.has_image = True
desktop2.has_image = False

# ==== Camera ====
cap = cv2.VideoCapture(0)
tracker = HandTracker()

holding = False
held_from = None

while True:
    ret, cam = cap.read()
    cam = cv2.flip(cam, 1)

    results = tracker.process(cam)

    if results.multi_hand_landmarks:
        hand = results.multi_hand_landmarks[0]
        fist = tracker.is_fist(hand)
        x = tracker.get_x(cam, hand)

        # ==== GRAB ====
        if fist and not holding:
            if x < cam.shape[1]//2 and desktop1.has_image:
                desktop1.has_image = False
                holding = True
                held_from = "desktop1"

            elif x >= cam.shape[1]//2 and desktop2.has_image:
                desktop2.has_image = False
                holding = True
                held_from = "desktop2"

        # ==== DROP ====
        if not fist and holding:
            if x < cam.shape[1]//2:
                desktop1.has_image = True
            else:
                desktop2.has_image = True

            holding = False
            held_from = None

    desktop1.draw()
    desktop2.draw()

    cv2.imshow("Camera (Gesture Sensor)", cam)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
