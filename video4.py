import cv2
import numpy as np
import av
from helper_functions import run_inference, draw_prediction_on_image, determine_crop_region
from movenet import movenet
from streamlit_webrtc import webrtc_streamer, WebRtcMode, RTCConfiguration

input_size = 192

def process(image):
    image_height, image_width, _ = image.shape
    keypoints_with_scores = run_inference(movenet, image, crop_region,crop_size=[input_size, input_size])
    crop_region = determine_crop_region(keypoints_with_scores, image_height, image_width)
    output_image = draw_prediction_on_image(image.numpy().astype(np.int32), keypoints_with_scores,
                        crop_region=crop_region, close_figure=True, output_image_height=300)
    #crop_region = determine_crop_region(keypoints_with_scores, image_height, image_width)
    return output_image
RTC_CONFIGURATION = RTCConfiguration(
    {"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]}
)
class VideoProcessor:
    def __init__(self) -> None:
        self.count = 0
    def recv(self, frame):
        if self.count % 6 == 0: # adds a counter to process every 4 frames
            img = frame.to_ndarray(format="bgr24")
            img = process(img)
            return av.VideoFrame.from_ndarray(img, format="bgr24")
        self.count += 1

webrtc_ctx = webrtc_streamer(
    key="WYH",
    mode=WebRtcMode.SENDRECV,
    rtc_configuration=RTC_CONFIGURATION,
    media_stream_constraints={"video": True, "audio": False},
    video_processor_factory=VideoProcessor,
    async_processing=True)
##
