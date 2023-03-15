import streamlit as st
import cv2
import numpy as np
import av
import mediapipe as mp
from streamlit_webrtc import webrtc_streamer, WebRtcMode, RTCConfiguration
from streamlit_webrtc import (
VideoProcessorBase,
webrtc_streamer,
VideoHTMLAttributes)
import threading
import matplotlib.pyplot as plt
from yogi import preprocessor, load, params, predict, main
from PIL import Image
import streamlit as st
import av
import queue
from datetime import datetime


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

MuiBox-root css-0
    </style>

"""

st.metric(label="video_captues", value="Video Capture")
st.markdown(page_bg_img, unsafe_allow_html=True)

model = load.loading_model()

#Defining the variables
lock = threading.Lock()
img_container = {"frames":[]}

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mpPose = mp.solutions.pose
pose = mpPose.Pose()
points = mpPose.PoseLandmark#(
    #model_complexity=0,
    #min_detection_confidence=0.5,
    #min_tracking_confidence=0.5)



def main(model=[],label=[]):

    class SignPredictor(VideoProcessorBase):

        def __init__(self) -> None:
            # Hand detector
            # self.hand_detector = HandDetector(detectionCon=0.5, maxHands=1)

            #Queue to share information that happen within the live video thread outside the thread
            self.result_queue = queue.Queue()

        def process(self, image):
            pass
            #move net in here?

        def recv(self, frame: av.VideoFrame) -> av.VideoFrame:
            #pose prediction
            image = frame.to_ndarray(format="rgb24")
            pose = main.classification_model(image_input=image, model=model)


            return av.VideoFrame.from_ndarray(image, format="rgb24"), st.markdown("prediction") #pass back image with move net on

    webrtc_streamer(
        key="object-detection",
        mode=WebRtcMode.SENDRECV,
        video_processor_factory=SignPredictor,
        media_stream_constraints={
            "video": True,
            "audio": False
        },
        async_processing=True,
    )





if __name__ == "__main__":
    main()
