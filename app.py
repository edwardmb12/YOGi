import streamlit as st
import base64    #pip install pybase64
import streamlit.components.v1 as components
from PIL import Image

st.set_page_config(
    page_title="Yogi",
    page_icon="ॐ",
)

page_bg_img =  """
    <style>

    [data-testid="stSidebarNav"] {
        background: url("https://images.fineartamerica.com/images/artworkimages/mediumlarge/2/sacred-geometry-contemporary-art-metatrons-cube-dean-marston.jpg");
        background-size: cover;
        background-position: top left;
        background-repeat: no-repeat;
    }
    [data-testid="stSidebar"] {
        background: url("https://images.fineartamerica.com/images/artworkimages/mediumlarge/2/sacred-geometry-contemporary-art-metatrons-cube-dean-marston.jpg");
        background-size: cover;
        background-position: top left;
        background-repeat: no-repeat;
    }
    [data-testid="stAppViewContainer"] {
        background-position:center;
        background: url("http://www.mikesastrophotos.com/wp-content/uploads/2013/01/v4-heart-nebula-sm.jpg");
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
    </style>
"""
# [data-testid="stSidebarNav"] {
#     background: url("https://images.fineartamerica.com/images/artworkimages/mediumlarge/2/sacred-geometry-contemporary-art-metatrons-cube-dean-marston.jpg")
#     }
#
st.markdown(page_bg_img, unsafe_allow_html=True)

original_title = '<p style="font-family:Courier; color:white; font-size: 40px;">Yoga Pose Detection</p>'
st.markdown(original_title, unsafe_allow_html=True)

st.title("")
st.sidebar.success("Select a page above.")

# with open('style.css') as f:
#     st.markdown(f'<style>{f.read()}</style>',unsafe_allow_html=True)

# # col1, col2 = st.columns(2)
# # col1.metric("Column1")
# # col1.metric("Column2")

# components.html(
#     """
#     <head>
#     <link href="{% static 'fontawesomefree/css/fontawesome.css' %}" rel="stylesheet" type="text/css">
#     <link href="{% static 'fontawesomefree/css/brands.css' %}" rel="stylesheet" type="text/css">
#     <link href="{% static 'fontawesomefree/css/solid.css' %}" rel="stylesheet" type="text/css">
#     </head>
#     <i class="fa-solid fa-om"></i>
#     """,
# )
