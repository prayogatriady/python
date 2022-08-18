import joblib
import json
import numpy as np
import cv2
import os

from wavelet import w2d
from roi import get_roi

__class_gender_to_number = {}
__class_number_to_gender = {}

__model = None

def classify_image(file_path):

    img = get_roi(file_path)

    if img is None:
        return "face should be contain two eyes"

    scalled_raw_img = cv2.resize(img, (32, 32))
    img_har = w2d(img, 'db1', 5)
    scalled_img_har = cv2.resize(img_har, (32, 32))
    combined_img = np.vstack((scalled_raw_img.reshape(32 * 32 * 3, 1), scalled_img_har.reshape(32 * 32, 1)))

    len_image_array = 32*32*3 + 32*32

    final = combined_img.reshape(1,len_image_array).astype(float)
    result = class_number_to_name(__model.predict(final)[0])

    return result

def class_number_to_name(class_num):
    return __class_number_to_gender[class_num]

def load_saved_artifacts():
    print("loading saved artifacts...start")
    global __class_gender_to_number
    global __class_number_to_gender

    # load saved json class
    with open("./artifacts/class_dictionary.json", "r") as f:
        __class_gender_to_number = json.load(f)
        __class_number_to_gender = {v:k for k,v in __class_gender_to_number.items()}

    global __model
    if __model is None:
        # load saved pickle model
        with open('./artifacts/saved_model.pkl', 'rb') as f:
            __model = joblib.load(f)
    print("loading saved artifacts...done")

if __name__ == '__main__':
    load_saved_artifacts()

    img_dir = input("Type directory: ")
    if os.path.exists(img_dir):
        print(classify_image(img_dir))
    else:
        print("Directory doesn't exists")