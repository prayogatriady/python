import cv2

face_cascade = cv2.CascadeClassifier('../opencv/haarcascades/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('../opencv/haarcascades/haarcascade_eye.xml')

def get_roi(path):
    img = cv2.imread(path) # get image
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # make it gray

    faces = face_cascade.detectMultiScale(gray, 1.3, 5) # check faces
    for (x,y,w,h) in faces:
        roi_color = img[y:y+h, x:x+w] # region of interest of face
        roi_gray = gray[y:y+h, x:x+w] # region of interest of gray face

        eyes = eye_cascade.detectMultiScale(roi_gray) # check eyes from gray face
        if len(eyes) >= 2: # check appearance of 2 eyes
            return roi_color