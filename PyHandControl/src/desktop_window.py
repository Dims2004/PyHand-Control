import cv2
import numpy as np

class DesktopWindow:
    def __init__(self, name, image):
        self.name = name
        self.image = image
        self.has_image = False
        self.frame = np.zeros((400, 400, 3), dtype=np.uint8)

    def draw(self):
        self.frame[:] = (40, 40, 40)
        cv2.putText(self.frame, self.name, (20, 40),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)

        if self.has_image:
            img = cv2.resize(self.image, (200, 200))
            self.frame[100:300, 100:300] = img

        cv2.imshow(self.name, self.frame)
