import numpy as np
import cv2

class Enhance(object):
    def __init__(self):
        self.debug = False
        self.face_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')
        self.eye_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_eye.xml')

        self.glasses = cv2.imread('glasses/glasses1.png')

    def __loadFromFile(self):
        img = cv2.imread('input/Lionel-Messi.jpg')
        # img = cv2.imread('input/decaprio.jpg')
        # img = cv2.imread('input/Brad-Pitt.jpg')
        return img;

    def addGlasses(self, img=None, glasses=None, debug=None):

        if img is None:
            img = self.__loadFromFile()

        if glasses is None:
            glasses = self.glasses

        if debug is None:
            debug = self.debug

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # print gray
        faces = self.face_cascade.detectMultiScale(gray, 1.3, 3)

        for (x,y,w,h) in faces:
            # print x,y,w,h

            if debug:
                cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

            roi_gray = gray[y:y+h, x:x+w]
            roi_color = img[y:y+h, x:x+w]
            eyes = self.eye_cascade.detectMultiScale(roi_gray, minNeighbors=7)
            if (not len(eyes) > 0):
            	return img
            # print eyes
            # order the eyes based on their x direction , very important
            eyes = sorted(eyes, key=lambda eye: eye[0])

            # print 'eyes', eyes
            # print glasses
            # print img

            width_offset = int((w-x) * 0.3)

            extra_width = int((w-x) * 1.2)
            # width_offset = 0

            # print 'eyes[0]', eyes[0]
            ex, ey, ew, eh= eyes[0]

            # we use len(eyes)-1 becuase sometimes we arent garanteed that we only get 2 eyes
            # print 'eyes[1]', eyes[len(eyes)-1]
            ex2, ey2, ew2, eh2 = eyes[len(eyes)-1]

            ex = ex - width_offset
            ew2 = ew2 + width_offset


            width = ex2+ew2-ex + extra_width

            '''RESIZE'''
            size = (ex2+ew2-ex, ey2+eh2-ey)
            if size[0] < 1 or size[1] < 1:
            	return img
            # print 'size', size
            glasses = cv2.resize(glasses,size)
            # file_name = "output/glasses" + str(w) + ".jpg"
            # cv2.imwrite(file_name, glasses );
            row, col, channels = glasses.shape

            '''
            Note the we translate back to the img coordinates since
            we might have a negative ex since we subtract an offset
            '''
            masked_img = img[ ey+y:row+ey+y, ex+x:col+ex+x]
            if debug:
                print "masked_img.shape", masked_img.shape
                print 'glasses.shape',  glasses.shape

            # roi_color = cv2.addWeighted(masked_img,0.5,glasses,0.5,5)


            # I want to put logo on top-left corner, So I create a ROI
            img1 = masked_img
            img2 = glasses
            rows,cols,channels = img2.shape
            roi = img1[0:rows, 0:cols]

            # Now create a mask of logo and create its inverse mask also
            img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
            img2gray = cv2.bitwise_not(img2gray)
            ret, mask = cv2.threshold(img2gray, 127, 255, cv2.THRESH_BINARY)

            mask_inv = cv2.bitwise_not(mask)

            if debug:
                cv2.imwrite("output/mask.jpg", mask);
                cv2.imwrite("output/mask_inv.jpg", mask_inv);

            # Now black-out the area of logo in ROI
            img1_bg = cv2.bitwise_and(roi,roi,mask=mask_inv )

            # Take only region of logo from logo image.
            #img2_fg = cv2.bitwise_and(img2,img2,mask)

            if debug:
                cv2.imwrite("output/img1_bg.jpg", img1_bg);
                # cv2.imwrite("output/img2_fg.jpg", img2_fg);


            # Put logo in ROI and modify the main image
            dst = img1_bg
            img1[0:rows, 0:cols] = dst

            # dst = cv2.addWeighted(glasses,0.7,img2,0.3,0)
            for (ex,ey,ew,eh) in eyes:
                # cv2.rectangle(img, pt1, pt2, color, thickness)
                if debug:
                    cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(255,255,0))
                    cv2.circle(roi_color, (ex, ey), 1, (0,0,255), 1)
                    cv2.circle(roi_color, (ex+ew, ey), 1, (0,0,255), 1)
                    cv2.circle(roi_color, (ex, ey+eh), 1, (0,0,255), 1)
                    cv2.circle(roi_color, (ex+ew, ey+eh), 1, (0,0,255), 1)
                pass
            break
        return img
    def writeImageToFile(self, img):
        cv2.imwrite("output/output.jpg", img );

# enhance = Enhance()
# enhance.writeImageToFile(enhance.addGlasses())

# cv2.imshow('img',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
