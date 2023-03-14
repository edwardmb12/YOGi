
import matplotlib.pyplot as plt
from tensorflow.image import ResizeMethod
from tensorflow.image import resize_with_pad
from tensorflow import reshape
from yogi.params import IMG_HEIGHT
from yogi.params import IMG_WIDTH


def preprocess_image(image_input):
    preproc_image = resize_with_pad(
                                image_input,
                                IMG_HEIGHT,
                                IMG_WIDTH,
                                method=ResizeMethod.LANCZOS3,
                                )

    preproc_image = preproc_image/255.0
    preproc_image = reshape(preproc_image, (1, IMG_HEIGHT, IMG_WIDTH, 3))

    return preproc_image

if __name__ == '__main__':
    chosen_file = "images/dfd_test.jpeg"
    chosen_file = plt.imread(chosen_file)
    test_image = preprocess_image(chosen_file)
    print(test_image.shape, type(test_image))
