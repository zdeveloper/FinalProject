import numpy as np
import cv2
import time
from enhance import Enhance

enhance = Enhance()


cam = cv2.VideoCapture(0)

if not cam.isOpened()  :
	print("Can't open the camera")

isValid = True
prevImg = None

while True:
	try:
		ret, img = cam.read()
	except:
		print("Error the take a image")
		isValid = False

	if prevImg is not None:
		cv2.imshow('img',prevImg)
		time.sleep(0.1)
	if isValid == True:
		img = enhance.addGlasses(img=img)
		prevImg = img
		cv2.imshow('img',img)
		escKey = 27
		#waiting for keyboard input
		key = cv2.waitKey(30) & 0xff
		if key == escKey:
			break

cam.release()
cv2.destroyAllWindows()
