import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_eye.xml')

img = cv2.imread('input/Lionel-Messi.jpg')

glasses = cv2.imread('glasses/glasses1.png')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# print gray
faces = face_cascade.detectMultiScale(gray, 1.3, 5)

for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    eyes = eye_cascade.detectMultiScale(roi_gray)

    # print eyes
    # x = eyes[0, 1]
    # xx = eyes[1, 1] + eyes[1, 3]
    #
    # y = eyes[0, 0]
    # yy = eyes[1, 0] + eyes[1, 2]

    # print x, xx
    # print y, yy

    file_name = "output/img" + str(w) + ".jpg"
    cv2.imwrite(file_name, img );
    # glasses.copyTo(img.rowRange(x, y).colRange(xx, yy));


    # print glasses
    # print img



    print eyes
    # cv2.addWeighted(src1, alpha, src2, beta, gamma[, dst[, dtype]])
    ex = eyes[0, 0]
    ey = eyes[0, 1]
    ex2 = eyes[1, 0]
    ey2 = eyes[1, 1]
    ew2 = eyes[1, 2]
    eh2 = eyes[1, 3]


    '''RESIZE'''
    size = (ex2+ew2-ex , ey2+eh2-ey)
    glasses = cv2.resize(glasses,size)
    file_name = "output/glasses" + str(w) + ".jpg"
    cv2.imwrite(file_name, glasses );

    masked_img = roi_color[ey:ey2+eh2, ex:ex2+ew2] = roi_color[ey:ey2+eh2, ex:ex2+ew2] * 5
    print 'mask'
    print masked_img.shape
    print 'glasses'
    print glasses.shape


    roi_color = cv2.addWeighted(glasses,0.7,masked_img,0.3,0)

    cv2.circle(roi_color, (ex, ey), 1, (0,255,0), 1)
    cv2.circle(roi_color, (ex2+ew2, ey2+eh2), 1, (0,0,255), 1)

    # dst = cv2.addWeighted(glasses,0.7,img2,0.3,0)
    for (ex,ey,ew,eh) in eyes:
        # cv2.rectangle(img, pt1, pt2, color, thickness)
        # cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(255,255,0))
        # cv2.circle(roi_color, (ex, ey), 1, (0,0,255), 1)
        # cv2.circle(roi_color, (ex+ew, ey), 1, (0,0,255), 1)
        # cv2.circle(roi_color, (ex, ey+eh), 1, (0,0,255), 1)
        # cv2.circle(roi_color, (ex+ew, ey+eh), 1, (0,0,255), 1)
        pass


    # addPicture(glasses, img, )

cv2.imwrite("output/Lionel-Messi.jpg", img );

def addPicture(src, dst, x, y, i, j):
    src.copyTo(dst.rowRange(1, 6).colRange(3, 10));

# cv2.imshow('img',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
