import cv2

src = cv2.imread("IMG_5800.JPG", cv2.IMREAD_COLOR)
temp1 = cv2.imread("Ben.png", cv2.IMREAD_COLOR)

print(src.shape)
print(temp1.shape)