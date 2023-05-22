import cv2
import numpy as np
img = cv2.imread("poster.jpg")
rocket = img[120:360,400:500]
img[0:240, 500:600] = rocket

print(img)
text_to_show = "I love coding"
cv2.putText(
    img,
text_to_show,
(20,220),
fontFace = cv2.FONT_HERSHEY_COMPLEX_SMALL,
fontScale = 1,
color = (0,0,255)
)

cv2.imshow("displayimage", img)
# grey_img =cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
# cv2.imshow("Greyskill",grey_img) 
# print(grey_img)
# black = np.zeros([6,6])
# print(black[2:4, 2:4])
# cv2.imshow("displayimage",black)
cv2.waitKey(0)