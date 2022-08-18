import cv2
from wavelet import w2d
import numpy as np

def get_X_y_class(file_names_dict):
    class_dict = {}
    count = 0
    for gender in file_names_dict.keys():
        class_dict[gender] = count
        count += 1

    X, y = [],[]
    for gender, image_files in file_names_dict.items():
        for training_image in image_files:
            img = cv2.imread(training_image) # read image
            scalled_raw_img = cv2.resize(img, (32, 32)) # resize image

            img_har = w2d(img,'db1',5) # call wavelet func
            scalled_img_har = cv2.resize(img_har, (32, 32)) # resize waveleted image

            a = scalled_raw_img.reshape(32*32*3,1) # resbape to numpy 2d
            b = scalled_img_har.reshape(32*32,1) # resbape to numpy 2d
            combined_img = np.vstack((a,b)) # stack vertically

            X.append(combined_img) # append to the empty list
            y.append(class_dict[gender])


    X = np.array(X).reshape(len(X),len(X[0])).astype(float) # convert list to numpy => reshape as len(X) = row, and len(X[0]) = columns => convert to float
    
    return X, y, class_dict


def convert(path):
    img = cv2.imread(path) # read image
    scalled_raw_img = cv2.resize(img, (32, 32)) # resize image

    img_har = w2d(img,'db1',5) # call wavelet func
    scalled_img_har = cv2.resize(img_har, (32, 32)) # resize waveleted image

    a = scalled_raw_img.reshape(32*32*3,1) # resbape to numpy 2d
    b = scalled_img_har.reshape(32*32,1) # resbape to numpy 2d
    combined_img = np.vstack((a,b)) # stack vertically

    X = np.array(combined_img).reshape(len(combined_img[0]),len(combined_img)).astype(float)
    return X