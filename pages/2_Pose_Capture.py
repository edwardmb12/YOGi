import streamlit as st
from PIL import Image
import numpy as np
import json
import pandas as pd
from yogi import load, main
import numpy as np

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
        font-size: 30px
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

st.markdown(page_bg_img, unsafe_allow_html=True)
st.text("Picture Capture")

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

    # Check the type of img_array:
    # Should output: <class 'numpy.ndarray'>

    # st.write(type(img_array))

    # Check the shape of img_array:
    # Should output shape: (height, width, channels)
    # st.write(img_array.shape)
    # st.write(img_array)

    # # save the numpy array to a JSON file
    # with open('img_array.json', 'w') as outfile:
    #     json.dump(img_array.tolist(), outfile)

    # # load the numpy array from the JSON file and reshape it to its original form
    # with open('img_array.json', 'r') as infile:
    #     img_array_from_json = np.array(json.load(infile))

    # # check that the loaded numpy array has the same shape as the original array
    # assert img_array_from_json.shape == img_array.shape

    # # check that the loaded numpy array has the same values as the original array
    # assert np.array_equal(img_array_from_json, img_array)




try:
    prediction = main.classification_model(model, img_array)
    col2.metric(label="", value=prediction.replace("_", " "))
except:
    print('error with cnn')

try:
    col2.image(f"Ground_Truths/{prediction}.jpeg")
except:
    print('error with showing gt')

try:
    image = main.pose_detection_model(img, prediction)
    col2.image(image)
except:
    print('error with movenet')
