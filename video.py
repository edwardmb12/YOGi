import cv2
import numpy as np
import av
import streamlit as st
from yogi.angle_calc import angle_calc
from helper_functions_init import run_inference, draw_prediction_on_image, determine_crop_region, KEYPOINT_DICT, KEYPOINT_EDGE_INDS_TO_COLOR, init_crop_region
from movenet_init import movenet
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
        self.keypoints_dict = {} #is this necessary? can we just use keypoints.dict

    def process(self, image):
        image_height, image_width, _ = image.shape
        keypoints_with_scores = run_inference(movenet, image, self.crop_region,crop_size=[192, 192])
        output_image = draw_prediction_on_image(image.astype(np.int32), keypoints_with_scores,
                            crop_region=None, close_figure=True, output_image_height=300)
        self.crop_region = determine_crop_region(keypoints_with_scores, image_height, image_width)
        return output_image, keypoints_with_scores

    def angle_calc(self, keypoints):
        '''
        Returns a dictionary of calculated angles from image frame.
        '''
        #1. load key points from process
        #2. map these values to KEYPOINT_DICT
        #3. perform calculate_angle for each key point
        #4. append to dictionary
        key_dict = {}
        for key, value in KEYPOINT_DICT.items():
            vector = tuple(key_xy[0, 0, value])
            key_dict[key] = vector

        def calculate_angle(a,b,c):
            a = np.array(a) # First
            b = np.array(b) # Mid
            c = np.array(c) # End
        #where are we getting a, b and c from?
        radians = np.arctan2(c[1]-b[1], c[0]-b[0]) - np.arctan2(a[1]-b[1], a[0]-b[0])
        angle = np.abs(radians*180.0/np.pi)

        if angle >180.0:
            angle = 360-angle

        return angle


    def recv(self, frame):
        img = frame.to_ndarray(format="bgr24")
        img = self.process(img).astype(np.uint8)
        img
        return av.VideoFrame.from_ndarray(img[0], format="bgr24")



webrtc_ctx = webrtc_streamer(
    key="WYH",
    mode=WebRtcMode.SENDRECV,
    rtc_configuration=RTC_CONFIGURATION,
    media_stream_constraints={"video": True, "audio": False},
    video_processor_factory=VideoProcessor,
    async_processing=True)
##
