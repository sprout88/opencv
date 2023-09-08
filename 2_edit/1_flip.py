import cv2
import os

os.chdir(os.path.dirname(__file__))

src = cv2.imread("water.png",cv2.IMREAD_COLOR)
dst = cv2.flip(src,0)

cv2.imshow("src",src)
cv2.imshow("dst",dst)
cv2.waitKey()
cv2.destroyAllWindows()