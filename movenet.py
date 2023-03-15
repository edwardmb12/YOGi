import tensorflow_hub as hub
from tensorflow_docs.vis import embed
from tensorflow import lite
#import tflite_runtime.interpreter as tflite
from tensorflow import cast, uint8

from matplotlib.collections import LineCollection
import matplotlib.patches as patches

import imageio
from IPython.display import HTML, display

import numpy as np
import matplotlib.pyplot as plt
import cv2

model_path = "saved_models/lite-model_movenet_singlepose_lightning_tflite_float16_4.tflite"
  # Initialize the TFLite interpreter
interpreter = lite.Interpreter(model_path=model_path)
interpreter.allocate_tensors()

def movenet(input_image):
    """Runs detection on an input image.

    Args:
      input_image: A [1, height, width, 3] tensor represents the input image
        pixels. Note that the height/width should already be resized and match the
        expected input resolution of the model before passing into this function.

    Returns:
      A [1, 1, 17, 3] float numpy array representing the predicted keypoint
      coordinates and scores.
    """
    # TF Lite format expects tensor type of uint8.
    input_image = cast(input_image, dtype=uint8)#tensorflow.uint8)
    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()
    interpreter.set_tensor(input_details[0]['index'], input_image.numpy())
    # Invoke inference.
    interpreter.invoke()
    # Get the model prediction.
    keypoints_with_scores = interpreter.get_tensor(output_details[0]['index'])
    return keypoints_with_scores


#def movenet(input_image):
    """Runs detection on an input image.

    Args:
      input_image: A [1, height, width, 3] tensor represents the input image
        pixels. Note that the height/width should already be resized and match the
        expected input resolution of the model before passing into this function.

    Returns:
      A [1, 1, 17, 3] float numpy array representing the predicted keypoint
      coordinates and scores.
    """
    #model = module.signatures['serving_default']

    # SavedModel format expects tensor type of int32.
    #input_image = cast(input_image, dtype=int32)#tf.int32)
    # Run model inference.
    #outputs = model(input_image)
    # Output is a [1, 1, 17, 3] tensor.
    #keypoints_with_scores = outputs['output_0'].numpy()
    #return keypoints_with_scores
