import numpy as np
import cv2 
from detect_fact_test import detect_face

Ben = cv2.imread('IMG_5800.JPG')
Ben_2 = cv2.imread('IMG_6012.JPG')

result = detect_face(Ben)
result2 = detect_face(Ben_2)

cv2.imshow('Ben Face', result)
cv2.imshow('Ben Face2', result2)

cv2.waitKey(0)