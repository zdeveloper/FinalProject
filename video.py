import numpy as np
import cv2
from enhance import Enhance

enhance = Enhance()

# multiple cascades: https://github.com/Itseez/opencv/tree/master/data/haarcascades

#https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml
face_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')
#https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_eye.xml
eye_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_eye.xml')

cam = cv2.VideoCapture(0)

if not cam.isOpened()  :
	print("Can't open the camera")

isValid = True

while True:
	try:
		ret, img = cam.read()
	except:
		print("Error the take a image")
		isValid = False

	if isValid == True:
		try:
			gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
			faces = face_cascade.detectMultiScale(gray, 1.3, 5)

			for (x,y,w,h) in faces:
				cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
				roi_gray = gray[y:y+h, x:x+w]
				roi_color = img[y:y+h, x:x+w]

				eyes = eye_cascade.detectMultiScale(roi_gray)
				for (ex,ey,ew,eh) in eyes:
					cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

			cv2.imshow('img',img)
			escKey = 27
			#waiting for keyboard input
			key = cv2.waitKey(30) & 0xff
			if key == escKey:
				break
		except:
			print("Error during the convertion")



cam.release()
cv2.destroyAllWindows()
