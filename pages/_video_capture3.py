import streamlit as st
from PIL import Image
import numpy as np
import json
import pandas as pd

img_file_buffer = st.camera_input("Take a picture")

if img_file_buffer is not None:
    # To read image file buffer as a PIL Image:
    img = Image.open(img_file_buffer)
    #img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    # To convert PIL Image to numpy array:
    img_array = np.array(img)

    # Check the type of img_array:
    # Should output: <class 'numpy.ndarray'>
    st.write(type(img_array))

    # Check the shape of img_array:
    # Should output shape: (height, width, channels)
    st.write(img_array.shape)
    st.write(img_array)

    # save the numpy array to a JSON file
    with open('img_array.json', 'w') as outfile:
        json.dump(img_array.tolist(), outfile)

    # load the numpy array from the JSON file and reshape it to its original form
    with open('img_array.json', 'r') as infile:
        img_array_from_json = np.array(json.load(infile))

    # check that the loaded numpy array has the same shape as the original array
    assert img_array_from_json.shape == img_array.shape

    # check that the loaded numpy array has the same values as the original array
    assert np.array_equal(img_array_from_json, img_array)

    
