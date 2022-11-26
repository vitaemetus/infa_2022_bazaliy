import cv2
import numpy as np
import pyautogui
import pygetwindow as gw
'''Этот кусочек кода делает скрин'''
window_name="Need for Speed™ Most Wanted"
fourcc=cv2.VideoWriter_fourcc(*"XVID")
fps=30.0
window=gw.getWindowsWithTitle(window_name)[0]
window.activate()
while 1:
    img=pyautogui.screenshot(region=(window.left,window.top,window.width,window.height))
    frame=np.array(img)
    cv2.imshow("record",frame)
    if(cv2.waitKey(1)==ord("q")): break
cv2.destroyAllWindows()
