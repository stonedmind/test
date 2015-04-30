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

contours,h	= cv2.findContours(threshold, 1, 2)

cnt = contours[0]
M 	= cv2.moments(cnt)

cx = int(M['m10']/M['m00'])
cy = int(M['m01']/M['m00'])

print cx
print cy

for x in range(0, 400):
	img.itemset((x,x,0),255)
	img.itemset((x,x,1),255)
	img.itemset((x,x,2),255)

cv2.imshow("img",img)
cv2.imshow("res",threshold)
cv2.waitKey(0)

