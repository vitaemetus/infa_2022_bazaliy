import cv2
import numpy

import mss


# img = cv2.imread('images/ust.jpg')
# cv2.imshow('Output', img)
#
# cv2.waitKey(0)


# cap = cv2.VideoCapture('videos/hurt.mp4')
#
# while True:
#     success, img = cap.read()
#     cv2.imshow('Output', img)
#
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break


import numpy as np
import cv2
from mss import mss
from PIL import Image

bounding_box = {'top': 100, 'left': 0, 'width': 400, 'height': 300}

sct = mss()

while True:
    sct_img = sct.grab(bounding_box)
    cv2.imshow('screen', np.array(sct_img))

    if (cv2.waitKey(1) & 0xFF) == ord('q'):
        cv2.destroyAllWindows()
        break