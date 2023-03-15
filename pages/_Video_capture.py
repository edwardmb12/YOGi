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
from yogi import preprocessor, load, predict, main
from PIL import Image
import streamlit as st
import av
import queue
# from helper_functions import run_inference, draw_prediction_on_image, determine_crop_region, KEYPOINT_DICT, KEYPOINT_EDGE_INDS_TO_COLOR, init_crop_region


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


col1, col2 = st.columns([3,1])


class SignPredictor(VideoProcessorBase):
    def __init__(self) -> None:
        # Hand detector
        # self.hand_detector = HandDetector(detectionCon=0.5, maxHands=1)

        #Queue to share information that happen within the live video thread outside the thread
        self.result_queue = queue.Queue()


    def predict_pose(self):
        #get every fourth frame
        pose = main.classification_model(image, model)
        if pose == "Detecting Pose ...":
            pass
        else:
            im1 = f"Ground_Truths/{pose}.jpeg"
            col2.text(pose)
            col2.image(im1)


    def process(self, image):
        pass
        #move net in here?

    def recv(self, frame: av.VideoFrame) -> av.VideoFrame:
        #pose prediction
        image = frame.to_ndarray(format="rgb24")
        processed_image = preprocessor.preprocess_image(image)
        pose, probab= predict.pred(processed_image, model)

        return av.VideoFrame.from_ndarray(image, format="rgb24") #pass back image with move net on


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

# RTC_CONFIGURATION = RTCConfiguration(
#     {"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]}
# )

# class VideoProcessor:
#     def __init__(self) -> None:
#         self.count = 0
#         self.crop_region = init_crop_region(300, 300)

#     def process(self, image):
#         image_height, image_width, _ = image.shape
#         keypoints_with_scores = run_inference(movenet, image, self.crop_region,crop_size=[192, 192])
#         output_image = draw_prediction_on_image(image.astype(np.int32), keypoints_with_scores,
#                             crop_region=None, close_figure=True, output_image_height=300)
#         self.crop_region = determine_crop_region(keypoints_with_scores, image_height, image_width)
#         return output_image

#     def predict_pose(self):
#         #get every fourth frame
#         pose = main.classification_model(image, model)
#         if pose == "Detecting Pose ...":
#             pass
#         else:
#             im1 = f"Ground_Truths/{pose}.jpeg"
#             col2.text(pose)
#             col2.image(im1)

#     def recv(self, frame):
#         img = frame.to_ndarray(format="bgr24")
#         img = self.process(img).astype(np.uint8)
#         return av.VideoFrame.from_ndarray(img, format="bgr24")



# webrtc_ctx = webrtc_streamer(
#     key="WYH",
#     mode=WebRtcMode.SENDRECV,
#     rtc_configuration=RTC_CONFIGURATION,
#     media_stream_constraints={"video": True, "audio": False},
#     video_processor_factory=VideoProcessor,
#     async_processing=True)
