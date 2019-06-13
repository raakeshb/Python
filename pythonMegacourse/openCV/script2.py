import cv2

a=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
b=cv2.imread("/Users/raakeshb/Desktop/pythonMegacourse/CKU_2938.jpg")
c=cv2.cvtColor(b,cv2.COLOR_BGR2GRAY)
f=a.detectMultiScale(b,
scaleFactor=1.05,
minNeighbors=7)
for x,y,h,w in f:
    b=cv2.rectangle(b,(x,y),(x+w,y+h),(0,255,0),3)
   
h=cv2.resize(b,(600,500))
cv2.imshow("facedetection",h)
cv2.waitKey(0)
cv2.destroyAllWindows()

