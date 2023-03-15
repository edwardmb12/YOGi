
# OVERALL PIPELINE

# IMPORTS
from yogi.preprocessor import preprocess_image
from yogi.predict import pred
from yogi.params import POSE_PROBA_THRESHOLD

# 1) IMAGE CAPTURE

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
