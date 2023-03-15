
# OVERALL PIPELINE

# IMPORTS
from yogi.preprocessor import preprocess_image
from yogi.load import loading_model
from yogi.predict import pred
from yogi.threshold import threshold

# 1) IMAGE CAPTURE

# 2) CLASSIFICATION MODEL

    ## TAKES IMAGE CAPTURE AS FEED

    image_input

    ## PREPROCESS IMAGE CAPTURE

    preprocessed_image = preprocess_image(image_input)

    ## LOAD MODEL

    model = loading_model()

    ## PREDICT

    prediction = pred(model, preprocessed_image)
    pose_name = prediction[0]
    pose_proba = prediction[1]

    ## THRESHOLD
    if pose_proba < 0.6:
        print("Detecting Pose ...")
    else:
        print(pose_name)



# 3) POSE DETECTION MODEL

    ## IF CALSSIFIED, FIND GROUND TRUTH

    ## TAKE IMAGE CAPTURE, RUN POSE DETECTION

    ## COMPARE GROUND TRUTH TO POSE

    ## FEEDBACK
