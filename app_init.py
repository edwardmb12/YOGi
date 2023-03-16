import cv2
import numpy as np
import av
import streamlit as st
from helper_functions import run_inference, draw_prediction_on_image, determine_crop_region, KEYPOINT_DICT, KEYPOINT_EDGE_INDS_TO_COLOR, init_crop_region
from movenet import movenet
from streamlit_webrtc import webrtc_streamer, WebRtcMode, RTCConfiguration

input_size = 192

st.write("## Movenet")

RTC_CONFIGURATION = RTCConfiguration(
    {"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]}
)

class VideoProcessor:
    def __init__(self) -> None:
        self.count = 0
        self.crop_region = init_crop_region(300, 300)

    def process(self, image):
        image_height, image_width, _ = image.shape
        keypoints_with_scores = run_inference(movenet, image, self.crop_region,crop_size=[192, 192])
        output_image = draw_prediction_on_image(image.astype(np.int32), keypoints_with_scores,
                            crop_region=None, close_figure=True, output_image_height=300)
        self.crop_region = determine_crop_region(keypoints_with_scores, image_height, image_width)
        return output_image

    def recv(self, frame):
        img = frame.to_ndarray(format="bgr24")
        img = self.process(img).astype(np.uint8)
        return av.VideoFrame.from_ndarray(img, format="bgr24")



webrtc_ctx = webrtc_streamer(
    key="WYH",
    mode=WebRtcMode.SENDRECV,
    rtc_configuration=RTC_CONFIGURATION,
    media_stream_constraints={"video": True, "audio": False},
    video_processor_factory=VideoProcessor,
    async_processing=True)
##
