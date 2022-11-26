import cv2
import numpy as np
from PIL import Image
import mss
import win32gui
import pyautogui

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

# cap = cv2.VideoCapture("videos/hurt.mp4")
kernel = np.ones((5, 5), 'uint8')

while True:
    window_rect = (120, 650, 220, 220)
    img = pyautogui.screenshot(region=window_rect)
    img = np.array(img)
    erode_img = cv2.erode(img, kernel, iterations=1)
    (thresh, img) = cv2.threshold(img, 150, 255, cv2.THRESH_BINARY)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    cv2.imshow('Output', img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
