
from tensorflow.keras.models import load_model

def pred(preprocessed_image):
    model = load_model("../saved_models/model_final.h5")
    y_pred = model.predict(preprocessed_image)

    return y_pred # returns list of probabilities
