import cv2

src = cv2.imread("IMG_5800.JPG", cv2.IMREAD_COLOR)
temp1 = cv2.imread("Ben.png", cv2.IMREAD_COLOR)
height, width = temp1.shape[:2]                    

result = cv2.matchTemplate(src, temp1, cv2.TM_CCOEFF_NORMED)
minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(result)
upperleft = maxLoc                                          
lowerright = (maxLoc[0] + width, maxLoc[1] + height)        
dst = cv2.rectangle(src,upperleft,lowerright,(0,255,0),3)  
cv2.imshow("Ben face Detect", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()