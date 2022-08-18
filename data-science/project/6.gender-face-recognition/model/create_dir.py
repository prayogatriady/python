import os
import cv2
from roi import get_roi


def generate_image_feature(source_dir, destination_dir, n_pair_features = 50):
    gender_file_names_dict = {}

    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    list_exist_imgs = []
    for folder in os.scandir(destination_dir):
        gender = folder.path.split('/')[-1]
        gender_file_names_dict[gender] = []
        count = 0
        for file in os.scandir(folder.path):
            gender_file_names_dict[gender].append(file.path)
            count += 1
        list_exist_imgs.append(count)

    # check if files exist for n_pair_features
    if len(list_exist_imgs)>0 and list_exist_imgs[0] == list_exist_imgs[1] and list_exist_imgs[0] == n_pair_features:
        return gender_file_names_dict

    # if files don't exist
    source_img_dirs = []
    for source_folder in os.scandir(source_dir): # scan source_folder inside source_dir and save each paths to source_img_dirs
        if source_folder.is_dir():
            source_img_dirs.append(source_folder.path)

    for img_dir in source_img_dirs:
        count = 0
        gender = img_dir.split('/')[-1]
        gender_file_names_dict[gender] = []
        
        for entry in os.scandir(img_dir):
            try:
                roi_color = get_roi(entry.path)
            except:
                print(entry.path)

            if roi_color is not None:
                cropped_folder = destination_dir + gender
                if not os.path.exists(cropped_folder):
                    os.makedirs(cropped_folder)
                cropped_file_name = gender + "_" + str(count) + ".png"
                cropped_file_path = cropped_folder + "/" + cropped_file_name
                cv2.imwrite(cropped_file_path, roi_color)
                gender_file_names_dict[gender].append(cropped_file_path)
                count += 1

                if count == n_pair_features:
                    break
    
    return gender_file_names_dict