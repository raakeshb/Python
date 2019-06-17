import cv2

video=cv2.VideoCapture(0)

while True:
    check, frame=video.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow("VideoCapturing",gray)
    m=cv2.waitKey(0)
    if m==ord('q'):
        break
video.release()
cv2.destroyAllWindows()
