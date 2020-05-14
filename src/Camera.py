import cv2
import numpy as np


class Camera:

    # video dimensions and camera ID defined at construction
    def __init__(self, cam_id):
        self.camera_id = cam_id
        self.cap = cv2.VideoCapture(self.camera_id)

    # returns the newest frame from the camera as a 3 dimensional numpy array
    def frameRGB(self):
        ret, frame = self.cap.read()
        # if ret is False, no image was captured and black image is returned
        if ret == False:
            return np.zeros(shape=(300, 300, 3)).astype(np.uint8)

        return frame
