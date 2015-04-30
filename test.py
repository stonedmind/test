import numpy as np
import cv2
import sys

__file = sys.argv[1]

hsv_l = np.array([0,0,0])
hsv_h = np.array([0,0,255])

# Window
cv2.namedWindow("img",cv2.WINDOW_NORMAL)
cv2.namedWindow("res",cv2.WINDOW_NORMAL)

frame 		= cv2.imread(__file)
img 		= cv2.resize(frame, (400, 400)) 
fil 		= cv2.blur(img, (1, 1))
hsv 		= cv2.cvtColor(fil,cv2.COLOR_BGR2HSV)
threshold 	= cv2.inRange(hsv, hsv_l, hsv_h)
res 		= cv2.bitwise_and(hsv, hsv, mask=threshold)

kernel 		= cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(1,1))
erosion 	= cv2.erode(threshold,kernel,iterations = 1)
dilation 	= cv2.dilate(threshold,kernel,iterations = 1)

dilation 	= cv2.dilate(threshold,kernel,iterations = 1)
erosion 	= cv2.erode(threshold,kernel,iterations = 1)

moments 	= cv2.moments(threshold)

m01  	= moments['m01']
m10  	= moments['m10']
m00 	= moments['m00']

x		= m10 / m00
y		= m01 / m00

print x
print x
print y

cv2.imshow("img",img)
cv2.imshow("res",threshold)
cv2.waitKey(0)

