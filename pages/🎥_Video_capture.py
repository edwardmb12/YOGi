import streamlit as st

st.title("🎥 Video Capture")

from streamlit_webrtc import (
    VideoProcessorBase,
    webrtc_streamer,
    VideoHTMLAttributes)
from video import extract_and_plot
import threading


#Defining the variables
lock = threading.Lock()
img_container = {"frames":[]}

Extracting frames from the video input
class VideoProcessor(VideoProcessorBase):
    def __init__(self):
        self.style = 'color'

    def video_frame_callback(self):
        img = self.to_ndarray(format="bgr24")
        img = extract_and_plot(img)
        with lock:
            if img is not None:
                img_container["frames"].append(img)

def main():
    
    #Title, text, page setup
    page_bg_img = '''
    <style>
    body {
    background-image: url("https://getwallpapers.com/wallpaper/full/0/c/3/32197.jpg");
    background-size: cover;
    }
    </style>
    '''

    st.markdown(page_bg_img, unsafe_allow_html=True)

    st.markdown(f"<b style=text-align:left;>Video Camera goes here!</b>", unsafe_allow_html=True)
    playing = st.checkbox("Start/Stop", value=False)
    analysing=False

    #Recording the video
    if playing:
        st.session_state["photo_frames"]=[]
        webrtc_streamer(
            key="object-detection",
            video_frame_callback=VideoProcessor.video_frame_callback,
            media_stream_constraints={ "video": True},
            desired_playing_state=playing #link to Start/Stop button
             #, in_recorder_factory=recorder_factory
            , video_html_attrs = VideoHTMLAttributes(muted=True, volume=0, autoPlay=True, controls=False, stop=False #unabling the user to control video input
                                                    #,style={"border": "5px red solid", "margin": "0 auto", "width":"50%"}
                                                    )
             , rtc_configuration={"iceServers": [{"urls": ["stun:stun4.l.google.com:19302"]}]
                            }
        )

    # "stun:stun1.l.google.com:19302",
    # "stun:stun2.l.google.com:19302",
    # "stun:stun.l.google.com:19302",
    # "stun:stun3.l.google.com:19302",
    # "stun:stun4.l.google.com:19302",

    #Storing photo frames
    if 'photo_frames' not in st.session_state:
        st.session_state['photo_frames'] = img_container["frames"]
    else:
        if len(st.session_state['photo_frames']) < 1:
            st.session_state['photo_frames'] = img_container["frames"]


    #When the video input is done
    if not playing:
        #Extracting the frames
        full_frames=st.session_state["photo_frames"]




if __name__ == "__main__":
    main()
