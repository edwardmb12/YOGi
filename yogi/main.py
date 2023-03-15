
# OVERALL PIPELINE

# IMPORTS
from yogi.preprocessor import preprocess_image
from yogi.predict import pred
from yogi.params import POSE_PROBA_THRESHOLD
import json

# 1) IMAGE CAPTURE
# Opening JSON file from webcam capture and giving rgb array in form (398, 704, 3)
with open('img_array.json', 'r') as infile:
    img_array_from_json = np.array(json.load(infile))

img_array_from_json

# 2) CLASSIFICATION MODEL

def classification_model(model, image_input=None):

    ## PREPROCESS IMAGE CAPTURE
    preprocessed_image = preprocess_image(image_input)

    ## PREDICT
    pose, pose_proba = pred(model, preprocessed_image)

    if pose_proba < POSE_PROBA_THRESHOLD:
        pose = "Detecting Pose ..."

    return pose

# 3) POSE DETECTION MODEL

    ## IF CALSSIFIED, FIND GROUND TRUTH

    ## TAKE IMAGE CAPTURE, RUN POSE DETECTION

    ## COMPARE GROUND TRUTH TO POSE

    ## FEEDBACK
