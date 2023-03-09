import matplotlib.pyplot as plt
import random
import os
import numpy as np
import cv2
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras import utils, optimizers
from PIL import Image
import shutil
from tensorflow.keras import models, layers
from tensorflow.keras.applications import vgg16
from tensorflow.keras.callbacks import EarlyStopping



import glob
import os
import time
import pickle
from tensorflow import keras
import mlflow
from mlflow.tracking import MlflowClient



def create_data():
    train_dir = "../raw_data/Training"
    img_height, img_width = 256, 256
    batch_size = 32
    train_datagen = ImageDataGenerator(rescale=1./255,
                                    vertical_flip=True,
                                    validation_split=0.2) # set validation split

    train_generator = train_datagen.flow_from_directory(
                                        train_dir,
                                        target_size=(img_height, img_width),
                                        batch_size=batch_size,
                                        class_mode='categorical',
                                        subset='training',
                                        keep_aspect_ratio=True,
                                        interpolation='bicubic') # set as training data

    validation_generator = train_datagen.flow_from_directory(
                                        train_dir, # same directory as training data
                                        target_size=(img_height, img_width),
                                        batch_size=batch_size,
                                        class_mode='categorical',
                                        subset='validation',
                                        keep_aspect_ratio=True,
                                        interpolation='bicubic') # set as validation data


def model_1():
    train_generator, validation_generator = create_data()
    img_height, img_width = 256, 256
    base_model = vgg16.VGG16(
                        include_top=False,
                        weights='imagenet',
                        input_shape=(img_height, img_width, 3),
                        classifier_activation='softmax')

    base_model.trainable = False
    model = models.Sequential([
        base_model,
        layers.Flatten(),
        layers.Dropout(0.2),
        layers.Dense(800,activation="relu"),
        layers.Dropout(0.3),
        layers.Dense(600, activation="relu"),
        layers.Dense(83, activation="softmax")
    ])


    opt = optimizers.Adam(learning_rate=0.0001)
    model.compile(optimizer=opt,
                loss='categorical_crossentropy',
                metrics=['accuracy'])


    es = EarlyStopping(patience=1, restore_best_weights=True)
    batch_size = 32
    history = model.fit(
                train_generator,
                steps_per_epoch = train_generator.samples // batch_size,
                validation_data = validation_generator,
                validation_steps = validation_generator.samples // batch_size,
                epochs=1,
                callbacks=[es])

    params = {
        "layer"
    }

    return history

def save_results():

def save_model():
    if MODEL_TARGET == "mlflow":
    # $CHA_BEGIN
        mlflow.tensorflow.log_model(model=model,
                                artifact_path="model",
                                registered_model_name="yogi_DollyBelcher"
                                )
    print("✅ Model saved to mlflow")
    return None



if __name__=='__main__':
    create_data()
    model_1()
