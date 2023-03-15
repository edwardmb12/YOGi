from yogi.params import POSES_LIST

def pred(model, preprocessed_image):
    y_pred = model.predict(preprocessed_image)

    return POSES_LIST[y_pred.argmax()], y_pred.max()
