#https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_gui/py_image_display/py_image_display.html#display-image
import numpy as np
import cv2

# Load an color image in grayscale
#img = cv2.imread('plane.jpg',cv2.IMREAD_GRAYSCALE)
img = cv2.imread('OpenCV Play/plane.jpg',0)

cv2.imshow('image',img)
cv2.waitKey(0)
#cv2.destroyAllWindows()

cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()