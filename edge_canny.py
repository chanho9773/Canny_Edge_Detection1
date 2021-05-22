# 캐니 엣지 검출 (edge_canny.py)

import cv2, time
import numpy as np

img = cv2.imread('IMAGE1.jpg')
img = cv2.pyrDown(img)
img = cv2.pyrDown(img)

# 케니 엣지 적용
edge = cv2.Canny(img,100,200)

# 결과 출력
cv2.imshow('Original', img)
cv2.imshow('Canny', edge)
cv2.waitKey(0)
cv2.destroyAllWindows()