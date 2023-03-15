import streamlit as st
import cv2
import numpy as np
import av
import mediapipe as mp
from streamlit_webrtc import webrtc_streamer, WebRtcMode, RTCConfiguration
from streamlit_webrtc import (
VideoTransformerBase,
webrtc_streamer,
VideoHTMLAttributes)
from video import extract_and_plot
import threading
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

# def main():
#     class VideoTransformer(VideoTransformerBase):
#         frame_lock: threading.Lock  # `transform()` is running in another thread, then a lock object is used here for thread-safety.

#         out_image: Union[np.ndarray, None]

#         def __init__(self) -> None:
#             self.frame_lock = threading.Lock()

#             self.out_image = None

#         def transform(self, frame: av.VideoFrame) -> np.ndarray:
#             out_image = frame.to_ndarray(format="bgr24")

#             with self.frame_lock:

#                 self.out_image = out_image
#             return out_image

#     ctx = webrtc_streamer(key="snapshot", video_transformer_factory=VideoTransformer)

#     if ctx.video_transformer:

#         snap = st.button("Snapshot")
#         if snap:
#             with ctx.video_transformer.frame_lock:
#                 image = ctx.video_transformer.out_image

#         else:
#             st.warning("No frames available yet.")





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



class VideoProcessor():
    def recv(self, frame):
        img = frame.to_ndarray(format="bgr24")
        img = process(img)
        return av.VideoFrame.from_ndarray(img, format="bgr24")
webrtc_ctx = webrtc_streamer(
    key="WYH",
    mode=WebRtcMode.SENDRECV,
    rtc_configuration=RTC_CONFIGURATION,
    media_stream_constraints={"video": True, "audio": False},
    video_processor_factory=VideoProcessor,
    async_processing=True)

if webrtc_ctx.video_transformer:
    snap = st.button("Snapshot")
    if snap:
        image = webrtc_ctx.video_transformer.out_image
        st.image(image=image)

    else:
        st.warning("No frames available yet.")







# if __name__ == "__main__":
