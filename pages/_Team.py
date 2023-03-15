import streamlit as st
from PIL import Image
import base64
import streamlit as st
# from functions import add_bg_from_local

# add_bg_from_local('images/art4 (1).jpg')

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

    [data-testid="stImage"] {
        border:5px;
        padding:10px;
        border-radius: 15px;
        background:#E6F3FB;
        box-shadow: 3px 3px #afdcf1;
        border-radius: 4px;
    }

    [data-testid="stText"] {
        background-color: #E6F3FB;
        border: 2px solid #afdcf1;
        padding: 2%;
        border-radius: 2px;
        box-shadow: 3px 3px #afdcf1;
        border-radius: 4px;
        opacity: 0.9
    }

    </style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)

photo = """
            <style type="text/css">
            div[data-testid="stHorizontalBlock"] {
                border:20px;
                padding:40px;
                border-radius: 10px;
                background:#FFFFFF;
            } <img src="images/team_yogi.jpg">
            </style>
        """


st.metric(label="", value="Meet the Team")

image = Image.open('images/team_yogi.jpg')
st.image(image, caption='Team Yogi')

st.text("Dolly, Ted, Victoria and Melvin")
