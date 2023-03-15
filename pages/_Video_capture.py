import streamlit as st
import cv2
import numpy as np
import av
import mediapipe as mp
from streamlit_webrtc import webrtc_streamer, WebRtcMode, RTCConfiguration
from streamlit_webrtc import (
VideoTransformerBase,
VideoProcessorBase,
webrtc_streamer,
VideoHTMLAttributes)
import threading
import matplotlib.pyplot as plt
from yogi import preprocessor, load_predict, params
from PIL import Image
#need to import position detection and feed in an image


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

st.metric(label="", value="Video Capture")
st.markdown(page_bg_img, unsafe_allow_html=True)



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




class VideoProcessor(VideoProcessorBase):
    def __init__(self):
        self.style = 'color'

    def video_frame_callback(self):
        img = self.to_ndarray(format="bgr24")
        with lock:
            if img is not None:
                img_container["frames"].append(img)




def main():
    playing = st.checkbox("Start/Stop", value=False)

    if playing:
        st.session_state["photo_frames"]=[]
        webrtc_streamer(
            key="object-detection",
            video_frame_callback=VideoProcessor.video_frame_callback,
            media_stream_constraints={
                "video": True
            },
            desired_playing_state=playing #link to Start/Stop button
            ,  rtc_configuration={"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]
                            }
        )

    #Storing photo frames
    if 'photo_frames' not in st.session_state:
        st.session_state['photo_frames'] = img_container["frames"]
    else:
        if len(st.session_state['photo_frames']) < 1:
            st.session_state['photo_frames'] = img_container["frames"]

    if not playing:
        #Extracting the frames
        full_frames=st.session_state["photo_frames"]


#full frames is a list of an arrays of each image




def process(image):
    image.flags.writeable = False
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = pose.process(image)
# Draw the hand annotations on the image.
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    if results.pose_landmarks:
        mp_drawing.draw_landmarks(image, results.pose_landmarks, mpPose.POSE_CONNECTIONS
            #, mp_drawing_styles.get_default_hand_landmarks_style(),
            #mp_drawing_styles.get_default_hand_connections_style()
            )
        landmarks = results.pose_landmarks.landmark
    return cv2.flip(image, 1)
RTC_CONFIGURATION = RTCConfiguration(
    {"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]}
)






if __name__ == "__main__":
    main()
