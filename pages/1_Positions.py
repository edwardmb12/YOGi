import streamlit as st
import base64
from PIL import Image
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

    [data-testid="stMetricValue"] {
        background-color: #E6F3FB;
        border: 2px solid #c5d1f6;
        padding: 2%;
        box-shadow: 3px 3px #afdcf1;
        border-radius: 4px;
        opacity: 0.8;
        text-align: center
    }

    [data-testid="css-bibxuw effi0qh3"] {
        background-color: #E6F3FB;
        border: 2px solid #c5d1f6;
        padding: 1%;
        box-shadow: 3px 3px #afdcf1;
        border-radius: 4px;
        opacity: 0.8
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

    [class="css-bibxuw effi0qh3"] {
        border:1px;
        padding:2px;
        border-radius: 1px;
        background:#E6F3FB;
        box-shadow: 3px 3px #afdcf1;
        border-radius: 4px;
        opacity: 0.8
    }

    </style>

"""


st.markdown(page_bg_img, unsafe_allow_html=True)

st.metric(label="", value="Positions")

pose = st.text_input("What pose would you like to see?", value="Downward Dog")

# col1, col2 = st.columns(2)

# image1 = Image.open(f'YOGI_Ground_Truths_new/poses/{pose}.jpeg')
# image2 = Image.open(f'YOGI_Ground_Truths_new/poses_defined/{pose}.jpeg')
# col1.image(image1, caption=pose)
# col2.image(image2, caption=pose)

image = Image.open(f'pose_search/poses/{pose}.jpeg')
st.image(image=image, caption=pose)
