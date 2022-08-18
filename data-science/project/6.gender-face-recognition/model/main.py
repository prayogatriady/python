from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report

import joblib 
import json

from create_dir import generate_image_feature
from feature_eng import get_X_y_class

source = "../dataset/male_female/"
destination = "../dataset/cropped/"

if __name__ == '__main__':
    dict = generate_image_feature(source, destination, 50)
    print(dict)
    X, y, target_dict = get_X_y_class(dict)

    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

    pipe = Pipeline([('scaler', StandardScaler()), ('svc', SVC(kernel = 'rbf', C = 10))])
    pipe.fit(X_train, y_train)
    print(pipe.score(X_test, y_test))
    print(classification_report(y_test, pipe.predict(X_test)))


    # Save the model as a pickle in a file 
    joblib.dump(pipe, 'saved_model.pkl') 

    # save target dictionary
    with open("class_dictionary.json","w") as f:
        f.write(json.dumps(target_dict))


# dir1 = '../dataset/test/male/1 (189).jpg'
# new1 = convert(dir1)
# pred1 = pipe.predict(new1)[0]
# print(pred1)
# print(target_dict)

# print(list(target_dict.keys())[list(target_dict.values()).index(pred1)])