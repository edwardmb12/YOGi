import streamlit as st
import cv2
import mediapipe as mp
import numpy as np

from video2 import webcam, classify_pose


mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose
mp_drawing_styles = mp.solutions.drawing_styles


'''
YOGI
'''

st.markdown('''
Here we are adding a webcam
''')

st.title("Pose Detection")
st.write("Press 'q' to quit.")

webcam()
