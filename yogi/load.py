
import tensorflow as tf

def loading_model():
    model = tf.keras.models.load_model("saved_models/model1")
    return model
