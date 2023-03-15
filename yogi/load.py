
import tensorflow as tf
import streamlit as st


@st.cache_resource
def loading_model():
    model = tf.keras.models.load_model("saved_models/model1")
    return model
