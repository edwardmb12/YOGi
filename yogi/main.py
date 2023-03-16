
# OVERALL PIPELINE

# IMPORTS
from yogi.preprocessor import preprocess_image
from yogi.predict import pred
from yogi.params import POSE_PROBA_THRESHOLD
import json
import numpy as np
from yogi import angle_calc
import tensorflow as tf

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
        pose = "No pose detected"

    return pose

# 3) POSE DETECTION MODEL


def pose_detection_model(image, prediction):
    KEYPOINT_DICT = angle_calc.KEYPOINT_DICT
    KEYPOINT_EDGE_INDS_TO_COLOR = angle_calc.KEYPOINT_EDGE_INDS_TO_COLOR

    Downward_Facing_Dog_pose_or_Adho_Mukha_Svanasana_m = angle_calc.Downward_Facing_Dog_pose_or_Adho_Mukha_Svanasana_m
    Tree_Pose_or_Vrksasana_m = angle_calc.Tree_Pose_or_Vrksasana_m
    Warrior_I_Pose_or_Virabhadrasana_I_m =  angle_calc.Warrior_I_Pose_or_Virabhadrasana_I_m
    Warrior_II_Pose_or_Virabhadrasana_II_m = angle_calc.Warrior_II_Pose_or_Virabhadrasana_II_m
    Warrior_III_Pose_or_Virabhadrasana_III_m = angle_calc.Warrior_III_Pose_or_Virabhadrasana_III_m

    input_image = tf.expand_dims(image, axis=0)
    input_size = 192
    input_image = tf.image.resize_with_pad(input_image, input_size, input_size)


    keypoints_with_scores = angle_calc.movenet(input_image)

    angles = angle_calc.angle_calculation(keypoints_with_scores)

    dict3 = angle_calc.compare_angles(prediction, angles)

    RED_EDGES = angle_calc.render_red(dict3, KEYPOINT_EDGE_INDS_TO_COLOR)

    height = image.shape[0]
    width = image.shape[1]


    keypoints_xy, edges_xy, edge_colors = angle_calc._keypoints_and_edges_for_display_red(keypoints_with_scores,
                                                    RED_EDGES,
                                                    height=height,
                                                    width=width,
                                                    keypoint_threshold=0.11)

    image_from_plot = angle_calc.draw_prediction_on_image_red(image,
                                    keypoints_with_scores,
                                    crop_region=None,
                                    close_figure=False,
                                    output_image_height=None)

    output_overlay = angle_calc.plot_red(keypoints_with_scores,image)

    return output_overlay
