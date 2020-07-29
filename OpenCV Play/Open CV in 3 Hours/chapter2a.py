import cv2
import numpy as np
kernel = np.ones((5,5),np.uint8)

cap2 = cv2.VideoCapture(1)
cap2.set(3, 620)
cap2.set(4, 480)
cap2.set(10, 150)

while True:
    success, img = cap2.read()
    cv2.imshow("Video", img)


    
    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray,(7,7),0)
    imgCanny = cv2.Canny(img,150,200)
    imgDialation = cv2.dilate(imgCanny,kernel,iterations=1)
    imgEroded = cv2.erode(imgDialation,kernel,iterations=1)
    
    cv2.imshow("Gray Image",imgGray)
    cv2.imshow("Blur Image",imgBlur)
    cv2.imshow("Canny Image",imgCanny)
    cv2.imshow("Dialation Image",imgDialation)
    cv2.imshow("Eroded Image",imgEroded)

    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break