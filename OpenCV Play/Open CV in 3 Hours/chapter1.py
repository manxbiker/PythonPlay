#tutoral video https://www.youtube.com/watch?v=WQeoO7MI0Bs
#tutorial resources https://www.murtazahassan.com/learn-opencv-in-3-hours-chapter-1/
import cv2
print("Package imported")

# img = cv2.imread("OpenCV Play/Open CV in 3 Hours/Resources/lena.png")

# cv2.imshow("Output", img)
# cv2.waitKey(0)

# cap = cv2.VideoCapture("OpenCV Play/Open CV in 3 Hours/Resources/test_video.mp4")

# while True:
#     success, img = cap.read()
#     cv2.imshow("Video", img)

#     if cv2.waitKey(1) & 0xFF ==ord('q'):
#         break

cap2 = cv2.VideoCapture(1)
cap2.set(3, 620)
cap2.set(4, 480)
cap2.set(10, 150)

while True:
    success, img = cap2.read()
    cv2.imshow("Video", img)

    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break
