import cv2
import numpy as np
from PIL import Image
import mss
import win32gui
import pyautogui

# маска для сглаживания входящей картинки:
kernel = np.ones((5, 5), 'uint8')

while True:
    window_rect = (120, 650, 220, 220)  # область работыOpenCV
    img = pyautogui.screenshot(region=window_rect)  # CV делает скриншот своей области
    img = np.array(img)  # конвертация скриншота в список
    erode_img = cv2.erode(img, kernel, iterations=1)  # сглаживание
    (thresh, img) = cv2.threshold(img, 150, 255, cv2.THRESH_BINARY)  # отсеивание пикселей
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    cv2.imshow('Output', img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
