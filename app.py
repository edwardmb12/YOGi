import streamlit as st
import base64    #pip install pybase64
import streamlit.components.v1 as components
from PIL import Image
import os


st.set_page_config(layout="wide")

page_bg_img =  """
    <style>
    [data-testid="stMetricLabel"] {
        opacity:0;
        margin: -30px;
    }

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
        background-repeat: no-repeat
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

        [data-testid="stImage"] {
        border:5px;
        padding:10px;
        border-radius: 15px;
        background:#E6F3FB;
        box-shadow: 3px 3px #afdcf1;
        border-radius: 4px;
        width: 100%;
        max-height: 100px
        text-align: center;
        margin: 1%
    }

    [data-testid="stText"] {
        width: auto;
        text-align: center;
        display: block;
        position: relative;
        left: 0%;
        border:5px;
        padding:10px;
        border-radius: 15px;
        background:#E6F3FB;
        box-shadow: 3px 3px #afdcf1;
        border-radius: 4px;
        opacity: 0.9;
        margin: 3%
    }



    </style>
"""

st.sidebar.success("Select a page above.")

st.markdown(page_bg_img, unsafe_allow_html=True)

st.metric(label="", value="YOGi")

# slide_1 = Image.open(f'slides/Slide1.JPG')
# slide_2 = Image.open(f'slides/Slide2.JPG')
# slide_3 = Image.open(f'slides/Slide3.JPG')
# slide_4 = Image.open(f'slides/Slide4.JPG')
# slide_5 = Image.open(f'slides/Slide5.JPG')
# slide_6 = Image.open(f'slides/Slide6.JPG')
# slide_7 = Image.open(f'slides/Slide7.JPG')

# st.image(image=slide_1)
# st.image(image=slide_2)
# st.image(image=slide_3)
# st.image(image=slide_4)
# st.image(image=slide_5)
# st.image(image=slide_6)
# st.image(image=slide_7)

col1, col2 = st.columns(2)

col1.image("assets/images/about4.jpeg")
col2.image("assets/images/about.jpg")

st.text("""
        YOGi is for home-practising yogis to use while unassisted.
        The user feeds YOGi an image. It will then detect the pose,
        if the pose is sufficiently correct, and provide corrective feedback.
        """)
