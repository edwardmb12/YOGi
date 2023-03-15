
from tensorflow.keras.models import load_model

def loading_model():
    model = load_model("../saved_models/model1")

    return model
