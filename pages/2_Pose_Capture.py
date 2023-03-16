import streamlit as st
from PIL import Image
import numpy as np
import json
import pandas as pd
from yogi import load, main
import numpy as np
import tensorflow as tf

from yogi import posedetect

st.set_page_config(layout="wide")

page_bg_img =  """
    <style>

    [data-testid="stSidebarNav"] {
        background-size: cover;
        background-position: top left;
        background-repeat: no-repeat;
    }

    [data-testid="stSidebar"] {
        background-size: cover;
        background-position: top left;
        background-repeat: no-repeat;
        opacity: 0.85
    }

    [data-testid="stAppViewContainer"] {
        background-position:center;
        background: url("https://s32625.pcdn.co/wp-content/uploads/2020/08/Spring-Mist-oil-on-linen-20x24-Albert-Handell_WO-1536x1163.jpg.webp");
        background-size: cover;
        background-position: top left;
        background-repeat: no-repeat;
    }

    [data-testid="stHeader"] {
        background-colour:rgba(0,0,0,0);
        colour: white;
        opacity: 0.1
    }

    [data-testid="stToolbar"] {
        right: 2rem
    }

    [class="css-1wivap2 e16fv1kl3"] {
        background-color: #E6F3FB;
        border: 2px solid #c5d1f6;
        padding: 3%;
        box-shadow: 3px 3px #afdcf1;
        border-radius: 4px;
        opacity: 0.8;
        text-align: center;
    }

    [data-testid="stMetricLabel"] {
        opacity: 0;
        margin: -30px;
    }

    [data-testid="stText"] {
        background-color: #E6F3FB;
        border: 2px solid #c5d1f6;
        padding: 3%;
        box-shadow: 3px 3px #afdcf1;
        border-radius: 4px;
        opacity: 0.8;
        text-align: center;
        font-size: 20px
    }

        [data-testid="stImage"] {
        border:5px;
        padding:10px;
        border-radius: 15px;
        background:#E6F3FB;
        box-shadow: 3px 3px #afdcf1;
        border-radius: 4px;
        width="600"
        height="337";
        width: 500px;
        text-align: center;
        margin: auto;
        width: 100%;
        margin: 3%
    }

MuiBox-root css-0
    </style>

"""

# Maps bones to a matplotlib color name.
KEYPOINT_EDGE_INDS_TO_COLOR = {
    (0, 1): 'g',
    (0, 2): 'g',
    (1, 3): 'g',
    (2, 4): 'g',
    (0, 5): 'g',
    (0, 6): 'g',
    (5, 7): 'g',
    (7, 9): 'g',
    (6, 8): 'g',
    (8, 10): 'g',
    (5, 6): 'g',
    (5, 11): 'g',
    (6, 12): 'g',
    (11, 12): 'g',
    (11, 13): 'g',
    (13, 15): 'g',
    (12, 14): 'g',
    (14, 16): 'g',
}


st.markdown(page_bg_img, unsafe_allow_html=True)
st.metric(label="", value="Picture Capture")

col1, col2 = st.columns(2)

img_file_buffer = None
img_file_buffer = col1.camera_input("Take a picture")

model = load.loading_model()

# if st.button("New photo"):
#     img_file_buffer = None


if img_file_buffer is not None:
    # To read image file buffer as a PIL Image:
    img = Image.open(img_file_buffer)

    img.save("image_capture.jpeg")
    #img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    # To convert PIL Image to numpy array:
    img_array = np.array(img)




try:
    prediction = main.classification_model(model, img_array)
    col2.text(prediction.replace("_", " "))
except:
    print('error with cnn')

try:
    col2.image(f"Ground_Truths/{prediction}.jpeg")
except:
    print('error with showing gt')



### Pose Detection
try:
    input_image = tf.expand_dims(img_array, axis=0)
    input_size = 192
    input_image = tf.image.resize_with_pad(input_image, input_size, input_size)

    print('getting keypoints')
    keypoints_with_scores = posedetect.movenet(input_image)

    print('calculating angles')
    angles = posedetect.angle_calc(keypoints_with_scores)

    print('comparing angles')
    dict3 = posedetect.compare_angles(prediction, angles)

    print('red edges')
    red_edges = posedetect.render_red(dict3, KEYPOINT_EDGE_INDS_TO_COLOR)


    height = input_image.shape[0]
    width = input_image.shape[1]

    print('keypoints_and_edges_for_display_red')
    keypoints_xy, edges_xy, edge_colors = posedetect._keypoints_and_edges_for_display_red(keypoints_with_scores,
                                                                            red_edges,
                                                    height=height,
                                                    width=width,
                                                    keypoint_threshold=0.11)


    print('image_from_plot')
    image_from_plot = posedetect.draw_prediction_on_image_red(img_array,
                                keypoints_with_scores,
                                red_edges,
                                crop_region=None,
                                close_figure=False,
                                output_image_height=None)

    print('getting output overlay')
    output_overlay = posedetect.plot_red(keypoints_with_scores, img_array, red_edges)



    st.image(output_overlay)
except Exception as e:
    print(e)
