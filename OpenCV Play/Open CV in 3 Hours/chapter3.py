import cv2
import numpy as py

img = cv2.imread("OpenCV Play/Open CV in 3 Hours/Resources/lambo.png")
print(img.shape)

imgResize = cv2.resize(img,(300,200))
print(imgResize.shape)

imgCropped = img[0:200, 200:500]

cv2.imshow("Output", img)
cv2.imshow("Resized", imgResize)
cv2.imshow("Cropped", imgCropped)
cv2.waitKey(0)