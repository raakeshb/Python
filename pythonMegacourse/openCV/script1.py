import cv2
a=cv2.imread("street_fighter_v_fighting_fighter_art_106069_3840x2160.jpg")
b=cv2.resize(a,(500,500))
cv2.imshow("hadokken",b)
cv2.waitKey(0)
cv2.destroyAllWindows()
