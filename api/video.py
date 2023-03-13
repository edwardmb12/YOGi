import streamlit as st
import numpy as np
from PIL import Image
import pandas as pd
import mediapipe as mp
import cv2

def extract_and_plot(img):
    '''
    Extracts keypoints from image frame and plots these to generate a kinematic figure using Mediapipe's Pose Landmarks.
    '''
    mpPose = mp.solutions.pose
    pose = mpPose.Pose()
    mpDraw = mp.solutions.drawing_utils # For drawing keypoints
    points = mpPose.PoseLandmark # Landmarks
    data = []
    for p in points:
        x = str(p)[13:]
        data.append(x + "_x")
        data.append(x + "_y")
        data.append(x + "_z")
        data.append(x + "_vis")
    data = pd.DataFrame(columns = data)
    count = 0
    temp = []
    imageWidth, imageHeight = img.shape[:2]
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = pose.process(imgRGB)
    if results.pose_landmarks:
            mpDraw.draw_landmarks(img, results.pose_landmarks, mpPose.POSE_CONNECTIONS) #draw landmarks on image
            landmarks = results.pose_landmarks.landmark
            for i,j in zip(points,landmarks):
                    temp = temp + [j.x, j.y, j.z, j.visibility]
            data.loc[count] = temp
            count +=1
    cv2.imshow(img)
    cv2.waitKey(100)
