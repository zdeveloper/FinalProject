import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_eye.xml')

img = cv2.imread('input/Lionel-Messi.jpg')

glasses = cv2.imread('glasses/glasses3.png')

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

    width_offset = 20

    print eyes
    # cv2.addWeighted(src1, alpha, src2, beta, gamma[, dst[, dtype]])
    ex = eyes[0, 0] - width_offset
    ey = eyes[0, 1]
    ex2 = eyes[1, 0]
    ey2 = eyes[1, 1]
    ew2 = eyes[1, 2] + width_offset
    eh2 = eyes[1, 3]


    '''RESIZE'''
    size = (ex2+ew2-ex , ey2+eh2-ey)
    glasses = cv2.resize(glasses,size)
    file_name = "output/glasses" + str(w) + ".jpg"
    cv2.imwrite(file_name, glasses );

    masked_img = roi_color[ey:ey2+eh2, ex:ex2+ew2]
    print 'mask'
    # print masked_img.shape
    print 'glasses'
    print glasses.shape


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

    cv2.imwrite("output/mask.jpg", mask);
    cv2.imwrite("output/mask_inv.jpg", mask_inv);

    # Now black-out the area of logo in ROI
    img1_bg = cv2.bitwise_and(roi,roi,mask=mask_inv )

    # Take only region of logo from logo image.
    img2_fg = cv2.bitwise_and(img2,img2,mask)


    cv2.imwrite("output/img1_bg.jpg", img1_bg);
    cv2.imwrite("output/img2_fg.jpg", img2_fg);


    # Put logo in ROI and modify the main image
    dst = img1_bg
    img1[0:rows, 0:cols] = dst


    cv2.circle(roi_color, (ex, ey), 1, (0,255,0), 1)
    cv2.circle(roi_color, (ex2+ew2, ey2+eh2), 1, (0,0,255), 1)

    # dst = cv2.addWeighted(glasses,0.7,img2,0.3,0)
    for (ex,ey,ew,eh) in eyes:
        # cv2.rectangle(img, pt1, pt2, color, thickness)
        cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(255,255,0))
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
