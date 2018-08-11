import numpy as np
import cv2 as cv
import math
import time

def video_mask(input_file="input.avi",output_file="output.avi",mask_image="mask.jpg"):
 fourcc = cv.VideoWriter_fourcc(*'MJPG')
 out = cv.VideoWriter(output_file,fourcc, 20.0, (848,480))## output video file 
 face_cascade = cv.CascadeClassifier('/usr/local/lib/python3.5/dist-packages/cv2/data/haarcascade_frontalface_default.xml')
 eye_cascade = cv.CascadeClassifier('/usr/local/lib/python3.5/dist-packages/cv2/data/haarcascade_eye.xml')

 cap = cv.VideoCapture(input_file) ## input video file

 while cap.isOpened():
    ret, img = cap.read()
    mask=cv.imread(mask_image)
    mask_gray = cv.cvtColor(mask, cv.COLOR_BGR2GRAY)
    img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)


    for (x,y,w,h) in faces:
        roi_color = img[y:y+h, x:x+w]
        roi_gray = img_gray[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        cnt=-1
        eye2_mid_x=eye2_mid_y=eye1_mid_x=eye1_mid_y=-1
        for (ex,ey,ew,eh) in eyes:
            cnt=cnt+1
            if cnt==0:
                eye1_mid_x=(ex+ew)/2
                eye1_mid_y=(ey+eh)/2
            else:
                eye2_mid_x=(ex+ew)/2
                eye2_mid_y=(ey+eh)/2
        if eye1_mid_x!=-1:
         rotate_angle=math.atan(float(eye2_mid_y-eye1_mid_y)/(float(eye2_mid_x-eye2_mid_x)+0.000001))
         
         replace_roi = cv.resize(mask,(w,h),interpolation = cv.INTER_CUBIC)
         replace_roi_gray= cv.cvtColor(replace_roi, cv.COLOR_BGR2GRAY)
         tmp_rows,tmp_cols = replace_roi_gray.shape
         M = cv.getRotationMatrix2D((tmp_cols/2,tmp_rows/2),rotate_angle,1.0)
         over_roi = cv.warpAffine(replace_roi,M,(tmp_cols,tmp_rows),cv.BORDER_CONSTANT, borderValue=(255,255,255))
         mask_gray = cv.cvtColor(over_roi, cv.COLOR_BGR2GRAY)
        else:
         replace_roi = cv.resize(mask,(w,h),interpolation = cv.INTER_CUBIC)
         over_roi=replace_roi
         mask_gray= cv.cvtColor(over_roi, cv.COLOR_BGR2GRAY)
        #cv.imwrite("roi.jpg",over_roi)
        for i in range(h):
            for j in range(w):
                if mask_gray[i][j]>235:
                    continue
                else:
                    img[y+i][x+j]=over_roi[i][j]    
    out.write(img)
 cap.release()
 out.release()


def camera_mask(tim=1,camera_no=0,output_file="output.avi",mask_image="mask.jpg"):
 fourcc = cv.VideoWriter_fourcc(*'MJPG')
 out = cv.VideoWriter(output_file,fourcc, 20.0, (848,480))## output video file 
 face_cascade = cv.CascadeClassifier('/usr/local/lib/python3.5/dist-packages/cv2/data/haarcascade_frontalface_default.xml')
 eye_cascade = cv.CascadeClassifier('/usr/local/lib/python3.5/dist-packages/cv2/data/haarcascade_eye.xml')

 cap = cv.VideoCapture(camera_no) ## camera number
 start=time.time()
 new_time=start
 while float(float(new_time-start)/float(60))<=tim:
    
    ret, img = cap.read()
    mask=cv.imread(mask_image)
    mask_gray = cv.cvtColor(mask, cv.COLOR_BGR2GRAY)
    img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:
        roi_color = img[y:y+h, x:x+w]
        roi_gray = img_gray[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        cnt=-1
        eye2_mid_x=eye2_mid_y=eye1_mid_x=eye1_mid_y=-1
        for (ex,ey,ew,eh) in eyes:
            cnt=cnt+1
            if cnt==0:
                eye1_mid_x=(ex+ew)/2
                eye1_mid_y=(ey+eh)/2
            else:
                eye2_mid_x=(ex+ew)/2
                eye2_mid_y=(ey+eh)/2
        if eye1_mid_x!=-1:
         rotate_angle=math.atan(float(eye2_mid_y-eye1_mid_y)/(float(eye2_mid_x-eye2_mid_x)+0.000001))
         
         replace_roi = cv.resize(mask,(w,h),interpolation = cv.INTER_CUBIC)
         replace_roi_gray= cv.cvtColor(replace_roi, cv.COLOR_BGR2GRAY)
         tmp_rows,tmp_cols = replace_roi_gray.shape
         M = cv.getRotationMatrix2D((tmp_cols/2,tmp_rows/2),rotate_angle,1.0)
         over_roi = cv.warpAffine(replace_roi,M,(tmp_cols,tmp_rows),cv.BORDER_CONSTANT, borderValue=(255,255,255))
         mask_gray = cv.cvtColor(over_roi, cv.COLOR_BGR2GRAY)
        else:
         replace_roi = cv.resize(mask,(w,h),interpolation = cv.INTER_CUBIC)
         over_roi=replace_roi
         mask_gray= cv.cvtColor(over_roi, cv.COLOR_BGR2GRAY)
        #cv.imwrite("roi.jpg",over_roi)
        for i in range(h):
            for j in range(w):
                if mask_gray[i][j]>240:
                    continue
                else:
                    img[y+i][x+j]=over_roi[i][j]
    new_time=time.time()    
    out.write(img)
 cap.release()
 out.release()



def image_mask(input_image="input.jpg",output_image="output.jpg",mask_image="mask.jpg"):
    img = cv.imread(input_image)
    face_cascade = cv.CascadeClassifier('/usr/local/lib/python3.5/dist-packages/cv2/data/haarcascade_frontalface_default.xml')
    eye_cascade = cv.CascadeClassifier('/usr/local/lib/python3.5/dist-packages/cv2/data/haarcascade_eye.xml')
    mask=cv.imread(mask_image)
    mask_gray = cv.cvtColor(mask, cv.COLOR_BGR2GRAY)
    img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:
        roi_color = img[y:y+h, x:x+w]
        roi_gray = img_gray[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        cnt=-1
        eye2_mid_x=eye2_mid_y=eye1_mid_x=eye1_mid_y=-1
        for (ex,ey,ew,eh) in eyes:
            cnt=cnt+1
            if cnt==0:
                eye1_mid_x=(ex+ew)/2
                eye1_mid_y=(ey+eh)/2
            else:
                eye2_mid_x=(ex+ew)/2
                eye2_mid_y=(ey+eh)/2
        if eye1_mid_x!=-1:
         rotate_angle=math.atan(float(eye2_mid_y-eye1_mid_y)/(float(eye2_mid_x-eye2_mid_x)+0.000001))
         
         replace_roi = cv.resize(mask,(w,h),interpolation = cv.INTER_CUBIC)
         replace_roi_gray= cv.cvtColor(replace_roi, cv.COLOR_BGR2GRAY)
         tmp_rows,tmp_cols = replace_roi_gray.shape
         M = cv.getRotationMatrix2D((tmp_cols/2,tmp_rows/2),rotate_angle,1.0)
         over_roi = cv.warpAffine(replace_roi,M,(tmp_cols,tmp_rows),cv.BORDER_CONSTANT, borderValue=(255,255,255))
         mask_gray = cv.cvtColor(over_roi, cv.COLOR_BGR2GRAY)
        else:
         replace_roi = cv.resize(mask,(w,h),interpolation = cv.INTER_CUBIC)
         over_roi=replace_roi
         mask_gray= cv.cvtColor(over_roi, cv.COLOR_BGR2GRAY)
        #cv.imwrite("roi.jpg",over_roi)
        for i in range(h):
            for j in range(w):
                if mask_gray[i][j]>235:
                    continue
                else:
                    img[y+i][x+j]=over_roi[i][j]
    
    cv.imwrite(output_image,img)
