
# OVERALL PIPELINE

# IMPORTS
from yogi.preprocessor import preprocess_image
from yogi.predict import pred
from yogi.params import POSE_PROBA_THRESHOLD
import json
import numpy as np
from yogi import angle_calc

# 1) IMAGE CAPTURE
# Opening JSON file from webcam capture and giving rgb array in form (398, 704, 3)

# with open('img_array.json', 'r') as infile:
#     img_array_from_json = np.array(json.load(infile))

# img_array_from_json

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


def pose_detection_model(image, prediction):
    KEYPOINT_DICT = angle_calc.KEYPOINT_DICT
    KEYPOINT_EDGE_INDS_TO_COLOR = angle_calc.KEYPOINT_EDGE_INDS_TO_COLOR
    keypoints_with_scores = angle_calc.movenet(image)
    height = image[0]
    width = image[1]

    # angles = angle_calc.angle_calc(image)
    dict3 = angle_calc.compare_angles(image, prediction)
    RED_EDGES = angle_calc.render_red(dict3, KEYPOINT_EDGE_INDS_TO_COLOR)
    keypoints_xy, edges_xy, edge_colors = angle_calc._key_points_and_edges_for_display_red(keypoints_with_scores,
                                                     height=height,
                                                     width=width,
                                                     keypoint_threshold=0.11)

    image_from_plot = angle_calc.draw_prediction_on_image_red(image,
                                 keypoints_with_scores,

                                 crop_region=None,
                                 close_figure=False,
                                 output_image_height=None)

    return angle_calc.plot_red(image)
